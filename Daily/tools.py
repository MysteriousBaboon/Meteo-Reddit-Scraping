from datetime import datetime


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Firefox()  # Specify that the Browser will be Firefox

links = {"country": "", "region": "", "department": ""}
current_position = {"country": "France", "region": "", "department": "", "city":""}

df = pd.DataFrame(columns=['Date', 'Hour', 'Country', 'Region', 'Department', 'City', 'Temperature',
                           'Felt Temp', 'Wind', 'Sky'])


def init():
    driver.implicitly_wait(5)
    # Load a dummy page then add the cookie popup and load the right page
    driver.get('https://www.weathercrave.com/404')
    popup = {'name': 'cmp_v2_uuid', 'value': 'cmp16104008612180.9832955355586168', 'path': '/',
             'domain': '.weathercrave.com', 'secure': False, 'httpOnly': False, 'expiry': 1641850461,
             'sameSite': 'None'}
    driver.add_cookie(popup)
    driver.get('https://www.weathercrave.com/weather-forecast-world/country-63/weather-forecast-france-today')


def clear_map(clear_cities=True):
    if clear_cities:
        element = driver.find_element_by_css_selector("div[class='leaflet-pane leaflet-marker-pane']")
        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)
        regions = driver.find_element_by_tag_name("g").find_elements_by_tag_name("path")
        return regions
    else:
        regions = driver.find_elements_by_css_selector('img.leaflet-marker-icon')
        return regions



def go_back(scale="country"):
    if scale == "country":
        driver.get(links["country"])
    elif scale == "region":
        driver.get(links["region"])
    elif scale == "department":
        driver.get(links["department"])


def scrape_page():
        global df  # To access our Global Scope df

        soup = BeautifulSoup(driver.page_source, "lxml")
        current_position["city"] = soup.find("h1").find_all("div")[1].text

        data = soup.find("div", {"class": "data"}).find_all("div", {"class": "cell"})
        temp = data[1].find_all("div")[0].text
        felt_temp = data[1].find_all("div")[1].text
        sky = data[0].find('img')['alt']

        spans = data[2].find_all('span')
        wind = spans[0].text + spans[1].text

        now = datetime.now()  # current date and time
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M")
        new_row = pd.DataFrame([[date, time, current_position["country"], current_position["region"],
                                current_position["department"], current_position["city"], temp, felt_temp, wind, sky]],
                               columns=['Date', 'Hour', 'Country', 'Region', 'Department', 'City', 'Temperature',
                                        'Felt Temp', 'Wind', 'Sky'])
        df = df.append(new_row)


