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
        #Inicialización de variables
        contador_usuarios = 0
        contador_mep = 0
        contador_bonos = 0
        contador_cedear = 0
        contador_usuarios_mep_50_200 = 0
        acumulador_instrumentos = 0
        acumulador_monto_pesos = 0
        acumulador_monto_cedear = 0
        acumulador_instrumentos_mep = 0

        for _ in range(10):
            #Ingreso y validación de datos
            nombre = input("Ingrese su nombre: ")

            monto_pesos = input("Ingrese el monto en pesos (SIN $): ")
            monto_pesos = int(monto_pesos)
            while (monto_pesos < 10000):
                monto_pesos = input("Error: El monto debe ser mayor a $10000. Reingrese el monto (SIN $): ")
                monto_pesos = int(monto_pesos)

            tipo_instrumento = input("Ingrese el tipo de instrumento (CEDEAR - BONOS - MEP): ")
            while (tipo_instrumento != "CEDEAR" and tipo_instrumento != "BONOS" and tipo_instrumento != "MEP"):
                tipo_instrumento = input("Reingrese el tipo de instrumento (CEDEAR - BONOS - MEP): ")

            cantidad_instrumentos = input("Ingrese la cantidad de instrumentos: ")
            cantidad_instrumentos = int(cantidad_instrumentos)
            while (cantidad_instrumentos < 1):
                cantidad_instrumentos = input("Error: Reingrese la cantidad de instrumentos: ")
                cantidad_instrumentos = int(cantidad_instrumentos)

            #Procesamiento de datos
            match(tipo_instrumento):
                case "CEDEAR":
                    if (contador_cedear == 0):
                        nombre_primer_usuario_cedear = nombre
                        inversion_primer_usuario_cedear = monto_pesos
                    acumulador_monto_cedear += monto_pesos    
                    contador_cedear += 1

                case "BONOS":
                    if (contador_bonos == 0):
                        nombre_primer_usuario_bonos = nombre
                        inversion_primer_usuario_bonos = monto_pesos
                    contador_bonos += 1

                case "MEP":
                    if (cantidad_instrumentos >= 50 and cantidad_instrumentos <= 200):
                        contador_usuarios_mep_50_200 += 1
                    acumulador_instrumentos_mep += cantidad_instrumentos    
                    contador_mep += 1
                    
            if (contador_usuarios == 0):
                minimo_monto_invertido = monto_pesos
                nombre_minimo_monto_invertido = nombre
            else:
                if (minimo_monto_invertido > monto_pesos):
                    minimo_monto_invertido = monto_pesos
                    nombre_minimo_monto_invertido = nombre
                
            contador_usuarios += 1
            acumulador_instrumentos += cantidad_instrumentos
            acumulador_monto_pesos += monto_pesos
        
        #Procesamiento de datos fuera del bucle
        if (contador_cedear < contador_bonos and contador_cedear < contador_mep):
            mensaje = f"El tipo de instrumento que menos se operó fue el CEDEAR"
        elif (contador_bonos < contador_mep):
            mensaje = f"El tipo de instrumento que menos se operó fueron los BONOS"
        else:
            mensaje = f"El tipo de instrumento que menos se operó fue el MEP"
        informe_uno = mensaje

        mensaje = f"Cantidad de usuarios que compraron entre 50  y 200 MEP: {contador_usuarios_mep_50_200}"
        informe_dos = mensaje

        cantidad_usuarios_no_cedear = contador_mep + contador_bonos
        mensaje = f"Cantidad de usuarios que no compraron CEDEAR: {cantidad_usuarios_no_cedear}"
        informe_tres = mensaje

        mensaje = f"{nombre_primer_usuario_bonos} fue la primera persona en comprar BONOS e invirtió ${inversion_primer_usuario_bonos}. Por otro lado {nombre_primer_usuario_cedear} fue la primera persona en comprar CEDEAR e invirtió ${inversion_primer_usuario_cedear}"
        informe_cuatro = mensaje

        mensaje = f"{nombre_minimo_monto_invertido} fue la persona que menos invirtió: ${minimo_monto_invertido}"
        informe_cinco = mensaje

        promedio_monto_cedear = acumulador_monto_cedear / contador_cedear
        mensaje = f"Promedio de dinero en CEDEAR ingresado en total: ${int(promedio_monto_cedear)}"
        informe_seis = mensaje

        promedio_instrumentos_mep = acumulador_instrumentos_mep / contador_mep
        mensaje = f"Promedio de cantidad de instrumentos MEP vendidos en total: {int(promedio_instrumentos_mep)}"
        informe_siete = mensaje

        #Informes
        print(f"INFORMES:\n{informe_uno}\n{informe_dos}\n{informe_tres}\n{informe_cuatro}\n{informe_cinco}\n{informe_seis}\n{informe_siete}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
