class Producto:
    """Clase que modela un producto de la tienda."""
    
    def __init__(self, nombre: str, precio: int, cantidad: int):
        """
        Inicializa un producto con nombre, precio unitario y cantidad.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        """Devuelve una representación en texto del producto."""
        return f"|{self.nombre:<10} |{self.cantidad:<12} unidades |{self.precio:<10} pesos |"


def solicitar_producto(numero: int) -> Producto:
    """Solicita los datos de un producto al usuario y devuelve un objeto Producto."""
    nombre = input(f"> Producto {numero}, ¿cuál es el nombre?\n< ")
    precio = int(input(f"> ¿Cuál es el precio de '{nombre}'?\n< "))
    cantidad = int(input(f"> ¿Qué cantidad hay de '{nombre}'?\n< "))
    return Producto(nombre, precio, cantidad)


def main():
    """Función principal que gestiona la recolección y visualización de los productos."""
    productos = [solicitar_producto(i) for i in range(1, 4)]

    print("\n> Resumen:")
    print("> |Producto  |Cantidad      |Precio      |")
    print("> |" + "-"*38 + "|")
    for producto in productos:
        print("> " + str(producto))


if __name__ == "__main__":
    main()
