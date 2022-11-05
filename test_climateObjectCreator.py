from datetime import datetime
prueba = [['Viernes 4', 'Temp. Máx 30° | Mín -°'], ['Sábado 5', 'Temp. Máx 10° | Mín -°'],
 ['Domingo 6', 'Máx 50° | Mín 0°'], ['Lunes 7', 'Máx -° | Mín -°'], ['Martes 8', 'Máx -° | Mín -°'],
  ['Miércoles 9', 'Máx -° | Mín -°'], ['Jueves 10', 'Máx -° | Mín 10°']]
prueba2 = [['Viernes 4', 'Temp. Máx 30° | Mín 40'], ['Sábado 5', 'Temp. Máx 10° | Mín 30'],
 ['Domingo 6', 'Máx 50° | Mín 15°'], ['Lunes 7', 'Máx 35° | Mín 10°'], ['Martes 8', 'Máx 30° | Mín 20°'],
  ['Miércoles 9', 'Máx 32° | Mín 12°'], ['Jueves 10', 'Máx 28° | Mín 7°']]
prueba3 = [['Viernes 4', 'Temp. Máx -° | Mín -°'], ['Sábado 5', 'Temp. Máx -° | Mín -°'],
 ['Domingo 6', 'Máx -° | Mín -°'], ['Lunes 7', 'Máx -° | Mín -°'], ['Martes 8', 'Máx -° | Mín -°'],
  ['Miércoles 9', 'Máx -° | Mín -°'], ['Jueves 10', 'Máx -° | Mín -°']]

prueba_list = [prueba, prueba2, prueba3]

