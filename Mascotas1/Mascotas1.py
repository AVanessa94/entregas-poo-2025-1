from datetime import datetime

class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().isoformat()

    def obtener_datos(self):
        return [self.__class__.__name__, self.nombre, f"{self.edad} años", self.raza, self.fecha_ingreso]

class Perro(Mascota):
    pass

class Gato(Mascota):
    pass

def ingresar_mascota():
    while True:
        tipo = input("Mascota, que clase es (P)erro o (G)ato? ").strip().lower()
        if tipo in ['p', 'g']:
            break
        print("Opción inválida. Intente de nuevo.")
    
    nombre = input("Cual es el nombre de la mascota? ").strip()
    edad = int(input(f"Que edad tiene '{nombre}'? ").strip())
    raza = input(f"De que raza es '{nombre}'? ").strip()
    
    if tipo == 'p':
        return Perro(nombre, edad, raza)
    else:
        return Gato(nombre, edad, raza)

def main():
    mascotas = []
    cantidad = int(input("Cuantas mascotas va a ingresar? ").strip())
    
    for i in range(1, cantidad + 1):
        print(f"Mascota {i}:")
        mascotas.append(ingresar_mascota())
    
    print("\nResumen:")
    print("|Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
    print("-" * 75)
    for mascota in mascotas:
        print(f"|{mascota.obtener_datos()[0]:<6}|{mascota.obtener_datos()[1]:<9}|{mascota.obtener_datos()[2]:<6}|{mascota.obtener_datos()[3]:<13}|{mascota.obtener_datos()[4]:<24}|")

if __name__ == "__main__":
    main()
