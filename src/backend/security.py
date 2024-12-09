from cryptography.fernet import Fernet
from typing import Dict
import os

class KeyEncryption:
    def __init__(self):
        # In production, store this key securely (e.g., in environment variables)
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
    
    def encrypt_keys(self, api_keys: Dict[str, str]) -> Dict[str, str]:
        """Encrypt API keys before storing"""
        encrypted_keys = {}
        for key, value in api_keys.items():
            if value:
                encrypted_value = self.cipher_suite.encrypt(value.encode())
                encrypted_keys[key] = encrypted_value.decode()
        return encrypted_keys
    
    def decrypt_keys(self, encrypted_keys: Dict[str, str]) -> Dict[str, str]:
        """Decrypt API keys for use"""
        decrypted_keys = {}
        for key, value in encrypted_keys.items():
            if value:
                decrypted_value = self.cipher_suite.decrypt(value.encode())
                decrypted_keys[key] = decrypted_value.decode()
        return decrypted_keys