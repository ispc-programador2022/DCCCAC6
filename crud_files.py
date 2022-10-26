    ##NOTA
#aprender a realizar un crud de carpetas y archivos va a ser importante cuando queramos manipular la data del
#scrapping de forma correcta y guardarla en DB, o exceles, o lo que sea que queramos.

import os
ruta = os.getcwd() #determinamos nuestra ubicacion en disco
print("la ruta se encuentra en ", ruta)

iteration = False
print("desea crear una nueva carpeta?")
choise = input("S? ")
if choise == "S" or choise == "s":
    iteration = True
while iteration:
    new_dir= input("nombre de la nueva carpeta: ")
    path = os.path.join(ruta, new_dir)

    if os.path.exists(path):
        print("el nombre de la carpeta ya existe, desea cambiarlo?")
        choise = input("S? ")
        if choise == "S" or choise == "s":
            iteration = True
        else:
            iteration = False
    else:
        os.mkdir(path)
        print("Carpeta creada con exito, desea crear otra?")
        choise = input("S? ")
        if choise == "S" or choise == "s":
            iteration = True
        else:
            iteration = False
print("creacion de carpetas finalizada")

print("desea eliminar alguna carpeta?")
choise = input("S? ")
if choise == "S" or choise == "s":
    iteration = True
while iteration:
        toDelete = input("nonbre de la carpeta a eliminar: ")
        path = os.path.join(ruta, toDelete)
        if os.path.exists(path):
            os.rmdir(path)
            print("la carpeta", toDelete, " ha sido eliminada con exito, desea continuar eliminando carpetas?")
            choise = input("S? ")
            if choise == "S" or choise == "s":
                iteration = True
            else:
                iteration = False
        else:
            print("esa carpeta no existe en el directorio actual, desea cambiar el nombre del documento a eliminar?")
            choise = input("S? ")
            if choise == "S" or choise == "s":
                iteration = True
            else:
                iteration = False
print("eliminación de carpetas finalizada")

print("el directorio queda con los siguientes archivos:")
print(os.listdir(ruta))

print("desea analizar y recorrer los archivos?")
choise = input("S? ")
if choise == "S" or choise == "s":
    with os.scandir(ruta) as itr:
        for i in itr:
            print(i.name)
            if i.is_file():
                print("es un archivo, no una carpeta")
            else:
                print("es una carpeta")