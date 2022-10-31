#instalar modulos lxml, requests, beautifulsoup4

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def get(url):
# no queremos que nuestro codigo se rompa y deje de ejecutar solo porque una página, por x motivo
# dejo de hacer funcionar sus links. Es buena practica ejecutar el codigo dentro del try-catch
# y, en el peor de los casos, no correr sobre un html y continuar con el resto
    
    try:
        return requests.get(url)
    except Exception as e:
        print("error en la request")
        print(e)
        print("\n")

#DECLARACIÓN DE LA URL SOBRE LA QUE SE TRABAJARÁ
p12= get("https://www.pagina12.com.ar/")

## ANALIZAMOS LAS REQ - RES LO QUE TRAE EL GET

## RES
# print(p12.status_code)
# => print(p12.text) ## imprime todo el html en forma de STRING <=
# print(p12.content) ## imprime el html en forma de BIT PLANO, especial para archivos como img
# print(p12.headers) ##imprime solo el encabezado del html

## REQ
#print(p12.request.headers) #imprime los encabezados de la CONSULTA =>
##{'User-Agent': 'python-requests/2.27.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive'}
                # se reconoce que la consulta proviene de un software automatizado, pero se puede enmascarar

#print(p12.request.method) #imprime el metodo de la consulta, GET POST PUT DELETE
#print(p12.request.url) #impre la url donde se estan procesando datos, muchas veces las paginas redireccionan y
#es importante contar con este metodo

##  INICIALIZAMOS EL BEAUTIFUL SOUP SOBRE EL STRING HTML 
p12_soup = bs(p12.text, "lxml")
#print(type(soup))
#print(soup.prettify())

# soup.find("ul") #encuentra TAGs especificos, en este caso la etiqueta de lista <UL> del encabezado de pagina
# con todas sus etiquetas de secciones <LI>. El problema es que solo devuelve el primer TAG, por lo que debemos 
# ser muy especificos. Finalmente, devuelve una lista de elementos debido a que, sobre el metodo find(), ejecutamos
# un nuevo metodo find_all() que devuelve un array, en este caso de todas las etiquetas <LI> dentro de <UL>

li_sections=p12_soup.find("ul", attrs={"class":"horizontal-list main-sections hide-on-dropdown"}).find_all("li")

## ANALIZAMOS EL ELEMENTO 0 DE LA LISTA

##section=li_sections[0]
# print(section) #<li class="p12-separator--right--primary"><a href="https://www.pagina12.com.ar/secciones/el-pais">El país</a></li>
# print(section.a.get("href")) #https://www.pagina12.com.ar/secciones/el-pais
# print(section.a.get_text()) #El país

links_of_sections=[seccion.a.get("href") for seccion in li_sections]
names_of_sections=[seccion.a.get_text() for seccion in li_sections]

print(f"Existen {len(links_of_sections)} secciones diferentes de noticias para leer:")
print(names_of_sections)
#print(f"trabajaremos sobre la primera sección : [{names_of_sections[0]}]")

def get_notes(link):
    new_section = get(link)
    soup_new_section=bs(new_section.text, "lxml")
    titles = soup_new_section.find_all("div", attrs={"class":"articles-list"})
    titles = titles[1].find_all("h2", attrs={"class":"is-display-inline title-list"})
    return [title.a.get("href") for title in titles]

# # volvemos a ejecutar un requests.get, ahora de los nuevos links que tenemos guardados
# new_section_elPais=get(links_of_sections[0]) # el elemento 0 corresponde a la sección "EL PAIS"
# section_elPais_soup=bs(new_section_elPais.text, "lxml")
# #print(section_elPais_soup.prettify())
# titles_elPais=section_elPais_soup.find_all("div", attrs={"class":"articles-list"}) ##hay dos div iguales, necesito el segundo
# titles_elPais=titles_elPais[1].find_all("h2", attrs={"class":"is-display-inline title-list"}) #recupero todos los h2

# links_of_titles_elPais=[title.a.get("href") for title in titles_elPais]

#print(f"hay {len(links_of_titles_elPais)} noticias de [{names_of_sections[0]}] para procesar")

def note_dict_creator(note_soup):
    note_dict = {}

    try:
        #TITUTLO
        note_title=note_soup.find("div", attrs={"class":"col 2-col"})
        #print(note_title.h1.get_text())
        note_dict["title"]=note_title.h1.get_text()

        #IMAGEN
        note_media=note_soup.find("div", attrs={"class":"article-main-media-image__container"}).find_all("img")
        if len(note_media)>0:
            note_media_img=note_media[-1]
            note_media_src=note_media_img.get("src")
            try:
                note_media_req=requests.get(note_media_src)
                if note_media_req.status_code == 200:
                    #print("imagen cargada")
                    note_dict["img"]=note_media_src
                else:
                    print("no hay imagen")
                    note_dict["img"]=None
            except:
                print("no hay imagen")
                note_dict["img"]=None
        else:
            print("no hay imagen")
            note_dict["img"]=None
        #FECHA
        #CUERPO
    except Exception as e:
        print("Error en la carga del diccionario")
        print(e)
        print("\n")

    return note_dict

print("")
# for i in range(len(links_of_titles_elPais)):
#     print(f"{i+1})")
#     print(note_dict_creator(links_of_titles_elPais[i], 0))

def scrape_notes(url):
    url= "https://www.pagina12.com.ar"+url
    try:
        note = requests.get(url)
    except Exception as e:
        print("Error al escrapear", url)
        print(e)
        return None

    if note.status_code != 200:
        print(f"Error al intentar obtener la nota {url}")
        print(f"status code: {note.status_code}")
    
    note_soup=bs(note.text, "lxml")
    note_dict=note_dict_creator(note_soup)
    note_dict["url"]=url

    return note_dict

#scrape_notes(links_of_titles_elPais[0])
print("")

notes_array = []
for link in links_of_sections:
    try:
        r = requests.get(link)
        if r.status_code == 200:
            print("agarra el link", link)
            notes_array.extend(get_notes(link))
        else:
            print("no dio el status Code para", link)
    except:
        print("no se pudo obtener la sección", link)

print("")
print(f"se obtienen {len(notes_array)} notas para ser procesadas")

data = []
for i, note in enumerate(notes_array):
    print(f"Scrapeando la nota {i+1}/{len(notes_array)}")
    data.append(scrape_notes(note))
    if i > 8:
        break

print(len(data), "elementos ya están procesados")
#solo falta armar el Data Frame

df = pd.DataFrame(data)
print(df.head())
df.to_csv("notas Pagina12.csv")