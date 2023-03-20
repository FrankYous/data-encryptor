#import os
#from cryptography.fernet import fernet


def main():
    print("Welcome to Enc/Dec software tool! Please choose your command.")
    print("Commands:")
    print("--exit")

    while True:
        command = input()

        if command == "--exit":
            return
        else:
            print("Error: Command not found.")


main()