import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        menor_edad = 0
        nombre_menor_edad = 0

        contador_python = 0
        contador_net = 0
        contador_js = 0

        contador_genero_m = 0
        contador_genero_f = 0
        contador_genero_nb = 0

        contador_nb_net_js = 0
        contador_postulantes_jr = 0

        acumulador_edad_m = 0
        acumulador_edad_f = 0
        acumulador_edad_nb = 0
        
        for _ in range(1, 11):
        #Ingreso de datos y validaciones
            nombre = alert("Nombre", "ingrese su nombre: ")
            while (nombre == ""):
                nombre = alert("Nombre", "Reingrese su nombre: ")

            edad = alert("Edad", "Ingrese su edad: ")
            edad = int(edad)
            while (edad < 18):
                edad = alert("Edad", "Reingrese su edad: ")
                edad = int(edad)

            genero = alert("Género", "Ingrese su género (M - F - NB): ")
            while (genero != "M" and genero != "F" and genero != "NB"):
                genero = alert("Género", "Reingrese su género (M - F - NB): ")

            tecnologia = alert("Tecnología", "Ingrese la tecnología (PYTHON - JS - ASP.NET): ")
            while (tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET"):
                tecnologia = alert("Tecnología", "Reingrese la tecnología (PYTHON - JS - ASP.NET): ")    

            puesto = alert("Puesto", "Ingrese el puesto al que se postula (Jr - Ssr - Sr): ")
            while (puesto != "Jr" and puesto != "Ssr" and puesto != "Sr"):
                puesto = alert("Puesto", "Reingrese el puesto al que se postula (Jr - Ssr - Sr): ")

        #Procesamiento de datos
            #A) Postulantes Ssr NB para NET o JS entre 25 y 48 años
            if genero == "NB" and (tecnologia == "ASP.NET" or tecnologia == "JS") and (edad >= 25 and edad <= 40) and (puesto == "Ssr"):
                contador_nb_net_js += 1
            #B) Nombre menor edad de postulante JR
            if (puesto == "Jr"):
                contador_postulantes_jr += 1
                if (menor_edad == 0 or menor_edad < edad):
                    menor_edad = edad
                    nombre_menor_edad = nombre
            #C) Promedio de edad por género
            match (genero):
                case "M":
                    contador_genero_m += 1
                    acumulador_edad_m += edad
                case "F":
                    contador_genero_f += 1
                    acumulador_edad_f += edad
                case _:
                    contador_genero_nb += 1
                    acumulador_edad_nb += edad
            #D) Tecnología con más postulantes
            match (tecnologia):
                case "PYTHON":
                    contador_python += 1
                case "ASP.NET":
                    contador_net += 1
                case _:
                    contador_js += 1
    
    #Procesamiento de datos fuera del ciclo FOR
        #A)
        if (contador_nb_net_js == 0):
            informe_uno = f"NO hay postulantes Ssr para para NET o JS entre 25 y 48 años"
        else:
            informe_uno = f"Número de postulantes Ssr para para NET o JS entre 25 y 48 años: {contador_nb_net_js}"
        print(informe_uno)
        #B)
        if (contador_postulantes_jr == 0):
            informe_dos = f"NO hay postulantes en el puesto Jr"
        else:
            informe_dos = f"El postulante Jr más joven se llama {nombre_menor_edad}"
        print(informe_dos)
        #C)
        promedio_edad_m = acumulador_edad_m / contador_genero_m
        promedio_edad_f = acumulador_edad_f / contador_genero_f
        promedio_edad_nb = acumulador_edad_nb / contador_genero_nb
        informe_tres = f"El promedio de edad del género M es: {int(promedio_edad_m)}\nEl promedio de edad del género F es: {int(promedio_edad_f)}\nEl promedio de edad del género NB es: {int(promedio_edad_nb)}"
        print(informe_tres)
        #D)
        if (contador_python > contador_js and contador_python > contador_net):
            informe_cuatro = f"PYTHON es la tecnología con más postulantes: {contador_python}"
        elif (contador_js > contador_net):
            informe_cuatro = f"JS es la tecnología con más postulantes: {contador_js}"
        else:
            informe_cuatro = f"ASP.NET es la tecnología con más postulantes: {contador_net}"
        print(informe_cuatro)
        #E)
        porcentaje_m = (contador_genero_m / 10) * 100
        porcentaje_f = (contador_genero_f / 10) * 100
        porcentaje_nb = 100 - (porcentaje_m + porcentaje_f)

        informe_cinco = f"Un {int(porcentaje_m)}% de los postulantes son de género M\n Un {int(porcentaje_f)}% de género F\n El {int(porcentaje_nb)}% restante pertenece al género NB"
        print(informe_cinco)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
