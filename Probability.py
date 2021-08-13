# m = (avail-1)*(tM/TM) + t/T + 1/206

import csv      #read/write csv

#Nation and the medals won
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


sports = [      #Sports in 2020, medals in 2020 in that sport
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

totals = {}         #dictionary where totals[nation] = total predicted medals
og = {}             #medals actually won by countries in 2020

for event in sports:        #iterate sports
    trial = {}              #dictionary to represent objects of Nation in this sport
    with open("data/historic/"+event[0]+".csv") as csvfile:     #read training set
        csvreader = csv.reader(csvfile, delimiter=',')
        lc = 0          #line counter
        for row in csvreader:
            if lc == 0:     #ignore headings
                lc += 1
            else:
                nation = Nation(row[0], row[1], row[2], row[3], row[4])     #create an object for that country in this sport
                trial[nation.getName()] = nation        
                if nation.getName() not in totals:      #initiate country as 0 medals
                    totals[nation.getName()] = 0
    with open("data/predicted/"+event[0]+".csv", "w", newline="") as csvfile:       #write data into predicted csv files
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Nation", "Gold", "Silver", "Bronze", "Total"])     #headings
        for noc in trial:
            row = []        #row to write
            row.append(trial[noc].getName())        #name of country
            gP = trial[noc].getGold()/trial["Totals"].getGold()           # m = (avail-1)*(tM/TM) + t/T + 1/206
            gP = gP*(event[1]-1)
            gP = gP + trial[noc].getTotal()/trial["Totals"].getTotal()
            gP = gP+(1/206)
            row.append(gP)
            sP = trial[noc].getSilver()/trial["Totals"].getSilver()      # m = (avail-1)*(tM/TM) + t/T + 1/206
            sP = sP*(event[1]-1)
            sP = sP + trial[noc].getTotal()/trial["Totals"].getTotal()
            sP = sP+(1/206)
            row.append(sP)
            bP = trial[noc].getBronze()/trial["Totals"].getBronze()      # m = (avail-1)*(tM/TM) + t/T + 1/206
            bP = bP*(event[1]-1)
            if event[0] in ["Wrestling", "Boxing", "Judo", "Taekwondo"]:        #Physical sports hand out 2 bronze medals
                bP = bP*2
            bP = bP + trial[noc].getTotal()/trial["Totals"].getTotal()
            bP = bP+(1/206)
            row.append(bP)
            row.append(gP+sP+bP)
            totals[trial[noc].getName()] += (gP+sP+bP)      #write predicted medals won into dictionary
            csvwriter.writerow(row)
with open("data/original/2020 Summer Olympics medal table.csv") as csvfile:     #read original score
    csvreader = csv.reader(csvfile)
    lc = 0
    for row in csvreader:
        if lc == 0:     #ignore header
            lc += 1
        else:
            if row[0] != "Totals":      #ignore last line
                og[row[0]] = row[4]     #og[country] = total medals won in 2020

for country in og:          #print a table with Nation, Medals Won, Medals Predicted, Unit Variance, Percentage Variance
    print(country, end=",")
    print(og[country], end=",")
    try:
        print(totals[country], end=",")
        print(float(og[country])-float(totals[country]), end=",")
        print((float(og[country])/float(totals[country])-1)*100)
    except:     #Laplace additive smoothing
        print(3/206, end=",")
        print(float(og[country])-3/206, end=",")
        print((float(og[country])/(3/206)-1)*100)
