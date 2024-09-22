from flask import jsonify
from key_manager import KeyManager
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

key_manager = KeyManager()

def get_jwks():
    public_keys = key_manager.get_public_keys()
    jwks = {
        "keys": []
    }
    for kid, public_key in public_keys.items():
        # Convert PEM public key to JWKS format
        public_key_obj = serialization.load_pem_public_key(public_key.encode(), backend=default_backend())
        public_numbers = public_key_obj.public_numbers()

        jwk = {
            "kty": "RSA",
            "kid": kid,
            "use": "sig",
            "alg": "RS256",
            "n": base64.urlsafe_b64encode(public_numbers.n.to_bytes(256, 'big')).decode('utf-8'),
            "e": base64.urlsafe_b64encode(public_numbers.e.to_bytes(3, 'big')).decode('utf-8')
        }
        jwks["keys"].append(jwk)

    return jsonify(jwks), 200
