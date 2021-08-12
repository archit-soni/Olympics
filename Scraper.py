# m = avail*(tM/TM) + t/T + 1/206
# g = avail*(totalGoldByCountryInThatEvent/totalGoldsGivenAllTimeInThatEvent) + totalMedalsByCountryInThatEvent/TotalMedalsGivenAllTimeInThatEvent + country/totalcountries

import requests
import pandas as pd
import os
from bs4 import BeautifulSoup
import csv


def fill(sub):
    with open("data/"+sub+"/"+title+".csv", "w", newline="", encoding="UTF8") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Nation", "Gold", "Silver", "Bronze", "Total"])
        for row in df.iterrows():
            try:
                nation = row[1]["Nation"].split('(')[0]
            except:
                nation = row[1]["NOC"].split('(')[0]
            gold = row[1]["Gold"]
            silver = row[1]["Silver"]
            bronze = row[1]["Bronze"]
            total = row[1]["Total"]
            csvwriter.writerow([nation, gold, silver, bronze, total])


urls = [
    ("https://en.wikipedia.org/w/index.php?title=Athletics_at_the_Summer_Olympics&oldid=1030136223", 0),
    ("https://en.wikipedia.org/w/index.php?title=Diving_at_the_Summer_Olympics&oldid=998967076", 0),
    ("https://en.wikipedia.org/w/index.php?title=Swimming_at_the_Summer_Olympics&oldid=1032266138", 0),
    ("https://en.wikipedia.org/w/index.php?title=Artistic_swimming_at_the_Summer_Olympics&oldid=1017590568", 0),
    ("https://en.wikipedia.org/w/index.php?title=Water_polo_at_the_Summer_Olympics&oldid=1034191245", 2),
    ("https://en.wikipedia.org/w/index.php?title=Basketball_at_the_Summer_Olympics&oldid=1031280787", 0),
    ("https://en.wikipedia.org/w/index.php?title=Canoeing_at_the_Summer_Olympics&oldid=999197278", 0),
    ("https://en.wikipedia.org/w/index.php?title=Cycling_at_the_Summer_Olympics&oldid=1004219484", 0),
    ("https://en.wikipedia.org/w/index.php?title=Gymnastics_at_the_Summer_Olympics&oldid=1029369183", 3),
    ("https://en.wikipedia.org/w/index.php?title=Volleyball_at_the_Summer_Olympics&oldid=1021101089", 0),
    ("https://en.wikipedia.org/w/index.php?title=Equestrian_at_the_Summer_Olympics&oldid=1026495338", 0),
    ("https://en.wikipedia.org/w/index.php?title=Wrestling_at_the_Summer_Olympics&oldid=1035195105", 0),
    ("https://en.wikipedia.org/w/index.php?title=Archery_at_the_Summer_Olympics&oldid=1033556846", 1),
    ("https://en.wikipedia.org/w/index.php?title=Boxing_at_the_Summer_Olympics&oldid=1033909255", 0),
    ("https://en.wikipedia.org/w/index.php?title=Fencing_at_the_Summer_Olympics&oldid=1029905315", 0),
    ("https://en.wikipedia.org/w/index.php?title=Field_hockey_at_the_Summer_Olympics&oldid=1027596429", 0),
    ("https://en.wikipedia.org/w/index.php?title=Football_at_the_Summer_Olympics&oldid=1034525487", 2),
    ("https://en.wikipedia.org/w/index.php?title=Handball_at_the_Summer_Olympics&oldid=1027197616", 2),
    ("https://en.wikipedia.org/w/index.php?title=Judo_at_the_Summer_Olympics&oldid=1029507560", 0),
    ("https://en.wikipedia.org/w/index.php?title=Modern_pentathlon_at_the_Summer_Olympics&oldid=1028266575", 0),
    ("https://en.wikipedia.org/w/index.php?title=Rowing_at_the_Summer_Olympics&oldid=1025727963", 0),
    ("https://en.wikipedia.org/w/index.php?title=Sailing_at_the_Summer_Olympics&oldid=1029561450", 0),
    ("https://en.wikipedia.org/w/index.php?title=Table_tennis_at_the_Summer_Olympics&oldid=995832669", 0),
    ("https://en.wikipedia.org/w/index.php?title=Taekwondo_at_the_Summer_Olympics&oldid=1032506807", 0),
    ("https://en.wikipedia.org/w/index.php?title=Tennis_at_the_Summer_Olympics&oldid=1031037275", 0),
    ("https://en.wikipedia.org/w/index.php?title=Weightlifting_at_the_Summer_Olympics&oldid=1030399852", 0),
    ("https://en.wikipedia.org/w/index.php?title=Badminton_at_the_Summer_Olympics&oldid=1012341901", 0)
]

urls2020 = [
    "https://en.wikipedia.org/wiki/Diving_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Swimming_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Artistic_swimming_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Water_polo_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Basketball_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Canoeing_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Cycling_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Gymnastics_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Volleyball_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Equestrian_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Archery_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Athletics_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Badminton_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Fencing_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Field_hockey_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Football_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Handball_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Judo_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Modern_pentathlon_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Rowing_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Sailing_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Table_tennis_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Taekwondo_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Tennis_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Weightlifting_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Boxing_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/Wrestling_at_the_2020_Summer_Olympics",
    "https://en.wikipedia.org/wiki/2020_Summer_Olympics_medal_table"

]

if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/historic")
    os.makedirs("data/original")
    os.makedirs("data/predicted")

for url in urls:
    response = requests.get(url[0])
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find(id="firstHeading")
    title = title.string.split(' at')[0]
    body = soup.find_all(
        'table', {"class": "wikitable sortable plainrowheaders jquery-tablesorter"})[url[1]]
    df = pd.read_html(str(body))
    df = pd.DataFrame(df[0])
    fill("historic")

for url in urls2020:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find(id="firstHeading")
    title = title.string.split(' at')[0]
    body = soup.find_all(
        'table', {"class": "wikitable sortable plainrowheaders jquery-tablesorter"})
    df = pd.read_html(str(body))
    df = pd.DataFrame(df[0])
    fill("original")
