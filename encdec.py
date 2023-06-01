import os
from encryption import encrypt
from decryption import decrypt


def main():
    print("Welcome to Enc/Dec software tool!")

    while True:
        print("=================================")
        print("Please enter a number:")
        print("1: Encrypt")
        print("2: Decrypt")
        print("0: Exit")
        print("=================================")
        main_command = input().lower()
        if main_command == "1":
            while True:
                print("=================================")
                print("Please enter the name of the file with the following format without brackets:")
                print("file:[name of the file]")
                print("To return, enter 0")
                print("=================================")
                encrypt_command = input().lower()
                if encrypt_command[0:5] == "file:":
                    file_name = encrypt_command[5:]
                    file_path = "files/" + file_name
                    with open(file_path, "r") as raw_file:
                        raw_string = raw_file.read()
                    print ("Please enter a password:")
                    password = input()
                    encrypt (file_name, raw_string, password)
                elif encrypt_command == "0":
                    break
                else:
                    print("Error: Command not found.")
        elif main_command == "2":
            while True:
                print("=================================")
                print("Please enter the name of the file with the following format without brackets:")
                print("file:[name of the file]")
                print("To return, enter 0")
                print("=================================")
                decrypt_command = input().lower()
                if decrypt_command[0:5] == "file:":
                    file_name = decrypt_command[5:]
                    file_path = "files/" + file_name
                    with open(file_path, "r") as enc_file:
                        enc_string = enc_file.read()
                    print ("Please enter a password:")
                    password = input()
                    decrypt(file_name, enc_string, password)
                elif decrypt_command == "0":
                    break
                else:
                    print("=================================")
                    print("Error: Command not found.")
        elif main_command == "0":
            break
        else:
            print("=================================")
            print("Error: Command not found.")


if __name__ == "__main__":
    main()