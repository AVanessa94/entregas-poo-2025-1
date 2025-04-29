from datetime import datetime

# Clase base Visualizador
class Visualizador:
    def resumen(self):
        clase = self.__class__.__name__
        nombre = self.nombre
        edad = f"{self.edad} años"
        raza = self.raza.capitalize()
        fecha = self.fecha_ingreso.isoformat()
        return f"|{clase:<6}|{nombre:<9}|{edad:<7}|{raza:<13}|{fecha:<25}|"

# Clase base Mascota (no modificar)
class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now()

# Clase Perro, hereda de Mascota y Visualizador
class Perro(Mascota, Visualizador):
    pass

# Clase Gato, hereda de Mascota y Visualizador
class Gato(Mascota, Visualizador):
    pass

# Función principal
def main():
    mascotas = []
    cantidad = int(input("¿Cuántas mascotas va a ingresar?\n> "))

    for i in range(1, cantidad + 1):
        tipo = input(f"Mascota {i}, ¿qué clase es (P)erro o (G)ato?\n> ").strip().lower()
        while tipo not in ['p', 'g', 'perro', 'gato']:
            tipo = input("Por favor ingrese 'P' para Perro o 'G' para Gato.\n> ").strip().lower()
        
        nombre = input(f"¿Cuál es el nombre del {'Perro' if tipo[0] == 'p' else 'Gato'}?\n> ").strip()
        edad = int(input(f"¿Qué edad tiene '{nombre}'?\n> "))
        raza = input(f"¿De qué raza es '{nombre}'?\n> ").strip()

        if tipo[0] == 'p':
            mascota = Perro(nombre, edad, raza)
        else:
            mascota = Gato(nombre, edad, raza)

        mascotas.append(mascota)

    # Mostrar el resumen
    print("> Resumen:")
    print("|Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
    for mascota in mascotas:
        print(mascota.resumen())

if __name__ == "__main__":
    main()
