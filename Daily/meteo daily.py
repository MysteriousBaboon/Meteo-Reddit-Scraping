import time
import random
import sys

import tools

from selenium import webdriver

tools.links["country"] = 'https://www.weathercrave.com/weather-forecast-world/country-63/weather-forecast-france-today'
tools.init()


def city_scan():
    city_indice = 1
    cities = tools.clear_map(False)
    tools.links["department"] = tools.driver.current_url
    tools.current_position["department"] = tools.driver.find_element_by_tag_name("h1").find_elements_by_tag_name("div")[1].text

    while city_indice < len(cities):
        time.sleep(random.uniform(3, 6))
        try:
            tools.driver.execute_script("arguments[0].scrollIntoView();", cities[city_indice])
            time.sleep(random.uniform(1.5, 4.0))
            print("1")
            webdriver.ActionChains(tools.driver).move_to_element(cities[city_indice]).click(cities[city_indice]).perform()

            time.sleep(random.uniform(1.5, 4.0)+2)
            tools.scrape_page()
            print("2")
            tools.go_back("department")
            time.sleep(random.uniform(1.5, 4.0))
            cities = tools.clear_map(clear_cities=False)

            city_indice += 1

        except:
            e = sys.exc_info()[0]
            tools.df.to_csv('unfinished.csv', index=False)
            print(f"{e} City")
            continue




def region_scan():
    department_indice = 1
    departments = tools.clear_map()
    tools.links["region"] = tools.driver.current_url
    tools.current_position["region"] = tools.driver.find_element_by_tag_name("h1").find_elements_by_tag_name("div")[1].text

    while department_indice < len(departments):
        time.sleep(2)
        try:
            tools.driver.execute_script("arguments[0].scrollIntoView();", departments[department_indice])
            time.sleep(random.uniform(1.5, 4.0))

            webdriver.ActionChains(tools.driver).move_to_element(departments[department_indice]).click(
                departments[department_indice]).perform()
            time.sleep(random.uniform(1.5, 4.0))
            city_scan()
            tools.go_back("region")
            time.sleep(random.uniform(1.5, 4.0))
            departments = tools.clear_map(clear_cities=True)

            department_indice += 1
        except:
            e = sys.exc_info()[0]
            print(f"{e} Region")
            continue



def country_scan():
    region_indice = 1
    regions = tools.clear_map()
    while region_indice < len(regions):
        time.sleep(2)
        try:
            tools.driver.execute_script("arguments[0].scrollIntoView();", regions[region_indice])
            time.sleep(random.uniform(1.5, 4.0))

            webdriver.ActionChains(tools.driver).move_to_element(regions[region_indice]).click(
                regions[region_indice]).perform()
            time.sleep(random.uniform(1.5, 4.0))
            region_scan()
            tools.go_back()
            time.sleep(random.uniform(1.5, 4.0))
            regions = tools.clear_map(clear_cities=True)
            region_indice += 1

        except:
            e = sys.exc_info()[0]
            print(e)
            continue

time.sleep(2)
country_scan()

tools.df.to_csv('Jan12.csv',index=False)