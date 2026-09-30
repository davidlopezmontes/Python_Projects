import random
from pathlib import Path

# Obtener la ruta dinámica del archivo palabras.txt
DIRECTORIO_ACTUAL = Path(__file__).parent
RUTA_TXT = DIRECTORIO_ACTUAL / "palabras.txt"

#Función para añadir un número de elementos a lista igual ao número
#de letras da p_adivinar
def añadir_posicion(lista):
  for _ in p_adivinar:
    lista.append("[]")


#Defino o número máximo de intentos
MAX_INTENTOS = 6
intentos = 0
#Bucle para que o xogador poida xogar unha nova partida ao acabar
while True:
  print("BIENVENIDO/A AL JUEGO WORDLE")
  print("Elige una opción")
  print("1. Jugar")
  print("2. Salir")

  opcion = input("Escribe el número de la opción que deseas:")

  lista_palabras = []

  n = 0
  # Juegar
  if opcion == "1":
    #Creo diccionario de palabras
    diccionario_palabras = {}

    #Leo o txt coas palabras
    archivo = open(RUTA_TXT, "r")

    lineas = archivo.readlines()

    archivo.close()

    #Añado os datos do txt ao diccionario_palabras
    for linea in lineas:
      #Separo a clave do valor
      clave, valor = linea.split(":")
      #Añado os elementos
      diccionario_palabras[clave] = valor.strip()

    #Elexir a dificulade
    print("Elige un nivel de dificultad")
    print("1. Fácil", "2. Media", "3. Difícil")
    dificultad = input("Escribe el número de dificultad:")
    print("Tienes 6 intentos")
    #Reseteo de intentos
    MAX_INTENTOS = 6
    intentos = 0

    #Dificultade fácil
    if dificultad == "1":
      print("Has elegido la dificultad fácil")
      for palabra, valor in diccionario_palabras.items():
        if valor == "4":
          n = 4
          #Añado as palabras coa dificulatade elixida a lista
          lista_palabras.append(palabra)
    if dificultad == "2":
      print("Has elegido la dificultad media")
      for palabra, valor in diccionario_palabras.items():
        if valor == "5":
          n = 5
          lista_palabras.append(palabra)
    if dificultad == "3":
      print("Has elegido la dificultad difícil")
      for palabra, valor in diccionario_palabras.items():
        if valor == "6":
          n = 6
          lista_palabras.append(palabra)

    #Palabra aleatoria da dificultade seleccionada
    p_adivinar = random.choice(lista_palabras)
    #print(p_adivinar)

    #Creo una lista para gardar as letras acertadas e poder mostralas en pantalla
    letras_correctas = []

    #Añado a cada letra de p_adivinar un símbolo para identificar el
    #número de letras gráficamente
    añadir_posicion(letras_correctas)
    print(letras_correctas)

    #Buble para xogar ata quedarse sen intentos.
    while intentos <= MAX_INTENTOS:
      #Pedimos ao usuario que escriba unha palabra
      p_intento = input("Escribe una palabra de " + str(n) + " letras:")
      intentos = intentos + 1

      #Comprobamos se a p_intento ten o nº de letras correctas, se o
      #número de letras e incorrecto volvemos a pedir a p_intento
      if len(p_intento) != len(p_adivinar):
        print("La palabra debe tener " + str(n) + " letras")
        intentos = intentos - 1
        continue

      try:
        #Se a letra esta na p_adivinar e ademais está na mesma
        #posición marcámola en maiúscula
        for posicion in range(len(p_adivinar)):
          if p_intento[posicion] == p_adivinar[posicion]:
            letras_correctas[posicion] = p_intento[posicion].upper()
            '''
            letras_correctas.insert(posicion, p_intento[posicion].upper())
            '''

          #Se a letra esta na p_adivinar pero nunha posición incorrecta
          #marcámola en minúscula
          if p_intento[posicion] in p_adivinar and \
          p_intento[posicion] != p_adivinar[posicion]:
            letras_correctas[posicion] = p_intento[posicion].lower()
            '''
            letras_correctas.insert(posicion, p_intento[posicion].lower())
            '''

          #Se a letra non esta na p_adivinar, añadimos un "_", nesa            #posicion
          elif p_intento[posicion] not in p_adivinar and \
          letras_correctas[posicion] == "[]":
            letras_correctas[posicion] = "_"

      except ValueError:
        print("Introduce una palabra de " + str(n) + " letras")

      print(letras_correctas)

      letras_correctas = []
      añadir_posicion(letras_correctas)

      if p_intento == p_adivinar:
        print("Enhorabuena, has acertado!")
        print("El intento fue", p_intento, "y la palabra a adivinar era",
              p_adivinar)
        break

      if intentos == MAX_INTENTOS:
        print("Has perdido, la palabra era", p_adivinar)
        break

    continuar = input("¿Jugar otra partida? (s/n): ")
    if continuar == "n":
      print("Saliendo del juego...")
      break

  elif opcion == "2":
    print("Saliendo del juego...")
    break
  else:
    print("Opción no válida")
