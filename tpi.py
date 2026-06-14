# Trabajo Práctico Integrador - Programación 1

def alta_pais():

    print("Agregar un Pais")
    
    while True:                         # ingreso pais
        nombre = input("\nNombre del pais: ").strip().capitalize()

        if nombre == "":                # comprobar nombre vacio
            print("\nError: el nombre no puede estar vacío")
            continue
        else:
            break

    while True:                         # ingreso problación

        try:
            poblacion = int(input("Población: "))

            if poblacion < 0:       # comprobar valor menor a cero
                raise ValueError("El valor no puede ser menor a cero.\n")

            superficie = int(input("Superficie: ")) # ingreso superficie

            if superficie < 0:       # comprobar valor menor a cero
                raise ValueError("El valor no puede ser menor a cero.\n")

            break
        except ValueError as e:
            print("Error: debe ingresar un numero entero.\n")

    while True:                         # ingreso continente
        continente = input("Continente: ").strip().capitalize()

        if continente == "":            # comprobar nombre vacio
            print("Error: el continente no puede estar vacio.\n")
            continue
        else:
            break

    if nombre and poblacion and superficie and continente:
        with open("paises.csv", "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{poblacion},{superficie},{continente}\n")
        print("País agregado correctamente.")
    else:
        print("Error: no se permiten campos vacíos.")


def actualizar_datos():

    while True:

        buscar = input("Pais a actualizar: ").strip().lower()

        if buscar == "":                # comprobar nombre vacio
            print("Error: el nombre no puede estar vacio.\n")
            continue

        else:
            break
                                        
    while True:                         #nuevo ingreso problación

        try:
            nueva_poblacion = int(input("Poblacion: "))

            if nueva_poblacion < 0:       # comprobar valor menor a cero
                raise ValueError("El valor no puede ser menor a cero.\n")

            nueva_superficie = int(input("Superficie: ")) # ingreso superficie

            if nueva_superficie < 0:       # comprobar valor menor a cero
                raise ValueError("El valor no puede ser menor a cero.\n")

            break
        except ValueError as e:
            print("Error: debe ingresar un numero entero.\n")   

    with open("paises.csv", "r", encoding="utf-8") as archivo:
            lista_paises = archivo.readlines()

    encontrado = False

    for i in range(1, len(lista_paises)):         # recorre linea por linea la lista, salta la cabecera
        
        nombre, poblacion, superficie, continente = lista_paises[i].strip().split(",")    # asigna a cada variable su indice correspondiente

        if nombre.lower() == buscar:
            lista_paises[i] = f"{nombre},{nueva_poblacion},{nueva_superficie},{continente}\n"
            encontrado = True
            break

    if encontrado:
        with open("paises.csv", "w", encoding="utf-8") as archivo:
            archivo.writelines(lista_paises)

        print("Pais actualizado correctamente.")
    else:
        print("Pais no encontrado.")


def consulta():

    while True:                             # ingresa pais a buscar

        buscar = input("Buscar pais: ").strip().lower()

        if buscar == "":            # comprobar nombre vacio
            print("Error: el nombre no puede estar vacío.\n")
            continue

        else:
            break

    with open("paises.csv", "r", encoding="utf-8") as archivo:
        lista_paises = archivo.readlines()

    encontrado = False

    print()

    for linea in lista_paises[1:]:        # recorre linea por linea la lista, y salta la cabecera

        nombre, poblacion, superficie, continente = linea.strip().split(",")    # separa a cada variable una linea obtenida de la lista

        if buscar in nombre.lower():    # compara linea por linea si "buscar" esta en "nombre", si esta lo muestra
            print(f"Pais: {nombre}")
            print(f"Poblacion: {poblacion}")
            print(f"Superficie: {superficie}")
            print(f"Continente: {continente}")
            encontrado = True

    if not encontrado:
        print("No se encontraron países con ese nombre.")

def filtrar_países():
    opcion = 0
    buscar = ""

    with open("paises.csv", "r", encoding="utf-8") as archivo:      # carga todo el archivo en una lista
        lista_paises = archivo.readlines()[1:] 

    print("\nFiltrar paises por:")                                  # muestra menú
    print("1. Continente")
    print("2. Rango de población")
    print("3. Rango de superficie\n")

    while opcion != 1 and opcion != 2 and opcion != 3:              # comprobar opcion de menú valida
        opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:                                                 # Continente
        while buscar == "":                                         # comprobar nombre vacio
            buscar = input("Ingrese el continente: ").strip().lower()

        for linea in lista_paises:                                        # recorre la lista
            nombre, poblacion, superficie, continente = linea.strip().split(",")

            if buscar == continente.lower():                        # busca coincidencia y muestra el pais
                print(f"Paises: {nombre}")

    elif opcion == 2:                                               # Rango Problación

        try:

            poblacion_min = int(input("Ingrese el mínimo de poblacion: "))

            while True:

                poblacion_max = int(input("Ingrese el máximo de poblacion: "))
                if poblacion_min > poblacion_max:
                    print("Error: El numero debe ser mayor que el valor minimo ingresado.\n")
                else:
                    break

            for linea in lista_paises:
                nombre, poblacion, superficie, continente = linea.strip().split(",")    # separa a cada variable una linea obtenida de la lista

                poblacion = int(poblacion)

                if poblacion_min < poblacion and poblacion_max > poblacion:     # chequeo valor maximo sea mayor que minimo
                    print(f"País: {nombre}")

                
        except ValueError as e:
            print("Error: debe ingresar un numero entero.\n") 

    elif opcion == 3:                                               # Rango Superficie

        try:
            superficie_min = int(input("Ingrese el minimo de superficie: "))    # comprobar valor valido

            while True:

                superficie_max = int(input("Ingrese el máximo de superficie: "))
                
                if superficie_min > superficie_max:                             # chequeo valor maximo sea mayor que minimo
                    print("Error: El numero debe ser mayor que el valor minimo ingresado.\n")
                else:
                    break

            for linea in lista_paises:
                nombre, poblacion, superficie, continente = linea.strip().split(",")    # separa a cada variable una linea obtenida de la lista

                superficie = int(superficie)

                if superficie_min < superficie and superficie_max > superficie:         # comprobar rangos y mostrar pais
                    print(f"paises: {nombre}")

        except ValueError as e:
            print("Error: debe ingresar un numero entero.\n") 

