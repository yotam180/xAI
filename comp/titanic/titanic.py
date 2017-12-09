import csv
import numpy as np
import nLib

def load_csv(fn):
    res = []
    agesum = 0
    agenum = 0
    with open(fn, "rb") as f:
        r = csv.reader(f, delimiter=",", quotechar='"')
        header = next(r)
        for row in r:
            res.append({header[i]: q for i, q in enumerate(row)})
            agesum += float(res[-1]["Age"] or "0")
            if res[-1]["Age"]:
                agenum += 1.0
    return res, agesum / agenum

def parse_csv_entry(e, mean_age):
    x = []
    x.append(float(e["Fare"] or "0") / 100.0)
    x.append(float(e["Age"] or mean_age) / 50.0)
    x.append(e["SibSp"])
    x += [int(e["Embarked"] == i) for i in "SCQ"] + \
         [int(e["S*x".replace("*", "e")] == i) for i in ["male", "female"]] + \
         [int(int(e["Pclass"]) == i) for i in range(3)] + \
         [int(int(e["Parch"]) == i) for i in range(6)] + \
         [int(e["Cabin"][:1] == i) for i in list("ABCDEFT")+[""]]
    return e["PassengerId"], np.array([float(i) for i in x]).reshape(-1, 1), np.array([[int(e["Survived"])], [1-int(e["Survived"])]])
    #return [e["Age"] or mean_age]

c, mean_age = load_csv("titanic.csv")
training_data = []
test_data = []
for i, e in enumerate(c):
    pid, x, y = parse_csv_entry(e, mean_age)
    training_data.append((x, y))

print len(training_data[0][0])
net = nLib.CNN([25, 20, 2], 2)
net.train(training_data, 100, 10, training_data[:100], lambda p, w: np.argmax(p) == np.argmax(w))

c, mean_age = load_csv("test.csv")
test_data = []
for i, e in enumerate(c):
    pid, x, _ = parse_csv_entry(e, mean_age)
    test_data.append((pid, 1 - np.argmax(net.predict(x))))
with open("result.csv", "w") as f:
    for p in test_data:
        f.write(str(int(p[0])))
        f.write(",")
        f.write(str(int(p[1])))
        f.write("\n")