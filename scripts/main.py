import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from PIL import Image, ImageTk
import tkinter as tk
import csv

# Configurar el lector RFID
reader = SimpleMFRC522()

def buscar_asiento(id_tarjeta):
    with open('../data/asientos.csv', newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile)
        for fila in lector:
            if int(fila['ID_tarjeta']) == id_tarjeta:
                return fila['Asiento']
    return "No encontrado"

def mostrar_imagen_mesa(asiento):
    if asiento != "No encontrado":
        ruta_imagen = f"../images/{asiento}.png"  # Ruta de la imagen de la mesa
    else:
        ruta_imagen = "../images/todas_mesas.png"  # Imagen base

    ventana = tk.Tk()
    ventana.title("Asignación de Asiento")

    # Cargar y mostrar la imagen
    imagen = Image.open(ruta_imagen)
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
    etiqueta_imagen.pack()

    ventana.mainloop()

try:
    print("Por favor, acerque la tarjeta al lector...")
    id_tarjeta, texto = reader.read()
    print(f"ID de tarjeta leído: {id_tarjeta}")

    # Buscar el asiento
    asiento = buscar_asiento(id_tarjeta)
    print(f"Asiento asignado: {asiento}")

    # Mostrar la imagen de la mesa
    mostrar_imagen_mesa(asiento)

finally:
    GPIO.cleanup()