def ordenar_países():
    opcion = 0
    paises = []

    with open("paises.csv", "r", encoding="utf-8") as archivo:
        lista_paises = archivo.readlines()[1:] 

    for linea in lista_paises:
        nombre, poblacion, superficie, continente = linea.strip().split(",")        # separa a cada variable una linea obtenida de la lista

        paises.append({"nombre": nombre, "poblacion": int(poblacion), "superficie": int(superficie), "continente": continente})     # carga el diccionario en la lista paises

    print("\nOrdenar paises por:")
    print("1. Nombre")
    print("2. Poblacion")
    print("3. Superficie ascendente")
    print("4. Superficie descendente")

    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:              # comprobar opcion de menú valida
        opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        paises.sort(key=lambda x: x["nombre"])          # ordena segun la clave indicada
    elif opcion == 2:
        paises.sort(key=lambda x: x["poblacion"])
    elif opcion == 3:
        paises.sort(key=lambda x: x["superficie"])
    elif opcion == 4:
        paises.sort(key=lambda x: x["superficie"], reverse=True)
    else:
        print("Opción inválida")
        return
    
    print("\nPaises ordenados:\n")
    for i in paises:                                    # recore la lista y muestra cada fila
        print(f"{i["nombre"]}, {i["poblacion"]}, {i["superficie"]}, {i["continente"]}")

def estadisticas():
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        lista_paises = archivo.readlines()

    mayor_pais = ""             # definir variables
    mayor_poblacion = 0

    menor_pais = ""
    menor_poblacion = None

    suma_poblacion = 0
    suma_superficie = 0
    cantidad_paises = 0

    continentes = {}            # crea el diccionario

    for linea in lista_paises[1:]:      # recorre linea por linea la lista, y salta la cabecera 
        nombre, poblacion, superficie, continente = linea.strip().split(",")

        poblacion = int(poblacion)          # pasa valores a un entero
        superficie = int(superficie)        # pasa valores a un entero

        if poblacion > mayor_poblacion:     # busca el número mayor de habitantes
            mayor_poblacion = poblacion
            mayor_pais = nombre

        if menor_poblacion is None or poblacion < menor_poblacion:      # busca el número mayor de habitantes
            menor_poblacion = poblacion
            menor_pais = nombre

        # Acumuladores para promedios
        suma_poblacion += poblacion
        suma_superficie += superficie
        cantidad_paises += 1

        # Cantidad por continente
        if continente in continentes:       # si continente no está en el dic lo agrega, si esta suna 1
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    promedio_poblacion = suma_poblacion / cantidad_paises                   # calcula los promedios
    promedio_superficie = suma_superficie / cantidad_paises

    print("\nEstadísticas\n")                                               # muestra todas las estadísticas
    print(f"Pais con mayor poblacion: {mayor_pais} ({mayor_poblacion})")
    print(f"Pais con menor poblacion: {menor_pais} ({menor_poblacion})")
    print(f"Promedio de poblacion: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")

    print("\nCantidad de paises por continente:")                           # muestra el dic. continentes
    for continente in continentes:
        print(f"{continente}: {continentes[continente]}")



# Inicio del programa
opcion = 0

print("Gestión de Datos de Países en Python")
print("filtros, ordenamientos y estadísticas")

while opcion != 7:

    print("\nMenu de opciones:")    # muestra menu de opciones
    print("1. Agregar un pais")
    print("2. Actualizar datos de Poblacion y Superficie")
    print("3. Buscar un pais")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadisticas")
    print("7. Salir")

    try:
        opcion = int(input("\nSeleccione una opcion: "))
        if opcion == 1: alta_pais()
        elif opcion == 2: actualizar_datos()
        elif opcion == 3: consulta()
        elif opcion == 4: filtrar_países()
        elif opcion == 5: ordenar_países()
        elif opcion == 6: estadisticas()

        elif opcion >= 8 or opcion <= 0:
            print("Error: opción invalida")

    except ValueError as e:
        print("\nError: Debe ingresar un valor numerico entre 1 y 7.")
