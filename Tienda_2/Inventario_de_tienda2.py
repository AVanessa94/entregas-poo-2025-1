# Código para el inventario Tienda2
class Producto:
    """
    Clase que representa un producto en la tienda.
    """
    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
        """
        Inicializa un producto con los atributos dados.
        :param nombre: Nombre del producto.
        :param precio: Precio unitario del producto.
        :param cantidad: Cantidad disponible del producto.
        :param descripcion: Descripción detallada del producto.
        :param clasificacion: Clasificación o categoría del producto.
        """
        self.nombre = nombre
        self.precio = float(precio)  # Asegurar que el precio sea flotante
        self.cantidad = int(cantidad)  # Asegurar que la cantidad sea entera
        self.descripcion = descripcion
        self.clasificacion = clasificacion
    
    def calcular_precio_total(self):
        """Calcula el precio total basado en la cantidad."""
        return self.precio * self.cantidad

def obtener_productos():
    """Genera una lista de productos sin usar input(), útil para GitHub Code."""
    productos = [
        Producto("SALCHICHA RANCHERA", 4500, 10, "SALCHICHA RANCHERA x3 marca RANCHERA", "alimentación"),
        Producto("Queso Mozzarella", 9400, 8, "QUESO MOZZARELLA TAJADO x400 GRS marca LATTI", "alimentación"),
        Producto("Tocino Carnudo", 10000, 12, "TOCINO CARNUDO x500 GRS marca REDCUT", "alimentación"),
        Producto("Yogurt Melocotón", 3000, 14, "Yogurt Alpina Melocotón x150 GRS", "alimentación"),
        Producto("Leche Deslactosada", 34000, 14, "Leche Colanta Deslactosada Semidescremada 1000 Ml X6 Unds", "alimentación")
    ]
    return productos

def ingresar_productos():
    """Permite al usuario ingresar productos manualmente."""
    productos = obtener_productos()
    cantidad_productos = int(input("¿Cuántos productos adicionales va a ingresar? "))
    
    for i in range(1, cantidad_productos + 1):
        print(f"\nProducto {i}, ¿cuál es el nombre?")
        nombre = input("> ")
        precio = float(input(f"¿Cuál es el precio de '{nombre}'? > "))
        cantidad = int(input(f"¿Qué cantidad hay de '{nombre}'? > "))
        descripcion = input(f"Introduzca la descripción de '{nombre}': > ")
        clasificacion = input(f"¿Qué clasificación tiene '{nombre}'? > ")
        productos.append(Producto(nombre, precio, cantidad, descripcion, clasificacion))
    
    return productos

def mostrar_resumen(productos):
    """Muestra el resumen de los productos ingresados."""
    print("\nResumen:")
    print(f"{'Producto':<20}{'Cantidad':<10}{'Precio':<10}{'Descripción':<30}{'Clasificación':<15}")
    print("=" * 90)
    
    for producto in productos:
        print(f"{producto.nombre:<20}{producto.cantidad:<10}{producto.precio:<10.2f}{producto.descripcion[:27]:<30}{producto.clasificacion:<15}")
    
    calcular_precio_por_clasificacion(productos)

def calcular_precio_por_clasificacion(productos):
    """Calcula y muestra el precio total por clasificación."""
    precios_por_clasificacion = {}
    
    for producto in productos:
        precio_total_producto = producto.calcular_precio_total()
        
        if producto.clasificacion in precios_por_clasificacion:
            precios_por_clasificacion[producto.clasificacion] += precio_total_producto
        else:
            precios_por_clasificacion[producto.clasificacion] = precio_total_producto
    
    print("\nPrecios por clasificación:")
    print(f"{'Clasificación':<20}{'Precio Total':<15}")
    print("=" * 35)
    
    for clasificacion, precio_total in precios_por_clasificacion.items():
        print(f"{clasificacion:<20}{precio_total:<15.2f}")

if __name__ == "__main__":
    productos = ingresar_productos()
    mostrar_resumen(productos)
