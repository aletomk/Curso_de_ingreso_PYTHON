import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alejo
apellido: Tomkiewicz
---
TP: Iluminación
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad = self.combobox_cantidad.get()
        cantidad = int(cantidad)

        precio = 800
        descuento = 0
        total = precio * cantidad

        mensaje_adicional = ""
        mensaje_descuento = "No obtuviste descuento"

        match (marca):
            case "ArgentinaLuz":
                if (cantidad == 5):
                    descuento_marca = 0.6
                elif (cantidad == 4):
                    descuento_marca = 0.75
                elif (cantidad == 3):
                    descuento_marca = 0.85

            case "FelipeLamparas":
                if (cantidad == 5):
                    descuento_marca = 0.7
                elif (cantidad == 4):
                    descuento_marca = 0.75
                elif (cantidad == 3):
                    descuento_marca = 0.9

            case "Jeluz" | "HazIluminacion" | "Osram":
                if (cantidad == 5):
                    descuento_marca = 0.7
                elif (cantidad == 4):
                    descuento_marca = 0.8
                elif (cantidad == 3):
                    descuento_marca = 0.05

        if (cantidad >= 6):
            descuento_marca = 0.5
        elif (cantidad <= 2):
            descuento_marca = 1

        total_final = total * descuento_marca
        descuento = total - total_final
        
        if total_final > 4000:
            descuento_adicional = total_final * 0.05
            total_final = total_final - descuento_adicional
            mensaje_adicional = f"Te cobramos un 5% menos (${descuento_adicional}) por gastar más de $4.000."

        if cantidad > 2:
            mensaje_descuento = f"Obtuviste un descuento de ${descuento}"

        mensaje = f"El total de su compra es ${total_final}. {mensaje_descuento}. {mensaje_adicional}"
        
        alert("Resúmen de compra", mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()