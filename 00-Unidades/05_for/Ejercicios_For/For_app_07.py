import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alejo
apellido: Tomkiewicz
---
Ejercicio: for_07
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt("Numero", "Ingrese un numero")
        numero = int(numero)
        bandera_divisor = False
                                    #SI NUMERO = 7
        for i in range(2, numero): # [2 - 3 - 4 - 5 - 6] 
            if (numero % i == 0): # 7 / numero de iteracion del rango. 7/2, 7/3 y su resto es 0
                bandera_divisor = True #encontró otro divisor ademas de si mismo y 1. #Cortar el ciclo for
                break
        if (bandera_divisor == False): #no encontró otro divisor que 1 y si mismo. Es primo
            print("Es primo")
        else:
            print("No es primo")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()