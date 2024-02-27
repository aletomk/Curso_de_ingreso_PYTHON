import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        seguir = True

        menor_edad_RV_RA = 0
        menor_edad_RV_RA = int(menor_edad_RV_RA)
        nombre_menor_edad_RV_RA = 0
        genero_menor_edad_RV_RA = 0

        contador_masculino = 0
        contador_femenino = 0
        contador_otro = 0

        contador_IA = 0
        contador_IOT = 0
        contador_RV_RA = 0

        contador_masculino_IOT_IA = 0
        contador_edad_especifica_IOT = 0
        contador_edad_femenino_IA = 0

        acumulador_edad_femenino_IA = 0
        acumulador_edad_femenino_IA = int(acumulador_edad_femenino_IA)

        while seguir == True:
            nombre = input("Ingrese su nombre: ")

            edad = input("Ingrese su edad: ")
            edad = int(edad)
            while (edad < 18):
                edad = input("Reingrese su edad: ")
                edad = int(edad)

            genero = input("Ingrese su género (Masculino - Femenino - Otro): ")
            while (genero != "Masculino" and genero != "Femenino" and genero != "Otro"):
                genero = input("Reingrese su género (Masculino - Femenino - Otro): ")

            tecnologia = input("Ingrese la tecnologia (IA, RV/RA, IOT): ")
            while (tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT"):
                tecnologia = input("Reingrese la tecnologia (IA, RV/RA, IOT): ")

            #Procesamiento de datos
            if (genero == "Masculino"):
                contador_masculino += 1
                if (tecnologia == "IOT" or tecnologia == "IA") and (edad > 24 and edad < 51):
                    contador_masculino_IOT_IA += 1

            if (genero == "Femenino"):
                contador_femenino += 1
                if (tecnologia == "IA"):
                    acumulador_edad_femenino_IA += edad
                    contador_edad_femenino_IA += 1
            
            if (genero == "Otro"):  
                contador_otro += 1        

            if (tecnologia == "IA"):   
                contador_IA += 1

            if (tecnologia == "IOT"):
                contador_IOT += 1
                if (edad > 17 and edad < 26) or (edad > 32 and edad < 43):
                    contador_edad_especifica_IOT += 1

            if (tecnologia == "RV/RA"):
                contador_RV_RA += 1 
                if (menor_edad_RV_RA == 0 or edad < menor_edad_RV_RA):
                    menor_edad_RV_RA = edad
                    nombre_menor_edad_RV_RA = nombre
                    genero_menor_edad_RV_RA = genero

            seguir = question("Seguir", "Desea continuar?")

    #Procesamiento de datos fuera del bucle
        #1) Cantidad masculinos entre 25 y 50 - IOT o IA
        if (contador_masculino_IOT_IA == 0):
            informe_uno = f"Ningún empleado masculino cuya edad este entre 25 y 50 años votó por IOT o IA"
        else:
            informe_uno = f"Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive: {contador_masculino_IOT_IA}."
        print(informe_uno)

        #2) Tecnología más votada
        if (contador_IA > contador_IOT and contador_IA > contador_RV_RA):
            informe_dos = f"La tecnología más votada fue: IA."
        elif (contador_IOT > contador_RV_RA):
            informe_dos = f"La tecnología más votada fue: IOT."
        else:
            informe_dos = f"La tecnología más votada fue: RV/RA."
        print(informe_dos)

        #3) Porcentaje género empledos
        cantidad_empleados = contador_masculino + contador_femenino + contador_otro 
        porcentaje_masculino = (contador_masculino / cantidad_empleados) * 100
        porcentaje_femenino = (contador_femenino / cantidad_empleados) * 100
        porcentaje_otro = (contador_otro / cantidad_empleados) * 100

        informe_tres = f"Del total de empleados, {int(porcentaje_masculino)}% son masculinos, {int(porcentaje_femenino)}% son femeninos y un {int(porcentaje_otro)}% otro."
        print(informe_tres)

        #4) Empleados entre 18 y 24 o 33 y 42 - IOT
        if (contador_IOT == 0):
            informe_cuatro = f"Ningún empleado votó por IOT"
        else:
            porcentaje_edad_especifica_IOT = (contador_edad_especifica_IOT / cantidad_empleados) * 100
            porcentaje_edad_especifica_IOT = int(porcentaje_edad_especifica_IOT)
            informe_cuatro = f"El {porcentaje_edad_especifica_IOT}% de los empleados cuya edad se encuentre entre 18 y 25 o entre 33 y 42, votaron por IOT."
        print(informe_cuatro)

        #5) Votos femenino - IA
        if (acumulador_edad_femenino_IA == 0 or contador_edad_femenino_IA == 0):
            informe_cinco = f"No hubo empleados de género Femenino que votaron por IA."
        else:
            promedio_edad_femenino_IA = acumulador_edad_femenino_IA / contador_edad_femenino_IA
            promedio_edad_femenino_IA = int(promedio_edad_femenino_IA)
            informe_cinco = f"Promedio de edad de los empleados de género Femenino que votaron por IA: {promedio_edad_femenino_IA}."
        print(informe_cinco)

        #6) Más joven en votar - RV/RA
        if (contador_RV_RA == 0):
            informe_seis = f"Ningún empleado votó por RV/RA"
        else:
            informe_seis = f"{nombre_menor_edad_RV_RA} de género {genero_menor_edad_RV_RA} fue la persona más joven que votó por RV/RA."
        print(informe_seis)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