def climate_object_creator(clima_list, area):
    # retorna un objeto con todas las propiedades recuperadas de la web listo para ser procesado en pandas

    #region
    new_object = {}
    new_object["id"] = datetime.now().strftime("%d%m%Y%H%M%S")+area
    new_object["fecha"] = datetime.now().strftime("%d/%h/%Y")
    new_object["ciudad"] = area 
    max = 0
    min = 0
    max_day = "sin datos"
    min_day = "sin datos"
    max_average = 0
    min_average = 0
    no_max_data = 0
    no_min_data = 0
    no_val_data = 0
    min_clima_day = ""
    max_clima_day = ""
    first = True
    #endregion

    try:
        for i in range(len(clima_list)):

            print(f"{i+1}° iteración. El elemento es: {clima_list[i]}")
            
            counter = True
            counter_min = True 
            counter_max = True
            min_value = 0
            max_value = 0
            value = clima_list[i][1].split()
            print(f"la lista es: {value}, tiene {len(value)} elementos \n")
            remove_index = []
            for index in range(len(value)):
                if value[index] == "Temp.":
                    remove_index.append(index)
                if value[index] == "-°":
                    print("se activa el sumador de puntos de no existencia de datos en el indice: ",index,"en el valor: ", value[index])
                    if index < 3:
                        no_max_data += 1
                        print(f" => se adiere un punto a no_max_data = {no_max_data}, por el indice {index} ")
                        value[index-1] = "SIN DATOS"
                        counter_max = False
                    else:
                        no_min_data += 1
                        print(f"=>  se adiere un punto a no_min_data = {no_min_data}, por el indice {index} ")
                        value[index-1] = "SIN DATOS"
                        counter_min = False
                    remove_index.append(index)
                    
            for index in reversed(range(len(remove_index))):
                value.pop(remove_index[index])

            if counter_max == False or counter_min == False:
                no_val_data += 1
                counter = False
                print(f"se suma 1 a no_val_data {no_val_data} ")
                        

            print(f"\nla nueva lista es: {value} ")
            print(f"por lo tanto es {counter_max} que existan datos maximos y {counter_min}"+ 
            f" que existan datos minimos para procesar el día {clima_list[i][0]} \n")
            
            if counter_max:
                max_day = clima_list[i][0] + " : " + value[1][0] + value[1][1] + "°"
                print(f"max_day ahora es: {max_day}")
            if counter_min:
                try:
                    if value[4][1] != "°":
                        min_day = clima_list[i][0] + " : " + value[4][0] + value[4][1] + "°"
                    else:
                        min_day = clima_list[i][0] + " : " + value[4][0] + "°"
                except:
                    if value[3][1] != "°":
                        min_day = clima_list[i][0] + " : " + value[3][0] + value[3][1] + "°"
                    else:
                        min_day = clima_list[i][0] + " : " + value[3][0] + "°"
                print(f"min_day ahora es: {min_day} //linea 79")

            if counter_max:
                try:
                    print(f"se intenta procesar el valor {value[1][0]} para maximos")
                    if value[1][0] != "-":
                        if value[1][1] != "°":
                            max_value = int(value[1][0] + value[1][1])
                        else: 
                            max_value = int(value[1][0])
                    print(f"al promedio = {max_average} se le suma {max_value} ")
                    max_average += max_value
                except:
                    max_value = "SIN DATOS"
                    counter = False
                    print(f"se pasa Counter a {counter} ")
            # else:
            #     max_value = "SIN DATOS"
            #     counter = False
            #     print(f"el valor es: {value}")
            
            if counter_min:
                print("=> se procesa el minimo del dia:")
                try:
                    print(f"se intenta procesar el valor {value[4][0]} para minimos en el primer try")
                    if value[4][0] != "-":
                        if value[4][1] != "°":
                            min_value = int(value[4][0] + value[4][1])
                        else:
                            min_value = int(value[4][0])
                    print(f"a {min_average} se le suma {min_value} ")
                    min_average += min_value
                except:
                    # min_value = "SIN DATOS"
                    # counter = False
            # else:
                    try:
                        print(f"se intenta procesar el valor {value[3][0]} para minimos en el segundo try")
                        if value[3][0] != "-":
                            if value[3][1] != "°":
                                min_value = int(value[3][0] + value[3][1])
                            else:
                                min_value = int(value[3][0])
                        print(f"a {min_average} se le suma {min_value} ")
                        min_average += min_value
                    except:
                        min_value = "SIN DATOS"
                        counter = False
                        print(f"se pasa Counter a {counter} ")

            # print(f"si counter es False = {counter} , se suma 1 a no_val_data {no_val_data} ")
            # if counter == False:
            #     no_val_data += 1
            #     print(f"se suma 1 a no_val_data {no_val_data} ")
            
            print(f"los valores max value= {max_value},min value = {min_value}, max day = {max_day}, min day = {min_day} \n")
            print(f" ====> la primera vez está en modo: {first} ")

            if first == True:
                if i <= no_val_data and counter_max == True or counter_min == True:
                    print("SE ACTIVA LA OPCION DE PRIMERA ITERACION CON VALORES")
                    print(f"los valores son {max_value}, {min_value}, {max_day}, {min_day}\n")
                    max = max_value
                    max_clima_day = max_day
                    min = min_value
                    min_clima_day = min_day
                    first = False
                    print(f"y ahora se desactivo: {first} ")
            elif counter == True:
                print("se activa la opción de iteracion con valores")
                print(f"los valores son {max_value}, {min_value}, {max_day}, {min_day} ")
                if max < max_value:
                    max = max_value
                    max_clima_day = max_day
                if min > max_value:
                    min = max_value
                    min_clima_day = min_day

            if value == ['Máx', '|', 'Mín']:
                value = "no hay datos"
            
            print(f"=> se agrega '{value}' como propiedad '{clima_list[i][0].split()[0]}' al objeto")
            new_object[clima_list[i][0].split()[0]] = value
            print(clima_list[i][0].split()[0], " = ", new_object[clima_list[i][0].split()[0]])

            print("")
            print(f"de momento los valores no_max_data = {no_max_data} y no_min_data = {no_min_data}")
            print(f"de momento los promedios son max_average = {max_average} y min_average = {min_average}")
            print(f"de momento el valor no_val_data = {no_val_data}")
            print("-----------------------------------------------------------------------------------")
    
    except Exception as e:
        print(e)
    
    #region

    try:
        print(f"falta/n {no_max_data} dato/s para maximos, por lo que el promedio {max_average} se divide en {len(clima_list)} - {no_max_data}  ")
        print(f"lo que da como resultado {max_average//(len(clima_list)-no_max_data)} ")
        print(f"falta/n {no_min_data} dato/s para minimos, por lo que el promedio {min_average} se divide en {len(clima_list)} - {no_min_data}  ")
        print(f"lo que da como resultado {min_average//(len(clima_list)-no_min_data)} ")
    except:
        print(f"el valor no_val_data = {no_val_data} imposibilita cualquier cuenta")

    print("")
    if no_val_data == 0:
        new_object["maxima_semanal"] = max_clima_day
        new_object["minima_semanal"] = min_clima_day
        new_object["promedio_maximo"] = max_average//(len(clima_list)-no_max_data)
        new_object["promedio_minimo"] = min_average//(len(clima_list)-no_min_data)
        new_object["temperatura_media"] = (new_object["promedio_maximo"] + new_object["promedio_minimo"]) / 2
        new_object["estatus"] = "PERFECTO"
    elif no_val_data < 7:
        new_object["maxima_semanal"] = max_clima_day
        new_object["minima_semanal"] = min_clima_day
        new_object["promedio_maximo"] = max_average//(len(clima_list)-no_max_data)
        new_object["promedio_minimo"] = min_average//(len(clima_list)-no_min_data)
        new_object["temperatura_media"] = (new_object["promedio_maximo"] + new_object["promedio_minimo"]) / 2
        new_object["estatus"] = f"ERROR: FALTAN {no_max_data + no_min_data} DATOS DE LA SEMANA"
    else:
        if no_min_data < 7:
            print("activa crear minimos")
            new_object["minima_semanal"] = min_clima_day
            new_object["promedio_minimo"] = min_average//(len(clima_list)-no_min_data)
            new_object["estatus"] = "ERROR: NINGÚN DÍA DE LA SEMANA ESTA COMPLETO"
        elif no_max_data < 7:
            print("activa crear maximos")
            new_object["maxima_semanal"] = max_clima_day
            new_object["promedio_maximo"] = max_average//(len(clima_list)-no_max_data)
            new_object["estatus"] = "ERROR: NINGÚN DÍA DE LA SEMANA ESTA COMPLETO"
        else:
            new_object["estatus"] = "ERROR: NINGÚN DÍA DE LA SEMANA ESTA COMPLETO"

    for key,val in new_object.items():
        print(f"{key} : {val}")
    #endregion
    return new_object
    
#
print("")

for i in prueba_list:
    climate_object_creator(i, "Rosario")
    print("\n--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------\n")
