import os
import getpass
import time
import csv
import matplotlib.pyplot as plt
from collections import Counter
import random

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
    print("Your username or password is wrong!")
    time.sleep(2)
    return menu()
            
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
        game(username)
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
    question_easy = 0
    question_medium = 0
    question_hard = 0

    with open(r'2. prace_se_soubory\PROJEKT_milionar\quiz_questions.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            question_topic.append(row[2])
            if row[1] == "easy":
                question_easy += 1
            elif row[1] == "medium":
                question_medium += 1
            elif row[1] == "hard":
                question_hard += 1


    plt.figure(figsize=(12, 5))

#Graph depending on topics
    sum_question_topics = Counter(question_topic)
    topics = sum_question_topics.keys()
    counts = sum_question_topics.values()
        
    plt.subplot(1, 2, 1)
    plt.bar(topics, counts)
    plt.title("Questions Count by Topic")
    plt.xlabel("Question Topics")
    plt.ylabel("Question Count")
    plt.xticks(rotation=45, ha="right")

#Graph depending on difficulty

    plt.subplot(1, 2, 2)
    plt.bar(["Easy", "Medium", "Hard"],[question_easy, question_medium, question_hard])
    plt.title("Difficulty count")
    plt.xlabel("Difficulties")
    plt.ylabel("Difficulty count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    return logged_in(username)

def winners(username):
    clear_terminal()
    wins = {}
    try:
        with open(r'2. prace_se_soubory\PROJEKT_milionar\winners_database.csv', 'r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[1] not in wins:
                    wins[row[1]] = 1
                else:
                    wins[row[1]] += 1

        for player in wins:
            print(f"User {player} has won {wins[player]} times!")
        
        print()
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
    clear_terminal()
    print(f"You have won {win_count} times!")
    time.sleep(3)
    
    return logged_in(username)

def game(username):
    easy_questions = {}
    medium_questions = {}
    hard_questions = {}
    playing = True
    should_win = False
    question_count = 0

    clear_terminal()
    print(f"Welcome, {username} to the Cichna wants to be a millionaire!")
    print()
    print("15 questions will be presented to you. For each one, you have to answer if the question is true (t) or false (f).")
    print("There are 3 difficulties. They are easy, medium and hard. Each difficulty has 5 questions total.")
    print("If you get one question wrong, you're out!")
    print("Goodluck!")
    print()
    while True:
        if input("Type [y] to start:\n").lower() == "y":
            break

    with open(r'2. prace_se_soubory\PROJEKT_milionar\quiz_questions.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1] == "easy":
                easy_questions[row[3]] = row[4]
            elif row[1] == "medium":
                medium_questions[row[3]] = row[4]
            elif row[1] == "hard":
                hard_questions[row[3]] = row[4]
    
    while playing:
        question_count += 1
        clear_terminal()
        print(f"Question no. {question_count}")
        print("----------------------------")
        if question_count <= 5:
            question, answer = random.choice(list(easy_questions.items()))
        elif question_count > 5 and question_count <= 10:
            question, answer = random.choice(list(medium_questions.items()))
        elif question_count > 10:
            question, answer = random.choice(list(hard_questions.items()))
        print(question)
        print()
        print(f"dbg cheat: {question},{answer}")
        choice = input("True [t]/False [f]: ")[0].lower()
        if choice == "t":
            choice = "True"
        else:
            choice = "False"
        if choice == answer:
            clear_terminal()
            print("Correct!")
            time.sleep(2)
            pass
        else:
            clear_terminal()
            playing = False
            print("You lose! Better luck next time.")
            time.sleep(2)
        if question_count == 15:
            should_win = True
            break
    
    if should_win == True:
        clear_terminal()
        print("Congrats! You just became a millionaire!")
        print("Adding your name to the winner's list...")
        time.sleep(2)
        print()
        while True:
            if input("Type [y] to continue:\n").lower() == "y":
                break
        return add_winner(username)
    else:
        return logged_in(username)
            

            

menu()