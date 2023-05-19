import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64
from base64 import b64encode


def main():
    print("Welcome to Enc/Dec software tool!")

    while True:
        print("=================================")
        print("Please choose your command.")
        print("Commands:")
        print("--encrypt")
        print("--exit")
        main_command = input().lower()
        if main_command == "--encrypt":
            while True:
                print("=================================")
                print("Commands:")
                print("--input [string]")
                print("--back")
                encrypt_command = input().lower()
                if encrypt_command[0:8] == "--input ":
                    input_string = encrypt_command[8:]
                    print (f"Entered string: {input_string}")
                    print ("Please enter a password:")
                    password = input()
                    print (f"Entered password: {password}")
                    password_bytes = bytes(password, "utf-8")
                    salt = os.urandom(16)
                    f = open("salt.txt","w+")
                    f.write(b64encode(salt).decode("utf-8"))
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
                elif encrypt_command == "--back":
                    break
                else:
                    print("Error: Command not found.")
        elif main_command == "--exit":
            break
        else:
            print("Error: Command not found.")


if __name__ == "__main__":
    main()