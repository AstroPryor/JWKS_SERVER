import os
import time
import uuid
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class KeyManager:
    def __init__(self):
        self.keys = {}
        self.expiry_time = 24 * 3600  # Keys valid for 24 hours
        self.generate_new_key()

    def generate_new_key(self):
        # Generate RSA key pair
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_key = private_key.public_key()
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        # Assign key ID and expiry
        kid = str(uuid.uuid4())
        expiry = time.time() + self.expiry_time
        self.keys[kid] = {
            'private': private_pem.decode('utf-8'),
            'public': public_pem.decode('utf-8'),
            'expiry': expiry
        }
    
    def clean_expired_keys(self):
        current_time = time.time()
        self.keys = {k: v for k, v in self.keys.items() if v['expiry'] > current_time}
    
    def get_public_keys(self):
        self.clean_expired_keys()
        return {kid: key['public'] for kid, key in self.keys.items() if key['expiry'] > time.time()}
    
    def get_private_key(self, kid):
        self.clean_expired_keys()
        return self.keys.get(kid, {}).get('private')
    
    def get_first_private_key(self):
        # Get the first unexpired key pair
        self.clean_expired_keys()
        if self.keys:
            for kid, key in self.keys.items():
                return kid, key['private']
        return None, None