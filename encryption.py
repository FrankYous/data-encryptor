import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64


def encrypt():
    password_bytes = bytes(password, "utf-8")
    salt = os.urandom(16)
    f = open("salt-value","w+")
    f.write(base64.b64encode(salt).decode("utf-8"))
    f.close()
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    print (f"Password converted to bytes: {password_bytes}")
    print (f"Key: {key}")
    f = Fernet(key)
    input_string_bytes = bytes(input_string, "utf-8")
    print (f"String converted to bytes: {input_string_bytes}")
    token = f.encrypt (input_string_bytes)
    print (f"Encrypted string: {token}")
    f = open("encrypted-message","w+")
    f.write(base64.b64encode(token).decode("utf-8"))
    f.close()