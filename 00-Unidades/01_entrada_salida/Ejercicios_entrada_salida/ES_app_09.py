import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alejo
apellido: Tomkiewicz
---
Ejercicio: entrada_salida_09
---
Enunciado:
Al presionar el botón 'Calcular', se deberá obtener el valor contenido en la caja de texto (txtSueldo), 
transformarlo a número y mostrar el importe de sueldo actualizado con el incremento del 15% utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        sueldo = self.txt_sueldo.get()
        sueldo = int(sueldo)

        sueldo_final = sueldo * 1.15 #0.15 seria lo mismo que hacer regla de 3 simple. 1.15 ahorra la suma del 15% al valor total ----> (sueldo_final = sueldo + aumento_sueldo_15)

        alert("Sueldo", f"Tu sueldo es : ${"%.2f" % sueldo_final}") #"%.2f" % --> %f se usa para dar formato a valores flotantes, debe estar entre comillas y separado del flotante por el operador de módulo. El número entre % y f (2 en este caso) le indica que tiene que redondear el número a 2 decimales
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()