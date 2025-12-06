import os
import getpass
import time
import csv
import matplotlib.pyplot as plt
from collections import Counter

def clear_terminal():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def leave():
    clear_terminal()
    print("See you next time!")
    return

def menu():
    clear_terminal()
    print("[1] Register")
    print("[2] Login")
    print("[3] Quit")
    choice = input("Choose an option [1-3]: ")
    if choice == "1":
        return registrace()
    elif choice == "2":
        return login()
    elif choice == "3":
        return leave()

def registrace():
    should_restart = True
    while should_restart == True:
        should_restart = False
        clear_terminal()
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        if username == "" or password == "":
            print("Please fill in all fields!")
            time.sleep(2)
            should_restart = True
            continue

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
                if username in row[0]:
                    print("The username already exists!")
                    time.sleep(2)
                    should_restart = True
        with open(r'2. prace_se_soubory\PROJEKT_milionar\login_database.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username,password])
            file.close()

    print("The account was successfully created!")
    time.sleep(2)
    return menu()

    
def login():
    clear_terminal()
    input_username = input("Username: ")
    input_password = getpass.getpass("Password: ")
    if input_username == "" or input_password == "":
        print("Please fill in all fields!")
        time.sleep(2)
        return login()
    with open(r'2. prace_se_soubory\PROJEKT_milionar\login_database.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if input_username == row[0] and input_password == row[1]:
                print("Login successful!")
                time.sleep(2)
                return logged_in(input_username)
            
def logged_in(username):
    clear_terminal()
    print(f"Welcome to wanna be a  Cichnallionaire Game, {username}!")
    print("----------------------------")
    print("[1] View the statistics of the questions")
    print("[2] List all winners")
    print("[3] Start the game")
    print("[4] Logout")

    choice = input("Choose an option [1-4]: ")
    if choice == "1":
        graph_statistics(username)
    elif choice == "2":
        winners(username)
    elif choice == "3":
        pass
    elif choice == "4":
        menu()
    else:
        print("Invalid choice, returning to menu.")
        time.sleep(2)
        return logged_in(username)

    time.sleep(2)
    return

def graph_statistics(username):
    clear_terminal()

    question_topic = []
    question_difficulty = []

    with open(r'2. prace_se_soubory\PROJEKT_milionar\quiz_questions.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            question_topic.append(row[2])
            question_difficulty.append(row[1])

    sum_question_topics = Counter(question_topic)
    topics = sum_question_topics.keys()
    counts = sum_question_topics.values()
        
    plt.bar(topics, counts)
    plt.title("Questions count")
    plt.xlabel("Question topics")
    plt.ylabel("Question count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    return logged_in(username)

def winners(username):
    try:
        with open(r'2. prace_se_soubory\PROJEKT_milionar\winners_database.csv', 'r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"User {row[1]} has won {row[0]} times!")
            while True:
                if input("Type 'exit' to return to menu: ").lower() == 'exit':
                    return logged_in(username)
    except FileNotFoundError:
        print("No one has won yet!")
        time.sleep(2)
        return logged_in(username)
    
def add_winner(username):
    try:
        with open(r'2. prace_se_soubory\PROJEKT_milionar\winners_database.csv', 'r', encoding='utf-8', newline='') as file:
            file.close()
    except FileNotFoundError:
        with open(r'2. prace_se_soubory\PROJEKT_milionar\winners_database.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["count", "username"])
            file.close()

    with open(r'2. prace_se_soubory\PROJEKT_milionar\winners_database.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["1", username])

    win_count = 0
    
    with open(r'2. prace_se_soubory\PROJEKT_milionar\winners_database.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == username:
                win_count += 1
    print(f"You have won {win_count} times!")
    time.sleep(2)
    
    return logged_in(username)

menu()