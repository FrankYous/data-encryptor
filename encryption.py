import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64


def encrypt(file_name, input_string, password_string):
    password_bytes = password_string.encode("utf-8")

    salt_bytes = os.urandom(16) # Salt is generated as a byte
    salt64_bytes = base64.b64encode(salt_bytes) # The salt is then converted to base 64 byte.
    salt64_string = salt64_bytes.decode("utf-8") # In order to save the salt, we convert it into a base64 string

    kdf = Scrypt(
        salt=salt_bytes,
        length=32,
        n=2**14,
        r=8,
        p=1,
    )

    key = base64.b64encode(kdf.derive(password_bytes))
    key_file = Fernet(key)
    input_string_bytes = bytes(input_string, "utf-8")
    token_bytes = key_file.encrypt(input_string_bytes)
    token_string = token_bytes.decode("utf-8")

    enc_file_name = file_name + ".enc"
    enc_file_path = "files/" + enc_file_name
    with open(enc_file_path,"w+") as enc_file:
        enc_file.writelines([f"Salt: {salt64_string}\n", f"Token: {token_string}"])
