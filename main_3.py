from clases import Vehiculo, Automovil, Bicicleta, Motocicleta, Particular, Carga
import csv

def guardar_datos_csv(nombre_archivo, datos):
    try:
        with open(nombre_archivo, "w", newline="") as archivo:
            archivo_csv = csv.writer(archivo)
            archivo_csv.writerows(datos)
        print(f"Datos guardados en el archivo '{nombre_archivo}'.")
    except IOError as err:
        print(f"Error al guardar los datos en el archivo '{nombre_archivo}': {str(err)}")

def leer_datos_csv(nombre_archivo):
    datos = []
    try:
        with open(nombre_archivo, "r") as archivo:
            archivo_csv = csv.reader(archivo)
            for descripcion, atributos in archivo_csv:
                datos.append((descripcion, eval(atributos)))  # Evaluate the string representation to convert it back to a dictionary
    except IOError as err: #why IOError? bc thats the result of incorrect file name or location
        print(f"Error al leer los datos del archivo '{nombre_archivo}': {str(err)}")
    return datos

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 58", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

# Convert the class instances to a list of tuples with the desired output format
datos = [
    ("Lista de Vehiculos Particular", particular.__dict__),
    ("Lista de Vehiculos Carga", carga.__dict__),
    ("Lista de Vehiculos Bicicleta", bicicleta.__dict__),
    ("Lista de Vehiculos Motocicleta", motocicleta.__dict__)
]

guardar_datos_csv("vehiculos.csv", datos)
automoviles = leer_datos_csv("vehiculos.csv")
for automovil in automoviles:
    print(automovil)