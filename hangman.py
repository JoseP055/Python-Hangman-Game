import random         #Importa bibliotecas de python.
import string
from words_for_hangman import words           #Importa cosas de archivos en un mismo directorio.
from hangman_draw import lifes_dicc

def get_valid_word(words):            #Funcion para definir las palabras validas para el juego.

    word = random.choice(words)                 #La palabra va aser igual a una opcion aleatoria gnerada por la computadora.

    while '-' in word or " " in word:           #Si la palabra contiene caracteres como "-" o " " va a elegir otra palabra de la lista.
        word = random.choice(words)

    return word.upper()                    #En dado caso que la palabra sea valida la va a convertir en Mayusculas.

def ahorcado():                                 #Funcion para iniciar el juego.

    print("Bienvenido al Juego del Ahorcado")

    word = get_valid_word(words)                    #La palabra para jugar va a ser igual a una palabra obtenida de la funcion de palabras validas.

    letters_to_guess = set(word)                      #Variable que determina las letras por adivinar, las consigue haciendo uso de un conjunto ya que en los conjuntos no se repuiten elementos.
    letters_guessed = set()                           #Variable que va a ir guardando las letras adivinadas en un nuevo conjunto.
    alphabet = set(string.ascii_uppercase)            #Variable que contiene un conjunto de todas las letras del abecedario en ingles especifacmente en mayuscula.

    lifes = 7                                        #Cantidad de vidas.

    while len(letters_to_guess) > 0 and lifes > 0:             #Mientras la cantidad de letras por adivinar y las vidas sean mayores a 0 inicia un ciclo.

        if letters_guessed == set():                          #Si no hay letras por adivinar dira el mensaje 1 y si ya hay letras dira el mensaje 2.
            print(f"Tienes la siguiente cantidad de vidas {lifes}. Es hora de empezar a adivinar letras.")
        else:
            print(f"Tienes la siguiente cantidad de vidas: {lifes} y has usado las siguientes letras: {' '.join(letters_guessed)}")

        word_list = [letter if letter in letters_guessed else '_' for letter in word]   #Variable que crea una lista donde reemplaza a las letras de la palabra original por "_".
        print(lifes_dicc[lifes])   #Muestra el diagrama visual del juego                #Cuando la letra es adivinada sustituye "_" por la letra adivinada.
        print(f"Palabra: {' '.join(word_list)}")      #Muestra la lista de letras adivinadas o "_" separadas por un " ".

        user_letter = input("Escoge una letra: ").upper()    #El usuario ingresa una letra, se guarda en una variable y se transforma en Mayusculas.

        #Logica del proceso de adivinar letras.
        if user_letter in alphabet - letters_guessed:         #Si la letra del usuario esta en el alfabeto y no esta en letras adivinadas:
            letters_guessed.add(user_letter)                  #Agrega la letra dle usuario en letras adivinadas.

            if user_letter in letters_to_guess:               #Si letra del usuario pertenece a las letras por adivinar:
                letters_to_guess.remove(user_letter)          #Se remueve la letra del conjunto letras por adivinar.
                print("")
            else:                                             #Si la letra no esta en las letras por adivinar:
                lifes -= 1                                    #Remueve una vida.
                print(f"\nLa letra {user_letter} no está en la palabra.")

        elif user_letter in letters_guessed:                                        #Si la letra ya fue utilizada manda un mensaje.
            print(f"\nLa letra {user_letter} ya fue escogida. Escoge otra letra.")
        else:                                                                       #Si se ingresa un caracter que no este en el abecedario. Manda otro mensaje.
            print(f"\nEl carácter {user_letter} no es válido. Intenta otra vez.")

    #Fin del juego
    if lifes == 0:                                              #si las vidas son = 0 entonces:
        print(lifes_dicc[lifes])
        print(f"Ahorcado. Perdiste. La palabra era {word}")
    else:                                                       #Si las vidas son mayores a 0 entonces:
        print(f"Palabra: {' '.join(word)}")
        print(f"¡Has ganado! Lograste adivinar la palabra {word} y te sobraron {lifes} intentos. ¡Felicidades!")


ahorcado()
