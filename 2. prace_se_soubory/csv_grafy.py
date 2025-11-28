import csv
import matplotlib.pyplot as plt

cesta = (r"2. prace_se_soubory\data\vira_v_cesku.csv")
with open(cesta, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    viry = {}

    for radek in reader:
        if (radek["uzemi_txt"] == "Brno"):
            hodnota = int(radek["hodnota"])
            if radek["vira_txt"] in viry:
                viry[radek["vira_txt"]] += hodnota
            else:
                viry[radek["vira_txt"]] = hodnota
    nejvetsi_vira = max(viry, key=viry.get)
    print(f"Nejvíce případů ve městě Brno je u víry {nejvetsi_vira} s počtem {viry[nejvetsi_vira]} případů.")

    for radek in reader:
        if (radek["uzemi_txt"] == "Brno"):
            if radek["vira_txt"] in viry:
                viry[radek["vira_txt"]] += 1
            else:
                viry[radek["vira_txt"]] = 1