import tkinter as tk
from tkinter import *
import segno
from tkinterweb import HtmlFrame

def ventana_principal_configuracion(ventana_principal):
    # Configuración de la ventana principal
    ventana_principal.title("Buscador y generador de QR")
    ventana_principal.geometry('1920x1080')
    ventana_principal.resizable(False, False)

def capturar_busqueda(buscador, ventana_principal):
    # Capturar busqueda desde el entry
    informacion = buscador.get()
    informacion = "https://www." + informacion + ".com"

    # Generar la busqueda
    frame = HtmlFrame(ventana_principal, width=1000, height=600)
    frame.pack(fill="both", expand=True)

    # Cargar URL
    frame.load_url(informacion)

    # Crear un código QR con el contenido deseado
    qr = segno.make(informacion)

    # Guardar el código QR en formato PNG
    qr.save('codigo_qr.png', scale=10)


def generador_buscador_web(ventana_principal):
    # Encabezado del buscador
    Label(ventana_principal, text="Barra de navegación", font='Arial, 17').place(x=800, y=50)

    # Entrada de la busqueda
    buscador_web = StringVar()
    buscador = Entry(ventana_principal, width=25, textvariable=buscador_web)
    buscador.place(x=800 , y=150)

    # Boton de busqueda
    Button(ventana_principal, text="Buscar", width=5, height=1, command=lambda: capturar_busqueda(buscador, ventana_principal)).place(x=1100, y=150)

def main():
    # Inicialización ventana principal
    ventana_principal = tk.Tk()
    ventana_principal_configuracion(ventana_principal)
    generador_buscador_web(ventana_principal)
    ventana_principal.mainloop()

if __name__ == '__main__':
    main()
