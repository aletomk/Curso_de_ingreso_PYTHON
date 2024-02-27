import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
nombre: Alejo
apellido: Tomkiewicz
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt y si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self): 
        numero_aleatorio = random.randint(1, 100)     
        limite_intentos = 7
        contador_intentos = 1

        for _ in range(1, limite_intentos):
            numero_ingresado = prompt("Número", "Ingrese un número: ")
            numero_ingresado = int(numero_ingresado)
            
            if (numero_ingresado != numero_aleatorio):
                if (numero_ingresado < numero_aleatorio):
                    alert("Adivina el número","Falta...")
                else:
                    alert("Adivina el número","Se pasó...")
            elif (numero_ingresado == numero_aleatorio):
                if (contador_intentos == 1):
                    alert("Adivina el número","Usted es un psíquico")
                    break
                elif (contador_intentos == 2):
                    alert("Adivina el número","Excelente percepción")
                    break
                elif (contador_intentos == 3):
                    alert("Adivina el número","Esto es suerte")
                    break
                elif (contador_intentos < 7):
                    alert("Adivina el número","Excelente técnica")
                    break
                else:
                    alert("Adivina el número","Perdiste, suerte para la próxima")
                    break

            contador_intentos += 1
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()