from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64

def decrypt(input_string, password_string):
    password_bytes = password_string.encode("utf-8")
    salt_file = open("salt-value", "r")
    if salt_file.mode == "r":
        salt64_string = salt_file.read()
    salt_file.close()
    salt64_bytes = salt64_string.encode("utf-8")
    salt_bytes = base64.b64decode(salt64_bytes)
    kdf = Scrypt(
        salt = salt_bytes,
        length = 32,
        n=2**14,
        r=8,
        p=1
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    key_file = Fernet(key)
    input_string_bytes = input_string.encode("utf-8")
    try:
        original_bytes = key_file.decrypt(input_string_bytes)
        original_string = original_bytes.decode("utf-8")
        print(original_string)
    except Exception:
        print('Invalid Password!')