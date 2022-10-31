# %% [markdown]
#     #Curso de autmatización y web Scrapping
# 
# Utilizamos la herramienta Chrome Driver, un archivo .exe basado en la interfaz WebDriver (simulador de interacciones cliente-navegador) para iniciar el Chrome sobre el framework Selenium (Seleniun es el resultado de fusionar la APi WebDriver con un antiguo software llamado JavaScriptTestRunner, creado en 2004 con el fin de validar la compatibilidad de una app con diferentes navegadores) que permite a los desarrolladores probar y registrar las interacciones con una aplicación web de forma completamente automática.

# %%
from selenium import webdriver
from selenium.webdriver.common.by import By

# %%
url1 = "https://listado.mercadolibre.com.ar/televisor-plasma#D[A:televisor%20plasma]"

# %%
    ##abrir ventana
driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe")
driver.get(url1)
#driver.maximize_window()

# %% [markdown]
# aprender a usar Xpath (expresiones que recorren y procesan un documento XML parseado por un analizador (o parser) construyendo un árbol de nodos. Este árbol comienza con un elemento raíz, que se diversifica a lo largo de los elementos que cuelgan de él y acaba en nodos hoja, que contienen solo texto).
#  Hay Xpath relativas y absolutas:

# %%
#obtener precios de televisores plasma de mercado libre basados en XPath absolutos: utilizar Ctrl+F para buscar por Xpath
##//li[@class="ui-search-layout__item shops__layout-item"]/div/div/div[2]/div[3]/div/div/div/div/div/span/span

    #HAY DOS FORMAS DE LLAMAR AL METODO .find_elements =>
price_envioGratis = driver.find_elements(By.XPATH, '//li[@class="ui-search-layout__item shops__layout-item"]/div/div/div[2]/div[3]/div/div/div/div/div/span/span/span[2]')
price_sinEnvioGratis = driver.find_elements_by_xpath('//li[@class="ui-search-layout__item shops__layout-item"]/div/div/div[2]/div[2]/div/div/div/div/div/span/span[2]/span[2]')

print("se obtiene una lista con", len(price_envioGratis), "precios de envío sin cargo")
# for i in price_envioGratis:
#     print(i.text)
print("se obtiene una lista con", len(price_sinEnvioGratis), "precios de envío con cargo")
# for i in price_sinEnvioGratis:
#     print(i.text)
print("__________________________________________________________________________________")
prices = price_envioGratis + price_sinEnvioGratis
# for i in prices:
#     print(i.text)

# %%
#se obtienen los nombres de cada uno de los televisores por medio de la clase div solamente:
## //h2[@class="ui-search-item__title shops__item-title"]

#item_names = driver.find_elements_by_class_name('ui-search-item__title shops__item-title')
#item_names = driver.find_elements(By.CLASS_NAME, "ui-search-item__title shops__item-title")
# NO FUNCIONA SELECCIONAR POR CLASE, SE INTENTA POR TAG <h2>

item_names = driver.find_elements(By.TAG_NAME, ("h2"))
#los 2 ultimos elementos de mas que no deben sen guardados en la ista, por lo que se eliminan
for i in range(2):
    item_names.pop(50)

print("hay", len(item_names), "productos con",len(prices), "precios listos para procesar")

for i in range (len(item_names)):
    print(item_names[i].text)
    print(prices[i].text)
    print("")

driver.close()


