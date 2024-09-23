from flask import Flask, request, jsonify
import jwt
import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import base64  
import json

app = Flask(__name__)

# Store keys and their metadata
keys = {}

def generate_key(kid):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    key_data = {
        "kid": kid,
        "private_key": private_key,
        "public_key": public_key,
        "expires_at": datetime.datetime.utcnow() + datetime.timedelta(days=1)  # expires in 1 day
    }
    keys[kid] = key_data
    return public_key

# Generate a key when the server starts
generate_key("key1")

@app.route('/.well-known/jwks.json', methods=['GET'])
def jwks():
    # Filter out expired keys
    valid_keys = [
        {
            "kty": "RSA",
            "kid": key_data["kid"],
            "n": base64.urlsafe_b64encode(key_data["public_key"].public_bytes(
                encoding=serialization.Encoding.DER,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )).decode('utf-8'),
            "e": "AQAB"  # Fixed exponent
        }
        for key_data in keys.values() if key_data["expires_at"] > datetime.datetime.utcnow()
    ]
    return jsonify({"keys": valid_keys})

@app.route('/auth', methods=['POST'])
def auth():
    expired = request.args.get('expired')
    kid = "key1"  # Use the generated key
    if kid not in keys:
        return jsonify({"error": "Key not found"}), 404

    if expired:
        # Issue JWT with an expired key
        expiration = datetime.datetime.utcnow() - datetime.timedelta(days=1)  # expired
    else:
        expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    token = jwt.encode(
        {"some": "data", "exp": expiration, "kid": kid},
        keys[kid]["private_key"],
        algorithm='RS256'
    )
    return jsonify({"token": token})

if __name__ == '__main__':
    app.run(port=8080)
