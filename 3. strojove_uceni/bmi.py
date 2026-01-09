import csv

from sklearn.neural_network import MLPClassifier

x = []
y = []

cesta = r"C:\Users\st025672\Downloads\prog\3. strojove_uceni\data\bmi.csv"
with open(cesta, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        y.append(int(row["Index"]))

        if row["Gender"] == "Male":
            gender = 100
        else:
            gender = 30

        height = int(row["Height"])
        weight = int(row["Weight"])

        x.append([gender, height, weight])

x_train = x[:round(len(x)*0.8)]
y_train = y[:round(len(y)*0.8)]

x_test = x[round(len(x)*0.8):]
y_test = y[round(len(y)*0.8):]

sit = MLPClassifier(
    hidden_layer_sizes=(10,8,6),
    activation="relu",
    max_iter=1000
)

sit.fit(x, y)

predikce = sit.predict(x_test)
pocet = len(predikce)

print(sit.predict(x_test))

spravne = 0
for i in range(len(predikce)):
    if predikce[i] == y_test[i]:
        spravne += 1

print(f"Pomer spravnych predikci: {spravne}/{pocet} = {spravne/pocet:.2%}")