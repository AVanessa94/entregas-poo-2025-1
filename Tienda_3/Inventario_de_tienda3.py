# Código para el inventario Tienda3
class Producto:
    """
    Clase que representa un producto en la tienda.
    """


class Producto:
    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion

    def calcula_precio(self, cantidad):
        return self.precio * cantidad

    def inventario_precio(self):
        return self.precio * self.cantidad


class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_resumen(self):
        print("\nResumen:")
        print("| Producto  | Cantidad   | Precio     | Descripción   | Clasificación  | Total en inventario | Precio x5 unidades |")
        print("-" * 100)
        for p in self.productos:
            print(f"| {p.nombre.ljust(9)} | {str(p.cantidad).ljust(10)} | {str(p.precio).ljust(9)} | {p.descripcion[:15].ljust(13)} | {p.clasificacion.ljust(12)} | {str(p.inventario_precio()).ljust(17)} | {str(p.calcula_precio(5)).ljust(18)} |")

    def resumen_por_clasificacion(self):
        resumen = {}
        for p in self.productos:
            if p.clasificacion not in resumen:
                resumen[p.clasificacion] = 0
            resumen[p.clasificacion] += p.calcula_precio(5)

        print("\nPrecios por clasificación:")
        print("| Clasificación  | Precio     |")
        print("-" * 30)
        for clasificacion, total in resumen.items():
            print(f"| {clasificacion.ljust(13)} | {str(total).ljust(9)} |")


# --- 🚀 Programa Principal ---
tienda = Tienda()

num_productos = int(input("¿Cuántos productos va a ingresar?\n> "))

for i in range(1, num_productos + 1):
    print(f"\n> Producto {i}, ¿cuál es el nombre?")
    nombre = input("> ")

    print(f"> ¿Cuál es el precio de '{nombre}'?")
    precio = int(input("> "))

    print(f"> ¿Qué cantidad hay de '{nombre}'?")
    cantidad = int(input("> "))

    print(f"> Introduzca la descripción de '{nombre}':")
    descripcion = input("> ")

    print(f"> ¿Qué clasificación tiene '{nombre}'?")
    clasificacion = input("> ")

    tienda.agregar_producto(Producto(nombre, precio, cantidad, descripcion, clasificacion))

# Mostrar resultados
tienda.mostrar_resumen()
tienda.resumen_por_clasificacion()
