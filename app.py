#instalar modulos => selenium (con chromeDriver), lxml, requests, beautifulsoup4 y pandas

#region variables
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import os
from datetime import date
from datetime import datetime
clear = lambda: os.system('cls')

options = ChromeOptions()
options.headless = True
driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe", options=options)

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

def get_divs( return_, link, typeOfDiv1, attrKey1, attrkValue1, typeOfDiv2 = 0, get = False, many = False, attrKey2 = 0, attrkValue2 = 0 ):
    #recupera la división especifica para trabajar y return_orna Href of text
        
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
        
        if return_ == "href":
            return [div.a.get("href") for div in divisions]
        elif ret == "text":
            return [div.a.get_text() for div in divisions]
    else:
        if typeOfDiv2 != 0:
            divisions = soup.find(typeOfDiv1, attrs = {attrKey1 : attrkValue1}).find_all(typeOfDiv2)
            if return_ == "href":
                return [div.a.get("href") for div in divisions]
            elif return_ == "text":
                return [div.a.get_text() for div in divisions]
            elif return_ == "table":
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

def climate_objetc_creator(clima_list):
    new_object = {}
    new_object["id"] = datetime.now().strftime("%d%m%Y%H%M%S")
    new_object["fecha"] = datetime.now().strftime("%d/%h/%Y")
    
    area = input("area de recolección de datos? (nacional por defecto) : ")
    if area == "":
        area = "Nacional"
    
    new_object["area"] = area
    max = 0
    min = 0
    max_average = 0
    min_average = 0

    for i in range(len(clima_list)):
        value = clima_list[i][1].split()

        for index in range(len(value)-2):
            if value[index] == "Temp.":
                value.pop(index)
        
        max_day = clima_list[i][0] + ":" + value[1][0] + value[1][1] + "°"
        min_day = clima_list[i][0] + ":" + value[4][0] + value[4][1] + "°"
        max_value = int(value[1][0] + value[1][1])
        max_average += max_value
        min_value = int(value[4][0] + value[4][1])
        min_average += min_value
        if i == 0:
            max = max_value
            max_clima_day = max_day
            min = min_value
            min_clima_day = min_day
        else:
            if max < max_value:
                max = max_value
                max_clima_day = max_day
            if min > max_value:
                min = max_value
                min_clima_day = min_day

        new_object[clima_list[i][0].split()[0]] = value
    
    new_object["maxima_semanal"] = max_clima_day
    new_object["minima_semanal"] = min_clima_day
    new_object["promedio_maximo"] = max_average//len(clima_list)
    new_object["promedio_minimo"] = min_average//len(clima_list)
    new_object["temperatura_media"] = (new_object["promedio_maximo"] + new_object["promedio_minimo"]) / 2

    print(new_object)
    return new_object


#endregion
#

#region scrap_init
url_pronostico_nacional = "https://www.smn.gob.ar/pronostico"
driver.get(url_pronostico)
climate_objetc_creator(get_divs("table", driver.page_source, "ul", "id", "lista_matriz", "li"))