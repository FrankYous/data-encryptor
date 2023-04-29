#import os
#from cryptography.fernet import fernet


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
                if encrypt_command[0:7] == "--input":
                    break
                if encrypt_command == "--back":
                    break
                else:
                    print("Error: Command not found.")
        elif main_command == "--exit":
            break
        else:
            print("Error: Command not found.")


main()