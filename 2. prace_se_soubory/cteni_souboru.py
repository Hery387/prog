def nacteni_souboru():
    cesta = r"2. prace_se_soubory\data\slova.txt"
    with open(cesta, "r", encoding="utf-8") as file:
        rozlozene_radky = file.readlines()

        pocet_radku = 0
        for radek in rozlozene_radky:
            pocet_radku +=1

        pocet_znaku = sum(len(radek.strip()) for radek in rozlozene_radky)

        pocet_slov = 0
        for radek in rozlozene_radky:
            pocet_slov += len(radek.split())

    return print(f"Radku: {pocet_radku}, Znaku: {pocet_znaku}, Slov: {pocet_slov}")

nacteni_souboru()