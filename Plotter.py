import matplotlib.pyplot as plt
import numpy as np
import csv

sports = [
    "Archery",
    "Artistic swimming",
    "Athletics",
    "Badminton",
    "Basketball",
    "Boxing",
    "Canoeing",
    "Cycling",
    "Diving",
    "Equestrian",
    "Fencing",
    "Field hockey",
    "Football",
    "Gymnastics",
    "Handball",
    "Judo",
    "Modern pentathlon",
    "Rowing",
    "Sailing",
    "Swimming",
    "Table tennis",
    "Taekwondo",
    "Tennis",
    "Volleyball",
    "Water polo",
    "Weightlifting",
    "Wrestling"
]

i = 1
for event in sports:
    countries = {}
    with open("data/original/"+event+".csv") as csvfile:
        csvreader = csv.reader(csvfile)
        lc = 0
        for row in csvreader:
            if lc == 0:
                lc += 1
            else:
                if row[0] != "Totals":
                    countries[row[0]] = [row[4]]
    with open("data/predicted/"+event+".csv") as csvfile:
        csvreader = csv.reader(csvfile)
        lc = 0
        for row in csvreader:
            if lc == 0:
                lc += 1
            else:
                if row[0] in countries:
                    countries[row[0]].append(row[4])
    x = []
    y = []
    for country in countries:
        if len(countries[country]) == 1:
            countries[country].append(1/206)
        x.append(countries[country][0])
        y.append(countries[country][1])
        print(country, end=" ")
        print(countries[country])
    xx = np.array(x)
    yy = np.array(y)
    yy = yy.astype(np.float)
    xx = xx.astype(np.float)
    plt.title(event)
    plt.subplot(5, 6, i)
    plt.scatter(xx, yy)
    m, b = np.polyfit(xx, yy, 1)
    plt.plot(xx, m*xx+b, color="green")
    plt.xlabel("Actual Medals won by NOC")
    plt.ylabel("Predicted Medal wins for NOC")
    i += 1
plt.show()

for event in sports:
    gold = {}
    silver = {}
    bronze = {}
    names = []
    gTest = []
    sTest = []
    bTest = []
    gTrial = []
    sTrial = []
    bTrial = []
    with open("data/original/"+event+".csv") as csvfile:
        csvreader = csv.reader(csvfile)
        lc = 0
        for row in csvreader:
            if lc == 0:
                lc += 1
            else:
                if row[0] != "Totals":
                    gold[row[0]] = [int(row[1])]
                    silver[row[0]] = [int(row[2])]
                    bronze[row[0]] = [int(row[3])]
    with open("data/predicted/"+event+".csv") as csvfile:
        csvreader = csv.reader(csvfile)
        lc = 0
        for row in csvreader:
            if lc == 0:
                lc += 1
            else:
                if row[0] in gold:
                    gold[row[0]].append(row[1])
                    silver[row[0]].append(row[2])
                    bronze[row[0]].append(row[3])
    for nation in gold:
        if len(gold[nation]) == 1:
            gold[nation].append((1/206))
            silver[nation].append((1/206))
            bronze[nation].append((1/206))
        names.append(nation)
        gTest.append(gold[nation][0])
        sTest.append(silver[nation][0])
        bTest.append(bronze[nation][0])
        gTrial.append(gold[nation][1])
        sTrial.append(silver[nation][1])
        bTrial.append(bronze[nation][1])
    first = np.array(gTest)
    second = np.array(sTest)
    third = np.array(bTest)
    pFirst = np.array(gTrial)
    pSecond = np.array(sTrial)
    pThird = np.array(bTrial)
    pFirst = pFirst.astype(np.float)
    pSecond = pSecond.astype(np.float)
    pThird = pThird.astype(np.float)
    width = 0.40
    x = np.arange(len(gold))
    plt.xticks(x, names, rotation="vertical")
    plt.bar(x-0.2, first, color="gold", width=width,
            edgecolor="black", label="Actual Gold")
    plt.bar(x-0.2, second, bottom=first, color="silver",
            width=width, edgecolor="black", label="Actual Silver")
    plt.bar(x-0.2, third, bottom=first+second,
            color="brown", width=width, edgecolor="black", label="Actual Bronze")
    plt.bar(x+0.2, pFirst, color="gold", width=width,
            alpha=0.5, edgecolor="black", label="Predicted Gold")
    plt.bar(x+0.2, pSecond, bottom=pFirst,
            color="silver", width=width, alpha=0.5, edgecolor="black", label="Predicted Silver")
    plt.bar(x+0.2, pThird, bottom=pFirst+pSecond,
            color="red", width=width, alpha=0.5, edgecolor="black", label="Predicted Bronze")
    plt.xlabel("Nation")
    plt.ylabel("Medals")
    plt.legend(loc="upper right")
    plt.title(event)
    plt.show()
