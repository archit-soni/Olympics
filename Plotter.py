#Plot Graphs comparing Predicted/Actual values

import matplotlib.pyplot as plt     #to plot graphs
import numpy as np          #arrays
import csv          #read csv

sports = [          #sports in 2020
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

for event in sports:        #iterate sports
    countries = {}          #contries[country] = [actual medals, predicted medals]
    with open("data/original/"+event+".csv") as csvfile:    #read test set
        csvreader = csv.reader(csvfile)
        lc = 0      #line counter
        for row in csvreader:
            if lc == 0:     #ignore headings
                lc += 1
            else:
                if row[0] != "Totals":      #ignore last line
                    countries[row[0]] = [row[4]]        #actual medals
    with open("data/predicted/"+event+".csv") as csvfile:       #read predictions
        csvreader = csv.reader(csvfile)     
        lc = 0
        for row in csvreader:
            if lc == 0:
                lc += 1
            else:
                if row[0] in countries:
                    countries[row[0]].append(row[4])    #predicted medals
    x = []      #x axis
    y = []      #y axis
    for country in countries:
        if len(countries[country]) == 1:    #additive Laplace smoothing at necessary places
            countries[country].append(1/206)
        x.append(countries[country][0])     #actual medals on x axis
        y.append(countries[country][1])     #actual medals on y axis
        print(country, end=" ")
        print(countries[country])
    xx = np.array(x)        #numpy array
    yy = np.array(y)        #numpy array
    yy = yy.astype(np.float)        #read as type float
    xx = xx.astype(np.float)        #read as type float
    plt.title(event)        #Title of Scatter Plot is sport name
    plt.scatter(xx, yy)     #Plot Scatter
    m, b = np.polyfit(xx, yy, 1)    #Regression line
    plt.plot(xx, m*xx+b, color="green")     #Plot regression line
    plt.xlabel("Actual Medals won by NOC")      #x axis label
    plt.ylabel("Predicted Medal wins for NOC")  #y axis label
    plt.show()      #Display Scatter Plot

    
#Plot double-clustered triple-stacked bar graph
for event in sports:
    gold = {}       #gold[nation] = [actual, predicted]
    silver = {}     #silver[nation] = [actual, predicted]
    bronze = {}     #bronze[nation] = [actual, predicted]
    names = []      #x-axis
    gTest = []      #array of gold medals won by nations in order of their x-axis location
    sTest = []      #array of silver medals won by nations in order of their x-axis location
    bTest = []      #array of bronze medals won by nations in order of their x-axis location
    gTrial = []     #array of gold medals predicted for nations in order of their x-axis location
    sTrial = []     #array of silver medals predicted for nations in order of their x-axis location
    bTrial = []     #array of bronze medals predicted for nations in order of their x-axis location
    with open("data/original/"+event+".csv") as csvfile:    #read test set
        csvreader = csv.reader(csvfile)
        lc = 0
        for row in csvreader:
            if lc == 0:     #ignore header
                lc += 1
            else:
                if row[0] != "Totals":      #ignore last line
                    gold[row[0]] = [int(row[1])]        #actual gold won in that sport by nation
                    silver[row[0]] = [int(row[2])]      #actual silver won
                    bronze[row[0]] = [int(row[3])]      #actual bronze won
    with open("data/predicted/"+event+".csv") as csvfile:       #read training set predictions
        csvreader = csv.reader(csvfile)
        lc = 0
        for row in csvreader:
            if lc == 0:     #ignore header
                lc += 1
            else:
                if row[0] in gold:
                    gold[row[0]].append(row[1])     #predicted gold for nation in that sport
                    silver[row[0]].append(row[2])       #predicted silver for nation in that sport
                    bronze[row[0]].append(row[3])       #predicted bronze for nation in that sport
    for nation in gold:
        if len(gold[nation]) == 1:      #Additive Laplace smoothing
            gold[nation].append((1/206))
            silver[nation].append((1/206))
            bronze[nation].append((1/206))
        names.append(nation)        #x-axis labels
        gTest.append(gold[nation][0])           #actual gold added to gTest
        sTest.append(silver[nation][0])         #actual silver added to sTest
        bTest.append(bronze[nation][0])         #actual bronze added to bTest
        gTrial.append(gold[nation][1])          #predicted gold added to gTrial
        sTrial.append(silver[nation][1])        #predicted silver added to sTrial
        bTrial.append(bronze[nation][1])        #predicted bronze added to bTrial
    #numpy arrays
    first = np.array(gTest)
    second = np.array(sTest)
    third = np.array(bTest)
    pFirst = np.array(gTrial)
    pSecond = np.array(sTrial)
    pThird = np.array(bTrial)
    #read as float
    pFirst = pFirst.astype(np.float)
    pSecond = pSecond.astype(np.float)
    pThird = pThird.astype(np.float)
    width = 0.40
    x = np.arange(len(gold))    #evenly spaced out
    plt.xticks(x, names, rotation="vertical")   #display name vertically rotated on x-axis
    plt.bar(x-0.2, first, color="gold", width=width,
            edgecolor="black", label="Actual Gold")     #plot actual gold
    plt.bar(x-0.2, second, bottom=first, color="silver",
            width=width, edgecolor="black", label="Actual Silver")      #plot actual silver on top of actual gold
    plt.bar(x-0.2, third, bottom=first+second,
            color="brown", width=width, edgecolor="black", label="Actual Bronze")       #plot actual bronze on top of actual siler
    plt.bar(x+0.2, pFirst, color="gold", width=width,
            alpha=0.5, edgecolor="black", label="Predicted Gold")       #plot predicted gold next to actual gold
    plt.bar(x+0.2, pSecond, bottom=pFirst,
            color="silver", width=width, alpha=0.5, edgecolor="black", label="Predicted Silver")    #plot predicted silver on top of predicted gold
    plt.bar(x+0.2, pThird, bottom=pFirst+pSecond,
            color="red", width=width, alpha=0.5, edgecolor="black", label="Predicted Bronze")   #plot predicted bronze on top of predicted silver
    plt.xlabel("Nation")
    plt.ylabel("Medals")
    plt.legend(loc="upper right")       #legend
    plt.title(event)        #title is name of sport
    plt.show()      #display graphs
