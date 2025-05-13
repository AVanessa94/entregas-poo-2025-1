class Matriz:
    def __init__(self):
        self.valores = [[0, 0], [0, 0]]

    def leer_matriz(self, nombre="Matriz"):
        print(f"\nIntroduciendo valores para {nombre}:")
        for i in range(2):
            for j in range(2):
                while True:
                    entrada = input(f"{nombre}: elemento {i},{j}: ")
                    if entrada.lstrip("-").isdigit():
                        self.valores[i][j] = int(entrada)
                        break
                    else:
                        print("Entrada inválida. Por favor, ingrese un número entero.")

    def __add__(self, other):
        resultado = Matriz()
        for i in range(2):
            for j in range(2):
                resultado.valores[i][j] = self.valores[i][j] + other.valores[i][j]
        return resultado

    def __sub__(self, other):
        resultado = Matriz()
        for i in range(2):
            for j in range(2):
                resultado.valores[i][j] = self.valores[i][j] - other.valores[i][j]
        return resultado

    def __mul__(self, other):
        resultado = Matriz()
        for i in range(2):
            for j in range(2):
                resultado.valores[i][j] = (self.valores[i][0] * other.valores[0][j] +
                                           self.valores[i][1] * other.valores[1][j])
        return resultado

    def mostrar(self):
        for fila in self.valores:
            print(f"| {fila[0]}  {fila[1]} |")

def pedir_opcion():
    while True:
        print("\nEscriba:")
        print("1 para suma")
        print("2 para resta")
        print("3 para multiplicación")
        opcion = input("Seleccione una opción: ")
        if opcion in ['1', '2', '3']:
            return int(opcion)
        else:
            print("Opción inválida. Intente nuevamente.")

def main():
    print("=== CALCULADORA DE MATRICES 2x2 ===")
    matriz1 = Matriz()
    matriz2 = Matriz()

    matriz1.leer_matriz("Matriz 1")
    matriz2.leer_matriz("Matriz 2")

    print("\nMatriz 1:")
    matriz1.mostrar()

    print("\nMatriz 2:")
    matriz2.mostrar()

    opcion = pedir_opcion()

    if opcion == 1:
        resultado = matriz1 + matriz2
        print("\nLa suma de las dos matrices es:")
    elif opcion == 2:
        resultado = matriz1 - matriz2
        print("\nLa resta de las dos matrices es:")
    elif opcion == 3:
        resultado = matriz1 * matriz2
        print("\nLa multiplicación de las dos matrices es:")

    resultado.mostrar()

if __name__ == "__main__":
    main()
