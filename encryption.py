import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64


def encrypt(input_string, password_string):
    password_bytes = password_string.encode("utf-8")
    print (f"Password converted to bytes: {password_bytes}")
    salt_bytes = os.urandom(16) # Salt is used as a byte
    print(f"Salt bytes= {salt_bytes}")
    salt64_bytes = base64.b64encode(salt_bytes)
    print(f"Salt64 bytes = {salt64_bytes}")
    salt64_string = salt64_bytes.decode("utf-8") # In order to save the salt, we convert it into a base64 string
    print(f"Salt64 string= {salt64_string}")
    salt_file = open("salt-value","w+")
    salt_file.write(salt64_string)
    salt_file.close()
    kdf = Scrypt(
        salt=salt_bytes,
        length=32,
        n=2**14,
        r=8,
        p=1,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    print (f"Key: {key}")
    key_file = Fernet(key)
    input_string_bytes = bytes(input_string, "utf-8")
    print (f"String converted to bytes: {input_string_bytes}")
    token_bytes = key_file.encrypt (input_string_bytes)
    print (f"Encrypted string: {token_bytes}")
    token_string = token_bytes.decode("utf-8")
    message_file = open("encrypted-message","w+")
    message_file.write(token_string)
    message_file.close()