import tkinter as tk
from tkinter import messagebox

class SaludoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Saludo en GUI")

        # Label para indicar qué dato ingresar
        self.label = tk.Label(root, text="Ingrese su nombre:")
        self.label.pack(pady=10)

        # Entry para ingresar el nombre
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        # Botón para saludar
        self.btn_saludar = tk.Button(root, text="Saludar", command=self.saludar)
        self.btn_saludar.pack(pady=5)

        # Botón para salir
        self.btn_salir = tk.Button(root, text="Salir", command=root.quit)
        self.btn_salir.pack(pady=5)

    def saludar(self):
        nombre = self.entry.get().strip()
        if nombre:
            messagebox.showinfo("Saludo", f"Hola {nombre}")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un nombre")

if __name__ == "__main__":
    root = tk.Tk()
    app = SaludoApp(root)
    root.mainloop()
