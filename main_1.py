from clases import Vehiculo, Automovil, Bicicleta, Motocicleta, Particular, Carga

instancias = [] #lista vacia 


n = int(input("Cuantos vehiculos desea insertar: "))

for i in range (n):
    print(f"Datos del automóvil {i+1}")
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    nro_ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindraje = int(input("Inserte el cilindraje en cc: "))
    nro_puestos = int(input("Inserte el número de puestos: "))


    print("********************")
    auto = Automovil(marca, modelo, nro_ruedas, velocidad, cilindraje) #crear instancia con todo lo que se le pidio a persona
    instancias.append(auto) #instancias parte como lista vacia, pero al agregar auto se va agregando la info de cada uno

print("Imprimiendo por pantalla los Vehículos:")

for index, item in enumerate(instancias):
    print(f"Datos del automóvil {index + 1} : Marca {item.marca}, Modelo {item.modelo}, {item.nro_ruedas} ruedas {item.velocidad} Km/h, {item.cilindraje} cc")

