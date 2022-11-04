#instalar modulos => selenium (con chromeDriver), lxml, requests, beautifulsoup4 y pandas

#region variables
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
import os
from datetime import date
from datetime import datetime
clear = lambda: os.system('cls')

this_route = os.getcwd()
options = ChromeOptions()
options.headless = True

area_list = ["Salta (Capital), Salta","San Salvador de Jujuy (Capital), Jujuy", "Rosario (Rosario), Santa Fe", 
"Córdoba (Capital), Córdoba", "Capital Federal (Capital Federal), Capital Federal", "Paraná (Paraná), Entre Ríos", 
"Posadas (Capital), Misiones", "Formosa (Formosa), Formosa", "Viedma (Adolfo Alsina), Río Negro", 
"Ushuaia (Ushuaia), Tierra del Fuego, Antártida e Islas del Atlántico Sur", "Mendoza (Capital), Mendoza", 
"San Juan (Capital), San Juan", "San Luis (Capital), San Luis", "Rawson (Rawson), Chubut",
"Santiago del Estero (Capital), Santiago del Estero", "La Rioja (Capital), La Rioja", "Neuquén (Confluencia), Neuquén",
"Resistencia (San Fernando), Chaco", "Río Gallegos (Güer Aike), Santa Cruz", "Corrientes (Capital), Corrientes",
"Santa Rosa (Capital), La Pampa", "San Miguel de Tucumán (Capital), Tucumán",
"San Fernando del Valle de Catamarca (Capital), Catamarca"] #23 provincias

driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe", options=options)
url_pronostico_nacional = "https://www.smn.gob.ar/pronostico"
driver.get(url_pronostico_nacional)
  
clear()

#endregion
#

#region funciones()
def get_Url(url):
    
    # requiere la pág para escrapear mediante el metodo requests.get()
    try:
        return requests.get(url)
    except Exception as e:
        print("error en la request")
        print(e)
        print("\n")
#

def get_divs( return_, link, typeOfDiv1, attrKey1, attrkValue1, typeOfDiv2 = 0, get = False, many = False, attrKey2 = 0, attrkValue2 = 0 ):
    
    #activa o inive la funcion get_url() en base a necesitar => requests.get(TRUE) o driver.get("FALSE")     
    if get == True:
        webPage = get_Url(link)
        soup = bs(webPage.text, "lxml")
    else:
        soup = bs(link, "lxml")
        #driver.close()

    #devuelve un array de elementos find_all() o un solo elemento find()
    if many:
        divisions = soup.find_all(typeOfDiv1, attrs = {attrKey1 : attrkValue1})

        if typeOfDiv2 != 0 :
            if attrKey2 != 0:
                divisions = soup.find_all(typeOfDiv2, attrs = {attrKey2 : attrkValue2})
            else:
                divisions = soup.find_all(typeOfDiv2)
        
        if return_ == "href":
            return [div.a.get("href") for div in divisions]
        elif return_ == "text":
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

def climate_object_creator(clima_list, area):
   
    # retorna un objeto con todas las propiedades recuperadas de la web listo para ser procesado en pandas
    new_object = {}
    new_object["id"] = datetime.now().strftime("%d%m%Y%H%M%S")+area
    new_object["fecha"] = datetime.now().strftime("%d/%h/%Y")
    new_object["ciudad"] = area
    max = 0
    min = 0
    max_average = 0
    min_average = 0
    no_max_data = 0
    no_min_data = 0
    no_val_data = 0
    min_clima_day = ""
    max_clima_day = ""

    for i in range(len(clima_list)):
        counter = False
        value = clima_list[i][1].split()

        for index in range(len(value)-2):
            if value[index] == "Temp.":
                value.pop(index)
        max_day = clima_list[i][0] + " : " + value[1][0] + value[1][1] + "°"
        min_day = clima_list[i][0] + " : " + value[4][0] + value[4][1] + "°"

        try:
            if value[1][0] != "-":
                if value[1][1] != "°":
                    max_value = int(value[1][0] + value[1][1])
                else: 
                    max_value = int(value[1][0])
            max_average += max_value
        except:
            max_value = "sin datos"
            no_max_data += 1
            counter = True

        try:
            if value[4][0] != "-":
                if value[4][1] != "°":
                    min_value = int(value[4][0] + value[4][1])
            else:
                min_value = int(value[4][0])
            min_average += min_value
        except:
            min_value = "sin datos"
            no_min_data += 1
            counter = True

        if counter == True:
            no_val_data += 1

        if i <= no_val_data and counter == False:
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
            no_val_data = 0

        new_object[clima_list[i][0].split()[0]] = value
    
    new_object["maxima_semanal"] = max_clima_day
    new_object["minima_semanal"] = min_clima_day
    new_object["promedio_maximo"] = max_average//len(clima_list)-no_max_data
    new_object["promedio_minimo"] = min_average//len(clima_list)-no_min_data
    new_object["temperatura_media"] = (new_object["promedio_maximo"] + new_object["promedio_minimo"]) / 2

    return new_object
#

def input_write(input):

    #hace uso del buscador para determinar que ciudades analizar
    element = driver.find_element_by_xpath('/html/body/div[2]/div/section/div/section/div/div/div/div/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/input')
    driver.implicitly_wait(2)

    element.send_keys(input, Keys.ARROW_DOWN)
    button = driver.find_element_by_xpath('/html/body/div[2]/div/section/div/section/div/div/div/div/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div[2]/ul/li[2]/a')
    driver.implicitly_wait(2)
    try:
        button.click()
    except Exception as e:
        print("problema:\n")
        print(e)
    element.clear()  
#

def city_name(area):

    #recupera de la lista de areas el nombre de cada una, dejando de lado otra info que necesita el <input> buscador
    city = ""
    for text in area:
        if text[0] == "(":
            break
        else:
            city += text
    return city
#

def scrape_cities(areas):
    
    data = []
    for i in range(len(areas)):
        input_write(areas[i])
        city = city_name(areas[i])
        objeto = climate_object_creator(get_divs("table", driver.page_source, "ul", "id", "lista_matriz", "li"), city)
        data.append(objeto)
        for key,value in objeto.items():
            print(f"{key}:{value}")
        print("\n")
        driver.implicitly_wait(2)
    
    return data
#

def to_dataFrame(data, new_dir, name):
    df = pd.DataFrame(data)
    print(df.head())
    path = os.path.join(this_route, new_dir)
    
    if os.path.exists(path):
        df.to_csv(f"{path}\\"+f"{name}.csv")
    else:
        os.mkdir(path)
        df.to_csv(f"{path}\\"+f"{name}.csv")
#

#endregion
#

#region scrap_init
data = scrape_cities(area_list)
fecha = datetime.now().strftime("%d%h%Y_%H%M%S")
to_dataFrame(data, "dataFrames", f"dataFrame_{fecha}")