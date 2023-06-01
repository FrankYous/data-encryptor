from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64

def decrypt(file_name, input_string, password_string):
    password_bytes = password_string.encode("utf-8")

    enc_file_path = "files/" + file_name


    try:
        input_lines = input_string.split("\n")
        if len(input_lines) != 2:
            raise Exception
        salt_line, token_line = input_lines
        if salt_line[0:6] != "Salt: " or token_line[0:7] != "Token: ":
            raise Exception
    except Exception:
        print ("Invalid file format!")
        return

    salt64_string = salt_line[6:]
    token64_string = token_line[7:]

    salt64_bytes = salt64_string.encode("utf-8")
    salt_bytes = base64.b64decode(salt64_bytes)

    kdf = Scrypt(
        salt = salt_bytes,
        length = 32,
        n=2**14,
        r=8,
        p=1
    )

    key = base64.b64encode(kdf.derive(password_bytes))
    key_file = Fernet(key)
    token64_bytes = token64_string.encode("utf-8")
    try:
        original_bytes = key_file.decrypt(token64_bytes)
    except InvalidToken:
        print('Invalid password!')
        return
    original_string = original_bytes.decode("utf-8")
    dec_file_name = file_name + ".dec"
    dec_file_path = "files/" + dec_file_name
    with open(dec_file_path, "w+") as dec_file:
        dec_file.write(original_string)