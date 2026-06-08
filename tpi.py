'''
1. Agregar un país con todos los datos necesarios para almacenarse (No se permiten campos vacíos).
2. Actualizar los datos de Población y Superficie de un País.
3. Buscar un país por nombre (coincidencia parcial o exacta).

4. Filtrar países por:
    Continente
    Rango de población
    Rango de superficie

5. Ordenar países por:
    Nombre
    Población
    Superficie (ascendente o descendente)

6. Mostrar estadísticas:
    País con mayor y menor población
    Promedio de población
    Promedio de superficie
    Cantidad de países por continente
'''
def alta_pais():

    print("Agregar un País")
    
    
    while True:                         # ingreso pais
        nombre = input("\nNombre del país: ").strip().capitalize()

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

            break
        except ValueError as e:
            print("Error: debe ingresar un número entero.\n")
    
    while True:                         # ingreso superficie

        try:
            superficie = int(input("Superficie: "))

            if superficie < 0:       # comprobar valor menor a cero
                raise ValueError("El valor no puede ser menor a cero.\n")

            break
        except ValueError as e:
            print("Error: debe ingresar un número entero.\n")

    while True:                         # ingreso continente
        continente = input("Continente: ").strip().capitalize()

        if continente == "":            # comprobar nombre vacio
            print("Error: el continente no puede estar vacío.\n")
            continue

        else:
            break


    if nombre and poblacion and superficie and continente:
        with open("paises.csv", "a") as archivo:
            archivo.write(f"\n{nombre},{poblacion},{superficie},{continente}")

        print("País agregado correctamente.")
    else:
        print("Error: no se permiten campos vacíos.")


def actualizar_datos():

    while True:

        buscar = input("País a actualizar: ").strip().lower()

        if buscar == "":                # comprobar nombre vacio
            print("Error: el nombre no puede estar vacío.\n")
            continue

        else:
            break
                                        
    while True:                         # nuevo ingreso problación

        try:
            nueva_poblacion = int(input("Población: "))

            if nueva_poblacion < 0:     # comprobar valor menor a cero
                raise ValueError("El valor no puede ser menor a cero.\n")

            break
        except ValueError as e:
            print("Error: debe ingresar un número entero.\n")
    
    while True:                         # nuevo ingreso superficie

        try:
            nueva_superficie = int(input("Superficie: "))

            if nueva_superficie < 0:    # comprobar valor menor a cero
                raise ValueError("El valor no puede ser menor a cero.\n")

            break
        except ValueError as e:
            print("Error: debe ingresar un número entero.\n")    


    with open("paises.csv", "r") as archivo:
            lineas = archivo.readlines()

    encontrado = False

    for i in range(1, len(lineas)):         # salta la cabecera
        
        nombre, poblacion, superficie, continente = lineas[i].strip().split(",")

        if nombre.lower() == buscar:
            lineas[i] = f"{nombre},{nueva_poblacion},{nueva_superficie},{continente}\n"
            encontrado = True
            break

    if encontrado:
        with open("paises.csv", "w") as archivo:
            archivo.writelines(lineas)

        print("País actualizado correctamente.")
    else:
        print("País no encontrado.")



def consulta():

    while True:

        buscar = input("Buscar pais: ").strip().lower()

        if buscar == "":            # comprobar nombre vacio
            print("Error: el nombre no puede estar vacío.\n")
            continue

        else:
            break

    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()

    encontrado = False

    for linea in lineas[1:]:  # Salta la cabecera

        nombre, poblacion, superficie, continente = linea.strip().split(",")

        '''
        datos = linea.strip().split(",")
        nombre = datos[0]
        poblacion = datos[1]
        superficie = datos[2]
        continente = datos[3]
        '''

        if buscar in nombre.lower():
            print(f"País: {nombre}")
            print(f"Población: {poblacion}")
            print(f"Superficie: {superficie}")
            print(f"Continente: {continente}")
            print()
            encontrado = True

    if not encontrado:
        print("No se encontraron países.")

def estadisticas():
    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()

    mayor_pais = ""
    mayor_poblacion = 0

    menor_pais = ""
    menor_poblacion = None

    suma_poblacion = 0
    suma_superficie = 0
    cantidad_paises = 0

    continentes = {}

    for linea in lineas[1:]:
        nombre, poblacion, superficie, continente = linea.strip().split(",")

        poblacion = int(poblacion)
        superficie = int(superficie)

        # Mayor población
        if poblacion > mayor_poblacion:
            mayor_poblacion = poblacion
            mayor_pais = nombre

        # Menor población
        if menor_poblacion is None or poblacion < menor_poblacion:
            menor_poblacion = poblacion
            menor_pais = nombre

        # Acumuladores para promedios
        suma_poblacion += poblacion
        suma_superficie += superficie
        cantidad_paises += 1

        # Cantidad por continente
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    promedio_poblacion = suma_poblacion / cantidad_paises
    promedio_superficie = suma_superficie / cantidad_paises

    print("\nEstadísticas\n")
    print(f"País con mayor población: {mayor_pais} ({mayor_poblacion})")
    print(f"País con menor población: {menor_pais} ({menor_poblacion})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")

    print("\nCantidad de países por continente:")
    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")



# Inicio del programa

#paises = []             # lista de diccionario {'herramienta': str, 'cantidad': int]

opcion = 0

print("Gestión de Datos de Países en Python")
print("filtros, ordenamientos y estadísticas")

while opcion != 7:

    print("\nMenú de opciones:")    # muestra menu de opciones
    print("1. Agregar un país")
    print("2. Actualizar datos de Población y Superficie")
    print("3. Buscar un pais")
    print("4. ")
    print("5. ")
    print("6. Mostrar estadísticas")
    print("7. Salir")

    try:
        opcion = int(input("\nSeleccione una opción: "))
        if opcion == 1: alta_pais()
        elif opcion == 2: actualizar_datos()
        elif opcion == 3: consulta()
        elif opcion == 4: reporte_agotados(inventario)
        elif opcion == 5: alta_producto(inventario)
        elif opcion == 6: estadisticas()

        elif opcion >= 8 or opcion <= 0:
            print("Error: opción invalida")

    except ValueError as e:
        print("\nError: Debe ingresar un valor numérico entre 1 y 7.")
