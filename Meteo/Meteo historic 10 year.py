################## import library #######
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
###
################## Create list  #######
listregion = []
list_url_region = []
list_temp = []
list_url_temp = []
list_month = []
list_month_years = []
###
################## init variable  #######
r1 = 0
r2 = 0
ligne = 0
###
################## Create Dataframe  #######
###
df = pd.DataFrame(columns=['date', 'Temperature moyenne', 'date', 'Temperature moyenne',
                            'date', 'Temperature moyenne', 'date', 'Temperature moyenne',
                            'date', 'Temperature moyenne', 'date', 'Temperature moyenne',
                            'date', 'Temperature moyenne', 'date', 'Temperature moyenne',
                            'date', 'Temperature moyenne', 'date', 'Temperature moyenne',
                            'date', 'Temperature moyenne', 'date', 'Temperature moyenne'])
###
################## Name of url  #######
###
url = 'https://www.historique-meteo.net/france'
################ Objet soup #################
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib.request.urlopen(req).read().decode('utf-8')
# Get page online
soup = BeautifulSoup(webpage, features="html.parser")
sp = soup.find_all('li', attrs={'class': 'item-thumbs col-sm-4 col-md-3 col-xs-6'})

for i in sp:
    region = i.find('a').get('href')
    listregion.append(region)
########## List url region
for a in listregion:
    url_region ="https://www.historique-meteo.net"+a
    list_url_region.append(url_region)
for x_url in list_url_region:
    req = urllib.request.Request(x_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(webpage, features="html.parser")
    sp1 = soup.find('div', attrs={'class': 'list-group'})
    for j in sp1.find_all('a'):
        temp = j.get("href")
        list_temp.append(temp)
for a in list_temp:
    url_temp ="https://www.historique-meteo.net"+a
    list_url_temp.append(url_temp)
#print(list_url_temp)
########## Create Dataframe with values
for temp_url in list_url_temp:
    for month in ['01', "02", '03', "04", '05', "06", '07', "08", '09', "10", '11', "12"]:
        url_x = temp_url + month
        list_month.append(url_x)
for url_monyh in list_month:
    try:
        req = urllib.request.Request(url_monyh, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(webpage, features="html.parser")
        sp = soup.find_all('tbody')
        for j in sp:
            sp = j.find('tr')
            sp = j.find('td', attrs={'class': 'text-center bg-primary'})
            sp = j.find('b').text
            r1 = r1 + 1
            r2 = r2 + 1
            if r1 == 1:
                v1 = sp
            elif r1 == 2:
                v2 = sp
            elif r1 == 3:
                v3 = sp
            elif r1 == 4:
                v4 = sp
            elif r1 == 5:
                v5 = sp
            elif r1 == 6:
                v6 = sp
            elif r1 == 7:
                v7 = sp
            elif r1 == 8:
                v8 = sp
            elif r1 == 9:
                v9 = sp
            elif r1 == 10:
                v10 = sp
            elif r1 == 11:
                v11 = sp
            elif r1 == 12:
                v12 = sp
            elif r1 == 13:
                v13 = sp
            elif r1 == 14:
                v14 = sp
            elif r1 == 15:
                v15 = sp
            elif r1 == 16:
                v16 = sp
            elif r1 == 17:
                v17 = sp
            elif r1 == 18:
                v18 = sp
            elif r1 == 19:
                v19 = sp
            elif r1 == 20:
                v20 = sp
            elif r1 == 21:
                v21 = sp
            elif r1 == 22:
                v22 = sp
            elif r1 == 23:
                v23 = sp
            elif r1 == 24:
                v24 = sp
                list_temp_moy = sp
                ligne = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v14]
                new_df = pd.DataFrame([ligne], columns=['date', 'Temperature moyenne', 'date', 'Temperature moyenne',
                                                        'date', 'Temperature moyenne', 'date', 'Temperature moyenne',
                                                        'date', 'Temperature moyenne', 'date', 'Temperature moyenne',
                                                        'date', 'Temperature moyenne', 'date', 'Temperature moyenne',
                                                        'date', 'Temperature moyenne', 'date', 'Temperature moyenne',
                                                        'date', 'Temperature moyenne', 'date', 'Temperature moyenne'])
                df = df.append(new_df)
                df.to_csv('temp_moy_10ans_new1.csv', index=False)
                if r2 == 288:
                    r1 = 2
                    r2 = 2
                else:
                    r1 = 0
                print(ligne)
                print(r2)
                #print(list_temp_moy)
            else:
                v1 = sp
                #print(list_years)
            #print(list_month_years)
    except urllib.error.HTTPError as err:
        print(err.code)
######################   calcul d'indice########################*
"""HI = T – [(0,55- 0,0055 . U) . (T- 14,5)]
1 thi < 0.1             trop froid
2  thi < 0.1 et <3.3        tres froid
3  thi >= 3.3 et <6.4    froid
4  thi >= 6.4 et < 9.6      frais
5  thi >= 9.6 et < 22.3        confortatbe
6  thi >= 22.3 et <25.4         chaud
7  thi >= 25.4  et <28.8        tres chaud
8 thi >= 28.8                  trop chaud

nuage ====> indice * (100% + 20 * % nuage)
print(p)
"""
##################################################################
"""
import math
v = 15
t = 12
u = 15
wci = 13.12 + 0.6215*t - 11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
#print("The wind chill index is", int(round(wci, 0)))

thi = wci - ((0.55 - (0.0055 * u) * (wci - 14.5)))
#print(thi)

nuage = 7
t_moy = 20
t_ecart = t - t_moy
wci = 13.12 + 0.6215*t_ecart - 11.37*math.pow(v, 0.16) + 0.3965*t_ecart*math.pow(v, 0.16)
print("The wind chill index is", int(round(wci, 0)))

thi = wci - ((0.55 - (0.0055 * u) * (wci - 14.5)))
print(thi)
indice = (thi + 20 ) * (100 + (20 * (100 - nuage) / 100)) / 100
print(indice)
"""""