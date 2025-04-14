from laptop_business import Laptop_Empresarial
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class App2:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes = [
            "C:\\Users\\darck\\Documents\\Krakedev\\Programacion_Brandon-modulo5\\POO\\Clases\\img\\dell.jpg",
            "C:\\Users\\darck\\Documents\\Krakedev\\Programacion_Brandon-modulo5\\POO\\Clases\\img\\hp.jpg",
            "C:\\Users\\darck\\Documents\\Krakedev\\Programacion_Brandon-modulo5\\POO\\Clases\\img\\huawei.jpg",
            "C:\\Users\\darck\\Documents\\Krakedev\\Programacion_Brandon-modulo5\\POO\\Clases\\img\\lenovo.jpg"
        ]

        root.title("Ingresar datos")

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text = "Marca").grid(row=0,column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)

        ttk.Label(self.root, text = "Procesador").grid(row=1,column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1,column=1)

        ttk.Label(self.root, text = "Memoria").grid(row=2,column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column=1)

        ttk.Label(self.root, text = "Almacenamiento").grid(row=3,column=0)
        self.almacenamiento = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento).grid(row=3, column=1)
        
        ttk.Label(self.root, text = "Duracion Bateria").grid(row=4,column=0)
        self.duracion = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.duracion).grid(row=4, column=1)
        
        ttk.Label(self.root, text = "Precio").grid(row=5,column=0)
        self.precio = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio).grid(row=5, column=1)

        ttk.Button(self.root, text = "Agregar Laptop", command=self.agregar_laptop).grid(row=6,column=1)

        self.mostras_laptops = tk.Text(self.root, height=10, width=50)
        self.mostras_laptops.grid(row=7,column=0, columnspan=2)

        self.canva = tk.Canvas(self.root, width=300, height=200)
        self.canva.grid(row=1, column=3,rowspan=6)
    
    def agregar_laptop(self):
        nueva_laptop = Laptop_Empresarial(self.marca.get(), self.procesador.get(), self.memoria.get(), self.almacenamiento.get(), self.duracion.get(), self.precio.get())
        self.laptops.append(nueva_laptop)

        self.mostras_laptops.insert(tk.END, f"{nueva_laptop}")

        self.mostras_imagen_aleatoria()

    def mostras_imagen_aleatoria(self):
        imagen_path = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((300,200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0,0, anchor=tk.NW, image = photo)
        self.canva.image = photo

        pass

root = tk.Tk()

app = App2(root)
root.mainloop()