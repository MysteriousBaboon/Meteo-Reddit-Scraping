from bs4 import BeautifulSoup

from datetime import date

import pandas as pd
import time

from selenium import webdriver


driver = webdriver.Firefox()  # Specify that the Browser will be Firefox
driver.get('https://subredditstats.com/r/france')
time.sleep(5)
soup = BeautifulSoup(driver.page_source, "lxml")
# Find all values and their corresponding name
comments = soup.find_all("td", attrs={"class": "property-name"})
values = soup.find_all("td", attrs={"class": "property-value"})

data = {}
# Create a relation Value and their name
for i in range(0, len(comments)):
    data[comments[i].text] = values[i].text

# Get the Date
today = date.today()
year = today.year
month = today.month
day = today.day

line = [values[1].text, values[2].text, year, month, day]

# Check if the data are already created if not create it
try:
    df = pd.read_csv('data.csv')
except:
    pd.DataFrame(columns=[comments[1].text, comments[2].text, 'year', 'month', "day"]).to_csv('data.csv', index=False)
    df = pd.read_csv('data.csv')

new_df = pd.DataFrame([line], columns=[comments[1].text, comments[2].text, 'year', 'month', "day"])
df = df.append(new_df)
df.to_csv('data.csv', index=False)

driver.quit()
