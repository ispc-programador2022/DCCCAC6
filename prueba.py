#instalar modulos => selenium (con chromeDriver), lxml, requests, beautifulsoup4 y pandas

#region variables
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import os
clear = lambda: os.system('cls')

options = ChromeOptions()
options.headless = True
driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe", options=options)

img_climate_icons_img_src = "/sites/all/themes/smn/img/weather-icons/" # + smn_climate_icons.prop + ".png"
url_pronostico = "https://www.smn.gob.ar/pronostico"
img_climate_icons_ul_id = "lista_matriz"

driver.get(url_pronostico)
clear()
print("")
#endregion
#

#region def()
def get_Url(url):
    # requiere la pág para escrapear
    try:
        return requests.get(url)
    except Exception as e:
        print("error en la request")
        print(e)
        print("\n")
#

def get_divs( ret, link, typeOfDiv1, attrKey1, attrkValue1, typeOfDiv2 = 0, get = False, many = False, attrKey2 = 0, attrkValue2 = 0 ):
    #recupera la división especifica para trabajar y retorna Href of text
        
    if get == True:
        webPage = get_Url(link)
        soup = bs(webPage.text, "lxml")
    else:
        soup = bs(link, "lxml")

    if many:
        divisions = soup.find_all(typeOfDiv1, attrs = {attrKey1 : attrkValue1})
        #print(divisions)
        if typeOfDiv2 != 0 :
            if attrKey2 != 0:
                divisions = soup.find_all(typeOfDiv2, attrs = {attrKey2 : attrkValue2})
            else:
                divisions = soup.find_all(typeOfDiv2)
        
        if ret == "href":
            return [div.a.get("href") for div in divisions]
        elif ret == "text":
            return [div.a.get_text() for div in divisions]
    else:
        if typeOfDiv2 != 0:
            divisions = soup.find(typeOfDiv1, attrs = {attrKey1 : attrkValue1}).find_all(typeOfDiv2)
            if ret == "href":
                return [div.a.get("href") for div in divisions]
            elif ret == "text":
                return [div.a.get_text() for div in divisions]
            elif ret == "table":
                table_division = []
                counter = 0
                for div in divisions:
                    if counter > 0:
                        div_list = []
                        data_day = div.find("th", attrs = {"id":"titulo"})
                        data_max = div.find("th", attrs = {"id":"maximas"})
                        div_list.append(data_day.get_text())
                        div_list.append(data_max.get_text())
                        table_division.append(div_list)
                    counter += 1
                return table_division
        else:
            return soup.find(typeOfDiv1, attrs = {attrKey1 : attrkValue1})
#

#endregion
#

#region scrap_init
list_table_clima = get_divs("table", driver.page_source, "ul", "id", "lista_matriz", "li")
print(list_table_clima)