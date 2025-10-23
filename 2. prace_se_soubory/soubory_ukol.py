import random
def citat_dne():
    emoji = ["🌺", "🌼", "🌞", "🐻", "❤️‍", "🔥"]
    pocet_emoji = random.randint(3,5)
    
    cesta_citat = r'2. prace_se_soubory\data\citaty.txt'
    with open(cesta_citat, 'r') as file:
        text = file.read()
