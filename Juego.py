import tkinter as tk
import random

# Opciones disponibles
opciones = ["Piedra", "Papel", "Tijera"]

# Puntuaciones
victorias = 0
derrotas = 0
empates = 0

def jugar(eleccion_jugador):
    global victorias, derrotas, empates

    eleccion_computadora = random.choice(opciones)
    resultado_texto.set(f"Computadora eligió: {eleccion_computadora}")

    if eleccion_jugador == eleccion_computadora:
        resultado = "Empate"
        empates += 1
    elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijera") or \
         (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or \
         (eleccion_jugador == "Tijera" and eleccion_computadora == "Papel"):
        resultado = "¡Ganaste!"
        victorias += 1
    else:
        resultado = "¡Perdiste!"
        derrotas += 1

    resultado_texto.set(f"{resultado}\nComputadora eligió: {eleccion_computadora}")
    puntuacion_texto.set(f"Ganadas: {victorias} - Perdidas: {derrotas} - Empates: {empates}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("300x200")
ventana.resizable(False, False)

# Variables de texto
resultado_texto = tk.StringVar()
puntuacion_texto = tk.StringVar()
resultado_texto.set("Haz tu elección:")
puntuacion_texto.set("Ganadas: 0 - Perdidas: 0 - Empates: 0")

# Etiquetas y botones
label_resultado = tk.Label(ventana, textvariable=resultado_texto, font=("Arial", 12))
label_resultado.pack(pady=10)

label_puntuacion = tk.Label(ventana, textvariable=puntuacion_texto, font=("Arial", 10))
label_puntuacion.pack(pady=10)

frame_botones = tk.Frame(ventana)
frame_botones.pack()

boton_piedra = tk.Button(frame_botones, text="Piedra", command=lambda: jugar("Piedra"), width=10)
boton_piedra.grid(row=0, column=0, padx=5)

boton_papel = tk.Button(frame_botones, text="Papel", command=lambda: jugar("Papel"), width=10)
boton_papel.grid(row=0, column=1, padx=5)

boton_tijera = tk.Button(frame_botones, text="Tijera", command=lambda: jugar("Tijera"), width=10)
boton_tijera.grid(row=0, column=2, padx=5)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
