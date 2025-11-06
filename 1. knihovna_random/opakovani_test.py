import random

def random_priklady():
    znamenka = ["+", "-", "*"]
    spravne = 0
    priklad0 = None
    priklad1 = None
    priklad2 = None

    for i in range(3):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        priklad = f"{a} {znamenka[i]} {b}"
        if i == 0:
            priklad0 = priklad
        elif i == 1:
            priklad1 = priklad
        else:
            priklad2 = priklad

    if int(input(f"{priklad0} = ")) == eval(priklad0):
        spravne += 1
    if int(input(f"{priklad1} = ")) == eval(priklad1):
        spravne += 1
    if int(input(f"{priklad2} = ")) == eval(priklad2):
        spravne += 1
    return print(f"Máš {spravne} správně z 3 možných.")

random_priklady()