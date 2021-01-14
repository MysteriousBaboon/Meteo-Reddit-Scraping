# A first scraping project made in a week by the 3 of us for Simplon

## In this project we scrape
- https://www.weathercrave.com/
- https://www.historique-meteo.net/
- https://subredditstats.com/r/france

## The data gathered from the scraping were used to 
1- A Meteo Database

2- Analyse it to understand the relatonships between meteo and social networks

3- Know if today is a good day for communicating on social networks

## How to use it
- Run "pip3 install -r requirements.txt"
- The folder contain the data scrapped from subredditstats. 4 csv containing posts/comments per day for 2019/2020 and the script used for getting it.




## Precisions
You need to add your browserdriver to the path for using the daily meteo scraping script, and you need to change the function webdriver.Firefox in tools to your browser name.