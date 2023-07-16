class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def __str__(self) -> str:
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    
    def __str__(self) -> str:
        return super().__str__() + f" {self.velocidad}, {self.cilindraje} cc"

class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindraje, peso_carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindraje)
        self.peso_carga = peso_carga 

    def __str__(self) -> str:
        return super().__str__() + f" {self.peso_carga}"
    
class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindraje, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindraje)
        self.nro_puestos = nro_puestos
    
    def __str__(self) -> str:
        return super().__str__() + f" {self.nro_puestos}"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo_bicicleta = tipo_bicicleta

    def __str__(self) -> str:
        return super().__str__() + f" {self.tipo_bicicleta}"
    
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo_bicicleta, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, nro_ruedas, tipo_bicicleta)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor 

    def __str__(self) -> str:
        return super().__str__() + f" {self.nro_radios} radios, {self.cuadro}, {self.motor}"