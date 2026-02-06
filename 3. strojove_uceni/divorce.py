#zdravim sveho spoluzaka, ktery se ptal na otazky

import csv

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

X = []
Y = []
questions = []
cesta = r"C:\Users\st025672\Downloads\prog\3. strojove_uceni\data\divorce.csv"

    
with open(cesta, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    hlavicka = next(reader)
    for otazka in hlavicka[1:-1]:
        questions.append(otazka)
        print(otazka)

with open(cesta, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for radek in reader:
        q = {}
        for question in questions:
            q[question] = int(radek[question])

        X.append([q[question] for question in questions])
        Y.append(int(radek[hlavicka[-1]]))  # Add the target variable to Y

rows = len(X)
split = round(0.8 * rows)

X_train, X_test, Y_train, Y_test  = train_test_split(
        X, Y,
        test_size=0.2,
        shuffle=True,
        random_state=42)


neuronka = MLPClassifier(
    hidden_layer_sizes=(19, 15, 9),
    activation="identity",
    max_iter=6969,
    verbose=True
)

neuronka.fit(X_train, Y_train)

predikce = neuronka.predict(X_test)
pocet = len(predikce)

spravne = 0
for i in range(pocet):
    if predikce[i] == Y_test[i]:
        spravne += 1

print(f"Poměr správných odpovědí: {round(spravne/pocet*100)}%")
ConfusionMatrixDisplay.from_predictions(
    Y_test, predikce)
plt.show()

