import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alejo
apellido: Tomkiewicz
---
Ejercicio: Simulacro Examen
---
Enunciado:
Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

    Nombre
    Importe ganado (mayor o igual $1000)
    Género (“Femenino”, “Masculino”, “Otro”)
    Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:
    Nombre y género de la persona que más ganó.
    Promedio de dinero ganado en Ruleta.
    Porcentaje de personas que jugaron en el Tragamonedas.
    Cuál es el juego menos elegido por los ganadores.
    Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
    Porcentaje de dinero en función de cada juego
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        pass


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()


