from encryption import encrypt
from decryption import decrypt


def main():
    print("Welcome to Enc/Dec software tool!")

    while True:
        print("=================================")
        print("Please choose your command.")
        print("Commands:")
        print("--encrypt")
        print("--decrypt")
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
                    encrypt (input_string, password)
                elif encrypt_command == "--back":
                    break
                else:
                    print("Error: Command not found.")
        elif main_command == "--decrypt":
            while True:
                print("=================================")
                print("Commands:")
                print("--input")
                print("--back")
                decrypt_command = input().lower()
                if decrypt_command == "--input":
                    message_file = open("encrypted-message", "r")
                    if message_file.mode == "r":
                        input_string = message_file.read()
                    print ("Please enter a password:")
                    password = input()
                    decrypt(input_string, password)
                elif decrypt_command == "--back":
                    break
                else:
                    print("Error: Command not found.")
        elif main_command == "--exit":
            break
        else:
            print("Error: Command not found.")


if __name__ == "__main__":
    main()