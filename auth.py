import time
import jwt
from flask import request, jsonify
from key_manager import KeyManager

key_manager = KeyManager()

def issue_jwt(expired=False):
    kid, private_key = key_manager.get_first_private_key()
    if not kid:
        return jsonify({"error": "No valid key found"}), 500

    exp_time = time.time() + 3600  # 1 hour expiration for normal token
    if expired:
        exp_time = time.time() - 3600  # Expired token

    token = jwt.encode({
        'iss': 'auth-server',
        'exp': exp_time,
        'sub': 'dummy_user',
        'kid': kid
    }, private_key, algorithm='RS256')

    return jsonify({'token': token}), 200
