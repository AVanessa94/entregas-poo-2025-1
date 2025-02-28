



class Producto:
    """Clase que modela un producto de la tienda."""
    
    def _init_(self, nombre: str, precio: int, cantidad: int):
        """
        Inicializa un producto con nombre, precio unitario y cantidad.
        
        :param nombre: Nombre del producto.
        :param precio: Precio unitario en COP.
        :param cantidad: Cantidad disponible en unidades.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def _str_(self):
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


if _name_ == "_main_":
    main()
