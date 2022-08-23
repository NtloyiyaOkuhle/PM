import colorama
from colorama import Fore
colorama.init(autoreset=True)

def encrypt(data, shift):
    encrypted = ""
    for i in range(len(data)):
        char = data[i]
        if (char.isupper()):
            encrypted += chr((ord(char) + shift - 65) % 26 + 65)
        elif (char.islower()):
            encrypted += chr((ord(char)+ shift - 97) % 26 + 97)
        elif (char.isdigit()):
            number = (int(char) + shift) % 10
            encrypted += str(number)
        else:
            encrypted += char
    return encrypted

def decrypt(data, shift):
    decrypted = ""
    for i in range(len(data)):
        char = data[i]
        if (char.isupper()):
            decrypted += chr((ord(char) + shift - 65) % 26 + 65)
        elif (char.islower()):
            decrypted += chr((ord(char)+ shift - 97) % 26 + 97)
        elif (char.isdigit()):
            number = (int(char) + shift) % 10
            decrypted += str(number)
        else:
            decrypted += char
    return decrypted



menu = ""

while menu != '1' or menu != '2':
    menu = input(f"{Fore.YELLOW}Would you like to save a new password or view old one?"
                 "\n1. Input new password"
                 "\n2. View passwords"
                 "\n3. Exit"
                 "\n>>>: ")
    if menu == '1':
        softwareName = input("Enter the name of the software: ")
        username = input(f"{Fore.YELLOW}Enter your username for this software: ")
        password = input(f"{Fore.YELLOW}Enter your password for this software: ")
        shift = 5
        file = open("SecurePasswordData.txt", "a")
        file.write(encrypt(softwareName,shift) +";|"+encrypt(username,shift)+ ";|"+encrypt(password,shift)+"\n")
        file.close()
    if menu == '2':
        file = open("securePasswordData.txt", "r")
        print(f"{Fore.GREEN}Software\tUsername\tPassword")
        for i in file:
            data = i.split(";|")
            print(data[0]+"\t\t"+data[1]+"\t\t"+data[2])
    if menu == '3':
        exit()
