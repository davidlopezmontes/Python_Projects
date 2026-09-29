matriz = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

tablero = matriz.copy()

jugadores = ["Player1", "Player2"]

fichas = ["X", "O"]

coordenadasValidas = ["0", "1", "2"]

finJuego = False


# Función para reiniciar o tablero cando empeza unha nova partida
def reiniciarTablero(tablero):
  for fila in range(3):
    for columna in range(3):
      tablero[fila][columna] = "*"


def imprimirTablero(matriz):
  #for fila in matriz:
  #print(fila)

  print(matriz[0][0] + ' | ' + matriz[0][1] + ' | ' + matriz[0][2])
  print(matriz[1][0] + ' | ' + matriz[1][1] + ' | ' + matriz[1][2])
  print(matriz[2][0] + ' | ' + matriz[2][1] + ' | ' + matriz[2][2])
  print(" ")


# Función para comprobar se a coordenada introducida é válida
def comprobarCoordenada():
  while True:

    valorX = input("Introduce una fila " + jugador + ":")
    valorY = input("Introduce una columna " + jugador + ":")
    print(" ")
    print(valorX + " " + valorY)
    print(" ")

    # Hai que comprobar primeiro se os valores introducidos son numeros
    # pq despois no elif non pode transformar unha letra nun int
    if valorX not in coordenadasValidas or valorY not in coordenadasValidas:
      print("Coordenada no válida :v")
    # Ahora esto sobra pq xa puxen unhas coordenadas concretas q son válidas
    elif int(valorX) > 2 or int(valorY) > 2 or int(valorX) < 0 or int(
        valorY) < 0:
      print("Estás fuera del tablero :O")
    # Comprobar se a posición está ocupada
    elif tablero[int(valorX)][int(valorY)] != "*":
      print("Posición ocupada :(")
    # Poñer ficha na coordenada introducida
    else:
      tablero[int(valorX)][int(valorY)] = ficha
      break

def tableroLLeno(tablero):
  global finJuego
  if all(elem != "*" for fila in tablero for elem in fila):
    print("Empate :/")
    finJuego = True


while True:

  reiniciarTablero(tablero)
  imprimirTablero(tablero)

  # bucle para xogar turnos ata que haxa ganador ou empaten
  while True:

    if finJuego is True:

      continuarBucle = True
      while (continuarBucle):

        confirmar = input("¿Jugar otra partida? (s/n): ")

        try:
          confirmarValido = str(confirmar)

          if confirmarValido == "s":
            finJuego = False
            print(" ")
            print("Comienza la partida")
            print(" ")
            reiniciarTablero(tablero)
            imprimirTablero(tablero)

          elif confirmarValido == "n":
            exit()
          continuarBucle = False

        except ValueError:
          break

    for jugador in jugadores:

      if finJuego is True:
        break

      ficha = fichas[0] if jugador == "Player1" else fichas[1]
      print("Turno de " + jugador)

      comprobarCoordenada()
      tableroLLeno(tablero)

      for fila in tablero:
        # Comprobar se a fila ten os 3 elementos iguales
        if fila[0] == fila[1] == fila[2]:
          # Comprobas o elemento que ganou
          if fila[0] == fichas[0]:
            print("Gana jugador " + jugadores[0] + " por filas.")
            finJuego = True
            break
          elif fila[0] == fichas[1]:
            print("Gana jugador " + jugadores[1] + " por filas.")
            finJuego = True
            break

      # Comprobar se a columna ten os 3 elementos iguales
      for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna]:
          # Comprobas o elemento que ganou
          if tablero[0][columna] == fichas[0]:
            print("Gana jugador " + jugadores[0] + " por columnas.")
            finJuego = True
            break
          elif tablero[0][columna] == fichas[1]:
            print("Gana jugador " + jugadores[1] + "por columnas.")
            finJuego = True
            break

      # Comprobar se a diagonal ten os 3 elementos iguales
      if tablero[0][0] == tablero[1][1] == tablero[2][2]:
        if tablero[0][0] == fichas[0]:
          print("Gana jugador " + jugadores[0] + " por diagonales.")
          finJuego = True
        elif tablero[0][0] == fichas[1]:
          print("Gana jugador " + jugadores[1] + " por diagonales.")
          finJuego = True

      if tablero[0][2] == tablero[1][1] == tablero[2][0]:
        if tablero[0][2] == fichas[0]:
          print("Gana jugador " + jugadores[0] + " por diagonales.")
          finJuego = True
        elif tablero[0][2] == fichas[1]:
          print("Gana jugador " + jugadores[1] + " por diagonales.")
          finJuego = True

      imprimirTablero(tablero)
