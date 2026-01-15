import csv
from sklearn.neural_network import MLPClassifier

x = []
y = []

cesta = r"C:\Users\st025672\Downloads\prog\3. strojove_uceni\data\heart.csv"
with open(cesta, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    next(reader)
    for row in reader:
        y.append(int(row["heart_disease"]))

        age = int(row["age"])
        trestbps = int(row["trestbps"])
        chol = int(row["chol"])
        if row["sex"] == "1":
            gender = 100
        else:
            gender = 30
        thalach = int(row["thalach"])
        cp = int(row["cp"])
        fbs = int(row["fbs"])
        restecg = int(row["restecg"])
        exang = int(row["exang"])
        oldpeak = float(row["oldpeak"])
        slope = int(row["slope"])
        ca = int(row["ca"])
        thal = int(row["thal"])

        x.append([age, trestbps, chol, gender, thalach, cp, fbs, restecg, exang, oldpeak, slope, ca, thal])

x_train = x[:round(len(x)*0.8)]
y_train = y[:round(len(y)*0.8)]

x_test = x[round(len(x)*0.8):]
y_test = y[round(len(y)*0.8):]

sit = MLPClassifier(
    hidden_layer_sizes=(16, 9, 8),
    activation='relu',
    max_iter=1000,
    random_state=69
)

sit.fit(x,y)

predikce = sit.predict(x_test)
pocet = len(predikce)

print(sit.predict(x_test))

spravne = 0
for i in range(len(predikce)):
    if predikce[i] == y_test[i]:
        spravne += 1

print(f"Pomer spravnych predikci: {spravne}/{pocet} = {spravne/pocet:.2%}")