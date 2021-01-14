import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError

# Init of our Dataframe and all our string list that will be use for url search
list_region = []
list_url_region = []
list_url_jour_mois = []
list_url_annes = []

df = pd.DataFrame(columns=['Date du jour', 'Region', 'Température max', 'Température mini',
                           'Vitesse du vent', 'Precipitation', 'Humidite', 'Visibilité',
                           'Couverture nuageuse', 'Dure du jour'])

url = 'https://www.historique-meteo.net/france'  # Main website url

# Request the page using the url provided
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib.request.urlopen(req).read().decode('utf-8')
# Use it for scraping with BS
soup = BeautifulSoup(webpage, features="html.parser")

sp = soup.find_all('li', attrs={'class': 'item-thumbs col-sm-4 col-md-3 col-xs-6'})
for i in sp:
    region = i.find('a').get('href')
    list_region.append(region)
########## List url region
for a in list_region:
    url_region = "https://www.historique-meteo.net" + a
    list_url_region.append(url_region)
########## List url region / year
for a in list_url_region:
    for y in ["2019/"]:
        url_annes = a + y
        list_url_annes.append(url_annes)
########## List url region / year / month / day
for a in list_url_annes:
    for month in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12"]:
        if month == '01':
            for day in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12", '13', "14", '15', "16",
                        '17', "18", '19', "20", '21', "22", '23', "24", '25', "26", '27', "28", '29', "30", '31']:
                url_x = a + month + '/' + day
                list_url_jour_mois.append(url_x)
        if month == '02':
            for day in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12", '13', "14", '15', "16",
                        '17',
                        "18", '19', "20", '21', "22", '23', "24", '25', "26", '27', "28"]:
                url_x = a + month + '/' + day
                list_url_jour_mois.append(url_x)
        if month == '03':
            for day in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12", '13', "14", '15', "16",
                        '17', "18", '19', "20", '21', "22", '23', "24", '25', "26", '27', "28", '29', "30", '31']:
                url_x = a + month + '/' + day
                url_x = a + y + day + '/' + month
        if month == '04':
            for day in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12", '13', "14", '15', "16",
                        '17',
                        "18", '19', "20", '21', "22", '23', "24", '25', "26", '27', "28", '29', "30"]:
                url_x = a + month + '/' + day
                list_url_jour_mois.append(url_x)
        if month == '05':
            for day in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12", '13', "14", '15', "16",
                        '17', "18", '19', "20", '21', "22", '23', "24", '25', "26", '27', "28", '29', "30", '31']:
                url_x = a + month + '/' + day
                list_url_jour_mois.append(url_x)
        if month == '06':
            for day in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12", '13', "14", '15', "16",
                        '17', "18", '19', "20", '21', "22", '23', "24", '25', "26", '27', "28", '29', "30"]:
                url_x = a + month + '/' + day
                list_url_jour_mois.append(url_x)
        if month == '07':
            for day in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12", '13', "14", '15', "16",
                        '17', "18", '19', "20", '21', "22", '23', "24", '25', "26", '27', "28", '29', "30", '31']:
                url_x = a + month + '/' + day
                list_url_jour_mois.append(url_x)
        if month == '08':
            for day in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12", '13', "14", '15', "16",
                        '17', "18", '19', "20", '21', "22", '23', "24", '25', "26", '27', "28", '29', "30", '31']:
                url_x = a + month + '/' + day
                list_url_jour_mois.append(url_x)
        if month == '09':
            for day in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12", '13', "14", '15', "16",
                        '17', "18", '19', "20", '21', "22", '23', "24", '25', "26", '27', "28", '29', "30"]:
                url_x = a + month + '/' + day
                list_url_jour_mois.append(url_x)
        if month == '10':
            for day in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12", '13', "14", '15', "16",
                        '17',
                        "18", '19', "20", '21', "22", '23', "24", '25', "26", '27', "28", '29', "30", '31']:
                url_x = a + month + '/' + day
                list_url_jour_mois.append(url_x)
        if month == '11':
            for day in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12", '13', "14", '15', "16",
                        '17', "18", '19', "20", '21', "22", '23', "24", '25', "26", '27', "28", '29', "30"]:
                url_x = a + month + '/' + day
                list_url_jour_mois.append(url_x)
        if month == '12':
            for day in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12", '13', "14", '15', "16",
                        '17', "18", '19', "20", '21', "22", '23', "24", '25', "26", '27', "28", '29', "30", '31']:
                url_x = a + month + '/' + day
                list_url_jour_mois.append(url_x)
########## Create Dataframe with values
for url_jour_mois in list_url_jour_mois:
    try:
        req = urllib.request.Request(url_jour_mois, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(webpage, features="html.parser")
        sp_date = soup.find('td', attrs={'class': 'text-center bg-primary'}).text
        sp_date_region = soup.find('h2', attrs={'id': 'meteo'}).text
        sp1 = soup.find_all('td', attrs={'class': 'text-center bg-primary'})
        region = url_jour_mois[url_jour_mois.find("/france/") + len("/france/"):url_jour_mois.find("/2")]
        print(len(sp1))
        print(sp_date_region)
        if len(sp1) == 9:
            ligne = [sp_date, region, sp1[1].text, sp1[2].text, sp1[3].text, sp1[4].text, sp1[5].text, sp1[6].text,
                     sp1[7].text, sp1[8].text]
            new_df = pd.DataFrame([ligne], columns=['Date du jour', 'Region', 'Température max', 'Température mini',
                                                    'Vitesse du vent', 'Precipitation', 'Humidite', 'Visibilité',
                                                    'Couverture nuageuse', 'Dure du jour'])
            df = df.append(new_df)
            df.to_csv('temperature2.csv', index=False)
        elif len(sp1) == 8:
            ligne = [sp_date, region, sp1[1].text, sp1[2].text, sp1[3].text, "Na", sp1[4].text, sp1[5].text,
                     sp1[6].text, sp1[7].text]
            new_df = pd.DataFrame([ligne], columns=['Date du jour', 'Region', 'Température max', 'Température mini',
                                                    'Vitesse du vent', 'Precipitation', 'Humidite', 'Visibilité',
                                                    'Couverture nuageuse', 'Dure du jour'])
            df = df.append(new_df)
            df.to_csv('temperature2.csv', index=False)
    except urllib.error.HTTPError as err:
        print(err.code)
