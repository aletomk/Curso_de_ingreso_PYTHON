import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alejo
apellido: Tomkiewicz
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_numero_positivo = 0
        suma_numero_negativo = 0
        contador_positivo = 0
        contador_negativo = 0
        contador_ceros = 0

        while True:
            numero_ingresado = prompt("Números", "Ingrese un número: ")

            if (numero_ingresado == None):
                break

            numero_ingresado = int(numero_ingresado)

            if (numero_ingresado > 0):
                suma_numero_positivo += numero_ingresado
                contador_positivo += 1
            elif (numero_ingresado < 0):
                suma_numero_negativo += numero_ingresado
                contador_negativo += 1
            else:
                contador_ceros += 1

        diferencia_positivo_negativo = suma_numero_positivo - suma_numero_negativo
        
        mensaje = f"Suma acumulada de los positivos: {suma_numero_positivo}; Suma acumulada de los negativos: {suma_numero_negativo}; Cantidad de números positivos: {contador_positivo}; Cantidad de números negativos: {contador_negativo}; Cantidad de ceros: {contador_ceros}; Diferencia entre positivos y negativos {diferencia_positivo_negativo}"

        alert("Resultados", mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
