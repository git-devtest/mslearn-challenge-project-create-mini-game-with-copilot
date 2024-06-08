# write 'hello world' to the console
# print('hello world')

# Crear el juego de Piedra, Papel o Tijera. Para la ejecución de este, usaremos las variables
# rock, paper y scissors para las opciones del juego. El usuario deberá elegir una de las opciones
# El jugador podrá elegir una de las tres opciones, rock, paper o scissors, y se le debería advertir 
# en caso de introducir una opción no válida.
# En cada ronda, el jugador debe entrar en una de las opciones de la lista y ser informado de si ganó, 
# perdió o empató con el oponente.
# Al final de cada ronda, el jugador elegirá si vuelve a jugar.
# Se debe mostrar la puntuación del jugador al final del juego.
# El minijuego debe controlar las entradas del usuario, colocarlas en minúsculas e informar al usuario 
# si la opción no es válida.

# Path: app.py
# importamos la librería random
import random

# Definimos las opciones del juego
rock = "rock"
paper = "paper"
scissors = "scissors"

# Definimos las opciones válidas
options = [rock, paper, scissors]

# Definimos la puntuación inicial
score = 0

# Definimos la función que nos permitirá jugar

def play():
    # Definimos la puntuación global
    global score

    # Definimos la elección del jugador
    player_choice = input("Elige rock, paper o scissors: ").lower()

    # Validamos la elección del jugador
    if player_choice not in options:
        print("Opción no válida")
        return

    # Definimos la elección del oponente
    opponent_choice = random.choice(options)

    # Mostramos la elección del oponente
    print(f"El oponente elige {opponent_choice}")

    # Definimos las condiciones de victoria
    if player_choice == rock and opponent_choice == scissors:
        print("Ganaste!")
        score += 1
    elif player_choice == paper and opponent_choice == rock:
        print("Ganaste!")
        score += 1
    elif player_choice == scissors and opponent_choice == paper:
        print("Ganaste!")
        score += 1
    elif player_choice == opponent_choice:
        print("Empate!")
    else:
        print("Perdiste!")

    # Mostramos la puntuación
    print(f"Puntuación: {score}")

# Definimos la función que nos permitirá jugar de nuevo
def play_again():
    return input("¿Quieres jugar de nuevo? (s/n): ").lower() == "s"

# Definimos el bucle principal
while True:
    play()
    if not play_again():
        break

# Mostramos la puntuación final
print(f"Puntuación final: {score}")

# Ejecutamos el juego
# python app.py