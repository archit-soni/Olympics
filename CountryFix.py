# m = avail*(tM/TM) + t/T + 1/206

import csv


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

for event in sports:
    trial = {}
    with open("data/original/"+event[0]+".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        lc = 0
        for row in csvreader:
            if lc == 0:
                lc += 1
            else:
                nation = Nation(row[0], row[1], row[2], row[3], row[4])
                trial[nation.getName()] = nation
    with open("data/original/"+event[0]+".csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Nation", "Gold", "Silver", "Bronze", "Total"])
        for noc in trial:
            row = []
            if trial[noc].getName() == "Japan*":
                row = ["Japan", trial[noc].getGold(), trial[noc].getSilver(
                ), trial[noc].getBronze(), trial[noc].getTotal()]
            elif trial[noc].getName() == "ROC":
                row = ["Russia", trial[noc].getGold(), trial[noc].getSilver(
                ), trial[noc].getBronze(), trial[noc].getTotal()]
            else:
                row = [trial[noc].getName(), trial[noc].getGold(), trial[noc].getSilver(
                ), trial[noc].getBronze(), trial[noc].getTotal()]
            csvwriter.writerow(row)

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
    with open("data/historic/"+event[0]+".csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Nation", "Gold", "Silver", "Bronze", "Total"])
        for noc in trial:
            row = []
            if trial[noc].getName() == "Germany":
                try:
                    gold = trial[noc].getGold() + \
                        trial["East Germany"].getGold()
                    silver = trial[noc].getSilver(
                    ) + trial["East Germany"].getSilver()
                    bronze = trial[noc].getBronze(
                    ) + trial["East Germany"].getBronze()
                except:
                    gold = trial[noc].getGold() + 0
                    silver = trial[noc].getSilver() + 0
                    bronze = trial[noc].getBronze() + 0
                try:
                    gold = gold + trial["West Germany"].getGold()
                    silver = silver + trial["West Germany"].getSilver()
                    bronze = bronze + trial["West Germany"].getBronze()
                except:
                    gold = gold + 0
                    silver = silver + 0
                    bronze = bronze + 0
                try:
                    gold = gold + trial["United Team of Germany"].getGold()
                    silver = silver + \
                        trial["United Team of Germany"].getSilver()
                    bronze = bronze + \
                        trial["United Team of Germany"].getBronze()
                except:
                    gold = gold + 0
                    silver = silver + 0
                    bronze = bronze + 0
                row = ["Germany", gold, silver, bronze, (gold+silver+bronze)]
                csvwriter.writerow(row)
            if trial[noc].getName() == "Russia":
                try:
                    gold = trial[noc].getGold() + \
                        trial["Soviet Union"].getGold()
                    silver = trial[noc].getSilver(
                    ) + trial["Soviet Union"].getSilver()
                    bronze = trial[noc].getBronze(
                    ) + trial["Soviet Union"].getBronze()
                except:
                    gold = trial[noc].getGold() + 0
                    silver = trial[noc].getSilver() + 0
                    bronze = trial[noc].getBronze() + 0
                try:
                    gold = gold + trial["Unified Team"].getGold()
                    silver = silver + trial["Unified Team"].getSilver()
                    bronze = bronze + trial["Unified Team"].getBronze()
                except:
                    gold = gold + 0
                    silver = silver + 0
                    bronze = bronze + 0
                row = ["Russia", gold, silver, bronze, (gold+silver+bronze)]
                csvwriter.writerow(row)
            if trial[noc].getName() == "Czech Republic":
                try:
                    gold = trial[noc].getGold() + \
                        trial["Czechoslovakia"].getGold()
                    silver = trial[noc].getSilver(
                    ) + trial["Czechoslovakia"].getSilver()
                    bronze = trial[noc].getBronze(
                    ) + trial["Czechoslovakia"].getBronze()
                except:
                    gold = trial[noc].getGold() + 0
                    silver = trial[noc].getSilver() + 0
                    bronze = trial[noc].getBronze() + 0
                row = ["Czech Republic", gold, silver,
                       bronze, (gold+silver+bronze)]
                csvwriter.writerow(row)
            if trial[noc].getName() not in ["West Germany", "East Germany", "Unified Team", "United Team of Germany", "Russia", "Soviet Union", "Czech Republic", "Czechoslovakia", "Germany"]:
                row = [trial[noc].getName(), trial[noc].getGold(), trial[noc].getSilver(
                ), trial[noc].getBronze(), trial[noc].getTotal()]
                csvwriter.writerow(row)

for country in trial:
    print(trial[country].getName(), end=" ")
    print(trial[country].getGold(), end=" ")
    print(trial[country].getSilver(), end=" ")
    print(trial[country].getBronze(), end=" ")
    print(trial[country].getTotal())
