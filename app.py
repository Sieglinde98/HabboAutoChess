import os, math


from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
from flask import Flask, flash, render_template, request, send_from_directory
from flask_session import Session

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
"""
1. El programa solo se puede ejecutar siempre que la partida haya empezado
dentro de la sala.
    - Hay que poner un receptor de cambios de variable web para detectar el
    comienzo.
2. Recibe entrada desde la sala, ya sea haciendo clic sobre una pieza,
ya sea haciendo clic sobre ella para seleccionarla y desplegar los movi-
mientos legales, o para realizar un movimiento o una coronación.
    - El imput leído activa una función dependiendo de la pieza seleccionada
    para mostrar fichas para los movimientos legales de cada pieza.
    - Envía una ruta a la api web de la pieza seleccionada para modificar las
    variables de los furnis de alrededor.
    - Esperar en esta parte hasta que se haga clic en variable objetivo para
    realizar un movimiento.
3. Se hace clic en una variable objetivo
    3.1 Comprueba si ha hecho jaque mate y lee la notación de la casilla objetivo
        - Quita variable blanca de las "blancas" para que no haga clic en dos 
        baldosas "objetivo" rápidamente.
        - Quitar "pieza_blanca" de la casilla seleccionada y la añade a la casilla
        objetivo.
        - Compruebo las variables de la casilla seleccionada y actualizo las variables
        de la casilla seleccionada y del tablero.
        - Compruebo la variable "jaque" y, si da positivo, compruebo las variables
        de piezas del equipo contrario para conocer el Número de movimientos legales,
        si no los hay, es mate.
            3.1.1 Devuelvo la variable blanca al jugador sin variable y activo ganador.
            -
    3.2 Almacena el movimiento y el ganador, si lo hay, en una base de datos y guardar
    la partida con un identificador en otra base de datos.
        - Enviamos la base de datos de la partida jugada a Irwin, para que compruebe
        si el ganador ha usado bots para ganar.
        - Si no hay fraude, devuelve la variable ganador y activa el premio en base.
        - Añade la partida al historial de lichess o a la propia base de datos de
        la web.
        - Muestra el resultado final del tablero de la partida a la entrada de la web,
        tal y como se encuentra en la sala de juego.
        - Añadir la
2. 

""" 