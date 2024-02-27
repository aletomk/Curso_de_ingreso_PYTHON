import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alejo
apellido: Tomkiewicz
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt("Número", "Ingrese un número")
        numero = int(numero)
        cantidad_primos = 0
                                    
        for i in range(1, numero + 1):
            contador_divisores = 0     #Se pone aca porque es necesario que se reinicie cada vez que se itera el for
            for a in range(1, i):
                if (i % a == 0):
                    contador_divisores += 1 
            if (contador_divisores < 2):
                cantidad_primos += 1
                print(i)
        
        mensaje = f"La cantidad de números primos es: {cantidad_primos}"
        print(mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()