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
        #Inicialización de variables
        seguir = True

        contador_ruleta = 0
        contador_poker = 0
        contador_tragamonedas = 0
        contador_ganadores = 0
        contador_dinero_tragamonedas_ruleta = 0
        acumulador_dinero_ruleta = 0
        acumulador_dinero_poker = 0
        acumulador_dinero_tragamonedas = 0
        acumulador_dinero_total = 0
        acumulador_dinero_tragamonedas_ruleta = 0
        maximo_importe_ganado = 0

        while seguir:
        #Ingreso y validación de datos
            nombre = input("Ingrese su nombre: ")

            importe_ganado = input("Ingrese el importe ganado (SIN $): ")
            importe_ganado = int(importe_ganado)
            while (importe_ganado < 1000):
                importe_ganado = input("Error: el importe debe ser mayor o igual a $1000. Reingrese el importe ganado (SIN $): ")
                importe_ganado = int(importe_ganado)

            genero = input("Ingrese su género (Femenino - Masculino - Otro): ")
            while (genero != "Femenino" and genero != "Masculino" and genero != "Otro"):
                genero = input("Reingrese su género (Femenino - Masculino - Otro): ")

            juego = input("Ingrese el juego (Ruleta - Poker - Tragamonedas): ")
            while (juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas"):
                juego = input("Reingrese el juego (Ruleta - Poker - Tragamonedas): ")

        #Procesamiento de datos
            match(juego):
                case "Ruleta":
                    contador_ruleta += 1
                    acumulador_dinero_ruleta += importe_ganado
                case "Poker":
                    contador_poker += 1
                    acumulador_dinero_poker += importe_ganado
                case "Tragamonedas":
                    contador_tragamonedas += 1  
                    acumulador_dinero_tragamonedas += importe_ganado  

            if (contador_ganadores == 0):
                maximo_importe_ganado = importe_ganado
                nombre_maximo_ganador = nombre
                genero_maximo_ganador = genero
            else:
                if (maximo_importe_ganado < importe_ganado):
                    maximo_importe_ganado = importe_ganado
                    nombre_maximo_ganador = nombre
                    genero_maximo_ganador = genero

            if (juego != "Poker" and importe_ganado > 15000):
                acumulador_dinero_tragamonedas_ruleta += importe_ganado
                contador_dinero_tragamonedas_ruleta += 1
            
            contador_ganadores += 1
            acumulador_dinero_total += importe_ganado
            seguir = question("Seguir", "¿Desea continuar?")
        
        #Procesamiento de datos fuera del bucle
        mensaje = f"{nombre_maximo_ganador} de género {genero_maximo_ganador} fue la persona que más ganó."
        informe_uno = mensaje

        promedio_dinero_ruleta = acumulador_dinero_ruleta / contador_ruleta
        mensaje = f"Promedio de dinero ganado en Ruleta: ${int(promedio_dinero_ruleta)}."
        informe_dos = mensaje

        porcentaje_jugadores_tragamonedas = (contador_tragamonedas * 100) / contador_ganadores
        mensaje = f"{int(porcentaje_jugadores_tragamonedas)}% de las personas jugaron en el Tragamonedas."
        informe_tres = mensaje

        if (contador_ruleta < contador_poker and contador_ruleta < contador_tragamonedas):
            mensaje = f"La ruleta es el juego menos elegido por los ganadores."
        elif (contador_poker < contador_tragamonedas):
            mensaje = f"El poker es el juego menos elegido por los ganadores."
        else:
            mensaje = f"La máquina tragamonedas es el juego menos elegido por los ganadores."
        informe_cuatro = mensaje

        promedio_tragamonedas_ruleta = acumulador_dinero_tragamonedas_ruleta / contador_dinero_tragamonedas_ruleta
        mensaje = f"Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000: ${int(promedio_tragamonedas_ruleta)}."
        informe_cinco = mensaje

        porcentaje_dinero_ruleta = (acumulador_dinero_ruleta * 100) / acumulador_dinero_total
        porcentaje_dinero_poker = (acumulador_dinero_poker * 100) / acumulador_dinero_total
        porcentaje_dinero_tragamonedas = (acumulador_dinero_tragamonedas * 100) / acumulador_dinero_total
        mensaje = f"El Poker representó el {int(porcentaje_dinero_poker)}% del dinero egresado total, la Ruleta se llevó un {int(porcentaje_dinero_ruleta)}% y la máquina Tragamonedas el {int(porcentaje_dinero_tragamonedas)}% restante."
        informe_seis = mensaje
        
        #Informes
        print(f"INFORMES:\n{informe_uno}\n{informe_dos}\n{informe_tres}\n{informe_cuatro}\n{informe_cinco}\n{informe_seis}")
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()


