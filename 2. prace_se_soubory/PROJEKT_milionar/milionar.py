import os
import getpass
import time
import csv

def clear_terminal():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def registrace():
    should_restart = True
    while should_restart == True:
        should_restart = False
        clear_terminal()
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        try:
            with open(r'2. prace_se_soubory\PROJEKT_milionar\login_database.csv', 'r', encoding='utf-8', newline='') as file:
                file.close()
        except FileNotFoundError:
            with open(r'2. prace_se_soubory\PROJEKT_milionar\login_database.csv', 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["username", "password"])
                file.close()

        with open(r'2. prace_se_soubory\PROJEKT_milionar\login_database.csv', 'r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file)

            for row in reader:
                if username in row:
                    print("The username already exists!")
                    time.sleep(2)
                    should_restart = True
                else:
                    with open(r'2. prace_se_soubory\PROJEKT_milionar\login_database.csv', 'a', encoding='utf-8', newline='') as psanicko:
                        writer = csv.writer(psanicko)
                        writer.writerow([username,password])
            file.close()

    print("The account was successfully created!")
    time.sleep(2)

registrace()