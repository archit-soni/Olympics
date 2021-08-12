# m = avail*(tM/TM) + t/T + 1/206

import csv
import matplotlib.pyplot as plt


class Nation:
    def __init__(self, name, gold, silver, bronze, total):
        self.gold = int(gold)
        self.silver = int(silver)
        self.bronze = int(bronze)
        self.total = int(total)
        self.name = name

    def getGold(self):
        return self.gold

    def getSilver(self):
        return self.silver

    def getBronze(self):
        return self.bronze

    def getTotal(self):
        return self.total

    def getName(self):
        return self.name


sports = [
    ("Archery", 5),
    ("Artistic swimming", 2),
    ("Athletics", 48),
    ("Badminton", 5),
    ("Basketball", 4),
    ("Boxing", 13),
    ("Canoeing", 16),
    ("Cycling", 22),
    ("Diving", 8),
    ("Equestrian", 6),
    ("Fencing", 12),
    ("Field hockey", 2),
    ("Football", 2),
    ("Gymnastics", 18),
    ("Handball", 2),
    ("Judo", 15),
    ("Modern pentathlon", 2),
    ("Rowing", 14),
    ("Sailing", 10),
    ("Swimming", 37),
    ("Table tennis", 5),
    ("Taekwondo", 8),
    ("Tennis", 5),
    ("Volleyball", 4),
    ("Water polo", 2),
    ("Weightlifting", 14),
    ("Wrestling", 18)
]

totals = {}
og = {}

for event in sports:
    trial = {}
    with open("data/historic/"+event[0]+".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        lc = 0
        for row in csvreader:
            if lc == 0:
                lc += 1
            else:
                nation = Nation(row[0], row[1], row[2], row[3], row[4])
                trial[nation.getName()] = nation
                if nation.getName() not in totals:
                    totals[nation.getName()] = 0
    with open("data/predicted/"+event[0]+".csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Nation", "Gold", "Silver", "Bronze", "Total"])
        for noc in trial:
            row = []
            row.append(trial[noc].getName())
            gP = trial[noc].getGold()/trial["Totals"].getGold()
            gP = gP*(event[1]-1)
            gP = gP + trial[noc].getTotal()/trial["Totals"].getTotal()
            gP = gP+(1/206)
            row.append(gP)
            sP = trial[noc].getSilver()/trial["Totals"].getSilver()
            sP = sP*(event[1]-1)
            sP = sP + trial[noc].getTotal()/trial["Totals"].getTotal()
            sP = sP+(1/206)
            row.append(sP)
            bP = trial[noc].getBronze()/trial["Totals"].getBronze()
            bP = bP*(event[1]-1)
            if event[0] in ["Wrestling", "Boxing", "Judo", "Taekwondo"]:
                bP = bP*2
            bP = bP + trial[noc].getTotal()/trial["Totals"].getTotal()
            bP = bP+(1/206)
            row.append(bP)
            row.append(gP+sP+bP)
            totals[trial[noc].getName()] += (gP+sP+bP)
            csvwriter.writerow(row)
with open("data/original/2020 Summer Olympics medal table.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    lc = 0
    for row in csvreader:
        if lc == 0:
            lc += 1
        else:
            if row[0] != "Totals":
                og[row[0]] = row[4]

for country in og:
    print(country, end=",")
    print(og[country], end=",")
    try:
        print(totals[country], end=",")
        print(float(og[country])-float(totals[country]), end=",")
        print((float(og[country])/float(totals[country])-1)*100)
    except:
        print(3/206, end=",")
        print(float(og[country])-3/206, end=",")
        print((float(og[country])/(3/206)-1)*100)
