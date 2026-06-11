# Programación 1 - Trabajo Práctico Integrador
## TPI - UTN TUPaD


### Gestión de Países

#### Descripción

Aplicación desarrollada en Python para gestionar información de países almacenada en un archivo CSV.

### El sistema permite:

Agregar países.
Buscar países por nombre.
Actualizar población y superficie.
Mostrar estadísticas generales.
Filtrar países según distintos criterios.

Los datos se almacenan de forma persistente en un archivo paises.csv.

### Tecnologías utilizadas
* Python 3.x
* Archivos CSV
* Listas
* Diccionarios
* Funciones


### Estructura de datos

Cada país posee los siguientes atributos:
* Campo	Descripción
* nombre	Nombre del país
* poblacion	Cantidad de habitantes
* superficie	Superficie en km²
* continente	Continente al que pertenece

Ejemplo de registro:

Argentina,45376763,2780400,América

### Instrucciones de uso

1. Clonar el repositorio:
```text
git clone https://github.com/tharos625/prog1-tpi/
```

2. Ingresar al directorio del proyecto.
3. Ejecutar el programa:
```text
python3 tpi.py
```
4. Seleccionar una opción del menú.

### Funcionalidades
#### Alta de país

Permite registrar un nuevo país validando que:

* No existan campos vacíos.
* La población sea un número entero positivo.
* La superficie sea un número entero positivo.

#### Búsqueda de país

Permite buscar países por nombre mediante coincidencia exacta o parcial.

#### Actualización de datos

Permite modificar la población y superficie de un país existente.

#### Estadísticas

El sistema muestra:

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

#### Ejemplos de entrada y salida

Agregar país (opcion 1 del menú principal)

Entrada:

Nombre: Japón  
Población: 125800000  
Superficie: 377975  
Continente: Asia  

Salida:

País agregado correctamente.

Buscar país

Entrada:

Ingrese el país: arg

Salida:

Argentina  
Población: 45376763  
Superficie: 2780400  
Continente: América  
Estadísticas  

Salida:

País con mayor población: China  
País con menor población: Uruguay  
Promedio de población: 92458731  
Promedio de superficie: 1834521  
América: 4 países  
Europa: 3 países  
Asia: 5 países  

#### Participación de los integrantes
Integrante	Tareas realizadas
Nombre Apellido	Diseño y desarrollo del módulo de altas
Nombre Apellido	Implementación de búsquedas y filtros
Nombre Apellido	Estadísticas y documentación

#### Licencia

Proyecto realizado con fines educativos.
