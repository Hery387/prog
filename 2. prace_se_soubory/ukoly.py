# UKOL 1

# import random

# def generator_cisel():
#     min = int(input("Zadejte min. hodnotu (0-100): "))
#     max = int(input("Zadejte max. hodnotu (0-100): "))
#     kolik = int(input("Zadejte kolik cisel chcete vygenerovat: "))

    
#     with open(r"2. prace_se_soubory\cislicka.txt", 'a', encoding="utf-8") as file:
#         for i in range(kolik):
#             vygenerovat = random.randint(min, max)
#             file.write(f"{str(vygenerovat)}\n")


# generator_cisel()


############################################

# UKOL 2
# import time
# def chatlogs():

#     with open(r"2. prace_se_soubory\data\chatlog.txt", 'a', encoding='utf-8') as file:
#         print(r"Zadejte '\konec' do jakehokoliv policka pro ukonceni chatu")
#         while True:
#             username = str(input("Zadejte vase uzivatelske jmeno: "))
#             zprava = str(input("Zadejte zpravu: "))
#             if username == r"\konec" or zprava == r"\konec":
#                 break
#             new_format = f"`{time.strftime('%Y-%m-%d %H:%M:%S')} - {username}: {zprava}`"
#             file.write(f"{new_format}\n")
# chatlogs()

############################################

#UKOL 3
import os
import platform
import getpass
def clear_terminal():
    # Check the operating system
    if platform.system() == "Windows":
        os.system('cls')  # Clear terminal for Windows
    else:
        os.system('clear')  # Clear terminal for Unix-like systems

def zalozeni_uctu():
    clear_terminal()
    username = input("Zadejte uzivatelske jmeno: ")
    password = getpass.getpass("Zadejte heslo: ")
    zustatek = 1000
    print("Za registraci jste obdrzel balance: 1000CZK")
    with open(r"2. prace_se_soubory\data\prihlaseni.txt", 'a', encoding='utf-8') as file:
        file.write(f"{username};{password};{zustatek}")

    return prihlaseni()

def prihlaseni():
    temp_username = input("Zadejte uzivatelske jmeno: ")
    temp_password = getpass.getpass("Zadejte heslo: ")

    with open(r"2. prace_se_soubory\data\prihlaseni.txt", 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(';')
            if len(parts) < 3:
                continue
            username, password, zustatek = parts

    #dodelat checknuti


def menu(username, password):
    pass
