import csv
import matplotlib.pyplot as plt

cesta = (r"2. prace_se_soubory\data\teploty.csv")
with open(cesta, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    roky = []
    teploty = []

    max_teplota = 0
    max_rok = 0
    for radek in reader:
        if (radek["TIME"] == "AVG"):
            teplota = float(radek["TEMPERATURE"])

            teploty.append(teplota)
            roky.append(int(radek["YEAR"]))

            if(teplota > max_teplota):
                max_teplota = teplota
                max_rok = int(radek["YEAR"])

print(f"Nejvyšší průměrná teplota byla v roce {max_rok} a činila {max_teplota} °C")

plt.plot(roky, teploty, color="red")
plt.title("Průměrné roční teploty")
plt.xlabel("Roky")
plt.ylabel("Teplota (°C)")
plt.xticks(roky[::5])  # Zobrazit každý 5. rok pro lepší čitelnost
plt.show()