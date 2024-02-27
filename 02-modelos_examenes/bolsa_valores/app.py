# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"""
nombre: Alejo
apellido: Tomkiewicz
---
'''
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de 
valores:

Para ello deberás programar el botón  para poder cargar 10 operaciones de compra con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    
Realizar los siguientes informes:
 
    #! 1) - Tipo de instrumento que menos se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion del usuario que invirtio menos dinero
    #! 6) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total

'''
"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Bolsa de valores")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        #A) Carga de operación de compra
        contador_operacion_compra = 0
        
        while (contador_operacion_compra < 3):
            nombre = input("Ingrese su nombre: ")

            monto = input("Ingrese el monto en pesos de la operación (no menor a $10000): ")
            monto = int(monto)
            if (monto < 10000):
                monto = input("Reingrese el monto en pesos de la operación (no menor a $10000): ")
                monto = int(monto)

            tipo_instrumento = input("Ingrese el tipo de instrumento: CEDEAR - BONOS - MEP: ")
            if (tipo_instrumento != "CEDEAR" and tipo_instrumento != "BONOS" and tipo_instrumento != "MEP"):
                tipo_instrumento = input("Reingrese el tipo instrumento: CEDEAR - BONOS - MEP: ")

            cantidad_instrumentos = input("Ingrese la cantidad de instrumentos: ")
            cantidad_instrumentos = int(cantidad_instrumentos)
            if (cantidad_instrumentos == 0):
                cantidad_instrumentos = input("Reingrese la cantidad de instrumentos: ")
                cantidad_instrumentos = int(cantidad_instrumentos)

            contador_operacion_compra += 1
            operacion_de_compra = print(f"Operación número {contador_operacion_compra}: {nombre} {monto} {tipo_instrumento} {cantidad_instrumentos}")
   

if __name__ == "__main__":
    app = App()
    app.mainloop()
