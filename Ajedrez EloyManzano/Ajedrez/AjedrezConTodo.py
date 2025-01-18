#Import de la libreria pygame
import pygame

#Inicializar Pygame
pygame.init()

#Configuración de la ventana
ANCHO = 800
ALTO = 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))#Crea una ventana de ancho*alto
pygame.display.set_caption("Ajedrez")#Cambia el titulo

#Dimensiones de las casillas
TAMAÑOCASILLA = ANCHO // 8 #Constante que almacena el tamaño de una casilla que es el ancho del tablero / 8

#Colores
BLANCO = (255, 255, 255) #Constante que almacena el color blanco
GRIS = (210, 210, 210) #Constante que almacena el color gris
AZUL = (0, 0, 80) #Constante que almacena el color azul

#Tablero
tablero = [ #Es un array bidimensional aunque en python es una lista de listas
    ["t", "c", "a", "q", "k", "a", "c", "t"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["T", "C", "A", "Q", "K", "A", "C", "T"]
]

#Cargar imagenes de las piezas
IMAGENESPIEZAS = {
    #Piezas blancas
    "P": pygame.image.load("Imagenes/peonBlanco.png"), #Asocia la letra del array a la imagen
    "T": pygame.image.load("Imagenes/torreBlanca.png"),
    "A": pygame.image.load("Imagenes/alfilBlanco.png"),
    "C": pygame.image.load("Imagenes/caballoBlanco.png"),
    "Q": pygame.image.load("Imagenes/reinaBlanca.png"),
    "K": pygame.image.load("Imagenes/reyBlanco.png"),

    #Piezas negras
    "p": pygame.image.load("Imagenes/peonNegro.png"), #Asocia la letra del array a la imagen
    "t": pygame.image.load("Imagenes/torreNegra.png"),
    "a": pygame.image.load("Imagenes/alfilNegro.png"),
    "c": pygame.image.load("Imagenes/caballoNegro.png"),
    "q": pygame.image.load("Imagenes/reinaNegra.png"),
    "k": pygame.image.load("Imagenes/reyNegro.png"),
}

#Redimensionar imágenes al tamaño de las casillas
for clave in IMAGENESPIEZAS: #Recorre todas las claves (letras) de IMAGENESPIEZAS
    #Redimensiona cada imagen y la guarda en el diccionario
    IMAGENESPIEZAS[clave] = pygame.transform.scale(IMAGENESPIEZAS[clave], (TAMAÑOCASILLA, TAMAÑOCASILLA))



#DibujarTablero
def dibujarTablero(tablero):
    for fila in range(8):#Recorrer el array de 8*8
        for col in range(8):
            #Alternar colores de las casillas
            if (fila + col) % 2 == 0: #si la suma es par
                color = GRIS
            else:
                color = AZUL
            #.rect dibuja un rectangulo en la ventana del color que toque
            pygame.draw.rect(VENTANA, color, (col * TAMAÑOCASILLA, fila * TAMAÑOCASILLA, TAMAÑOCASILLA, TAMAÑOCASILLA))
            
            # Dibujar piezas
            pieza = tablero[fila][col]#Accede a la pieza concreta de esa posicion del array
            if pieza != " ": #Si hay una pieza en la casilla
                #Se dibuja la imagen correspondiente a esa pieza
                VENTANA.blit(IMAGENESPIEZAS[pieza], (col * TAMAÑOCASILLA, fila * TAMAÑOCASILLA))

    pygame.display.flip()#Actualiza la pantalla


#Mover Peon
def moverPeon(tablero, origen, destino, jugador):
    filaOrigen, colOrigen = origen #Asignación múltiple
    filaDestino, colDestino = destino #Asignación múltiple
    pieza = tablero[filaOrigen][colOrigen] #Guarda en pieza la posición de esta

    if (jugador == "blanco" and pieza != "P") or (jugador == "negro" and pieza != "p"): #Comprueba que sea un peón negro o blanco
        print("La pieza seleccionada no es un peon valido.")
        return False

    if jugador == "blanco": #Si el jugador es blanco
        #Comprueba que solo se ha movido una posición hacia delante, comprueba que no cambia de columna porque solo se puede mover hacia delante y comprueba que la casilla de destino está vacía.
        if (filaDestino == filaOrigen - 1 and colDestino == colOrigen and tablero[filaDestino][colDestino] == " "): 
            tablero[filaDestino][colDestino] = "P" #Pone P en la posición de destino
            tablero[filaOrigen][colOrigen] = " " #Deja vacía la posición de origen
            return True
        #Comprueba que la fila de origen es 6 y la de destino es 4, que la columna es la misma, y que las dos posiciones por delante están vacías
        elif (filaOrigen == 6 and filaDestino == 4 and colDestino == colOrigen and tablero[5][colDestino] == " " and tablero[4][colDestino] == " "):
            tablero[filaDestino][colDestino] = "P" #Pone P en la posición de destino
            tablero[filaOrigen][colOrigen] = " " #Deja vacía la posición de origen
            return True
        #Comprueba que solo se ha movido una posición hacia delante, comprueba que solo se mueve una columna a la izquierda o derecha, y comprueba que la casilla de destino tiene una pieza negra
        elif (filaDestino == filaOrigen - 1 and abs(colDestino - colOrigen) == 1 and tablero[filaDestino][colDestino].islower()):
            tablero[filaDestino][colDestino] = "P" #Pone P en la posición de destino
            tablero[filaOrigen][colOrigen] = " " #Deja vacía la posición de origen
            return True
        else:
            print("No puedes comer tu propia pieza.") 

    elif jugador == "negro": #Si el jugador es negro
        #Comprueba que solo se ha movido una posición hacia delante, comprueba que no cambia de columna porque solo se puede mover hacia delante y comprueba que la casilla de destino está vacía.
        if filaDestino == filaOrigen + 1 and colDestino == colOrigen and tablero[filaDestino][colDestino] == " ":
            tablero[filaDestino][colDestino] = "p" #Pone p en la posición de destino
            tablero[filaOrigen][colOrigen] = " " #Deja vacía la posición de origen
            return True
        #Comprueba que la fila de origen es 1 y la de destino es 3, que la columna es la misma, y que las dos posiciones por delante están vacías.
        elif filaOrigen == 1 and filaDestino == 3 and colDestino == colOrigen and tablero[2][colDestino] == " " and tablero[3][colDestino] == " ":
            tablero[filaDestino][colDestino] = "p" #Pone p en la posición de destino
            tablero[filaOrigen][colOrigen] = " " #Deja vacía la posición de origen
            return True
        # Comprueba que solo se ha movido una posición hacia delante, comprueba que solo se mueve una columna a la izquierda o derecha, y comprueba que la casilla de destino tiene una pieza blanca.
        elif filaDestino == filaOrigen + 1 and abs(colDestino - colOrigen) == 1 and tablero[filaDestino][colDestino].isupper():
            tablero[filaDestino][colDestino] = "p" #Pone p en la posición de destino
            tablero[filaOrigen][colOrigen] = " " #Deja vacía la posición de origen
            return True
        else:
            print("No puedes comer tu propia pieza.")

    print("Movimiento no valido")
    return False

#Mover Torre
def moverTorre(tablero, origen, destino, jugador):
    filaOrigen, colOrigen = origen #Asignacion multiple
    filaDestino, colDestino = destino #Asignacion multiple
    pieza = tablero[filaOrigen][colOrigen] #Guarda en pieza la posicion de esta 

    if (jugador == "blanco" and pieza != "T") or (jugador == "negro" and pieza != "t"): #Comprueba que sea una torre negra o blanca
        print("La pieza seleccionada no es una torre valida.")
        return False

    if filaOrigen == filaDestino or colOrigen == colDestino: #Comprueba que el movimiento es en linea recta 
        if filaOrigen == filaDestino: #Si el movimiento es hacia delante o atras
            if colDestino > colOrigen: #Si el movimiento es hacia la derecha del tablero
                paso = 1
            else: #Si el movimiento es hacia la izquierda del tablero
                paso = -1
            for col in range(colOrigen + paso, colDestino, paso): #Recorre las columnas entre colOrigen y ColDestino hacia arriba o abajo
                if tablero[filaOrigen][col] != " ": #Comprueba si hay algo diferenet a un espacio en blanco en el camino
                    print("Hay una pieza en el camino.")
                    return False
        elif colOrigen == colDestino: #Si el movimiento es hacia un lado
            if filaDestino > filaOrigen: #Si el movimiento es hacia atras
                paso = 1
            else: #Si el movimiento es hacia delante
                paso = -1
            for fila in range(filaOrigen + paso, filaDestino, paso): #Recorre las filas entre filaOrigen y filaDestino hacia un lado o otro
                if tablero[fila][colOrigen] != " ": #Comprueba si hay algo diferente a un espacion en blanco en el camino
                    print("Hay una pieza en el camino.")
                    return False
        piezaDestino = tablero[filaDestino][colDestino] #Guarda en piezaDestino la posicion del tablero
        #Si la pieza de destino es igual a un espacio en blanco o a una pieza del oponente
        if piezaDestino == " " or (jugador == "blanco" and piezaDestino.islower()) or (jugador == "negro" and piezaDestino.isupper()):
            tablero[filaDestino][colDestino] = tablero[filaOrigen][colOrigen] #Reemplaza el contenido de la casilla de destino por la de origen
            tablero[filaOrigen][colOrigen] = " " #Deja la casilla de origen vacia
            return True
        else: #Si no es un espacion en blanco o una pieza del oponente
            print("No puedes comer tu propia pieza.")
            return False
    else: #Si el movimiento no es en linea recta
        print("Movimiento no valido para la torre. Debe moverse en linea recta.")
        return False

#Mover Alfil
def moverAlfil(tablero, origen, destino, jugador):
    filaOrigen, colOrigen = origen #Asignacion multiple
    filaDestino, colDestino = destino #Asignacion multiple
    pieza = tablero[filaOrigen][colOrigen] #Guarda en pieza la posicion de esta 

    if (jugador == "blanco" and pieza != "A") or (jugador == "negro" and pieza != "a"): #Comprueba que sea un alfil del color del jugador
        print("La pieza seleccionada no es un alfil valido.")
        return False

    #Comprueba que el numero de filas movidas sea igual que el de columnas, lo que quiere decir que se esta moviendo en diagonal
    if abs(filaDestino - filaOrigen) == abs(colDestino - colOrigen): 
        if filaDestino > filaOrigen: #Si el movimiento es hacia abajo
            pasoFila = 1
        else: #Si el movimiento es hacia arriba
            pasoFila = -1
        if colDestino > colOrigen: #Si el movimiento es hacia la derecha 
            pasoCol = 1
        else: #Si el movimiento es hacia la izquierda
            pasoCol = -1
        #Cambia las variables filaActual y colActual a las nuevas posiciones , si paso col es 1 va hacia la derecha y si es -1 va hacia la izquierda
        filaActual, colActual = filaOrigen + pasoFila, colOrigen + pasoCol 
        while filaActual != filaDestino and colActual != colDestino: #Mientras la fila de origen y destino sean distintas y la collumna de origen y destino sean distintas:
            if tablero[filaActual][colActual] != " ": #Si l posicion actual dentro del bucle es distinta a un espacio en blanco
                print("Hay una pieza en el camino.")
                return False
            filaActual += pasoFila #Suma a fila actual con el valor de pasoFila que sera el valor 1 o -1
            colActual += pasoCol #Suma a  col actual con el valor de pasoCol que sera el valor 1 o -1
        piezaDestino = tablero[filaDestino][colDestino] #Asigna a pieza destino la posicion del tablero
        #Si piezaDestino es igual a un espacio en blanco, y el jugador es blanco y la pieza de destino negra o el jugador es negro y la ficha de destino blanca
        if piezaDestino == " " or (jugador == "blanco" and piezaDestino.islower()) or (jugador == "negro" and piezaDestino.isupper()):
            tablero[filaDestino][colDestino] = tablero[filaOrigen][colOrigen] #Reemplaza el contenido de la casilla de destino por la de origen
            tablero[filaOrigen][colOrigen] = " " #Pone en la posicion de origen un espacio en blanco
            return True
        else: #Si el jugador es blanco y la posicion de destino es blanca o lo mismo con negras
            print("No puedes comer tu propia pieza.")
            return False
    else: #Si el numero de filas no es igual al numero de columans quiere decir que no se esta moviendo en diagonal
        print("Movimiento no valido para el alfil. Debe moverse en diagonal.")
        return False

#Mover Caballo
def moverCaballo(tablero, origen, destino, jugador):
    filaOrigen, colOrigen = origen #Asignacion multiple
    filaDestino, colDestino = destino #Asignacion multiple
    pieza = tablero[filaOrigen][colOrigen] #Guarda en pieza la posicion de esta 

    #Comprueba que el jugador es blanco y la pieza no es un caballo blanco y lo mismo para el color negro
    if (jugador == "blanco" and pieza != "C") or (jugador == "negro" and pieza != "c"): 
        print("La pieza seleccionada no es un caballo valido.")
        return False

    #Esto es una lista de tuplas que almacena los movimientos validos para el caballo
    movimientosValidos = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)] 

    #Comprueba si alguno de los movimientos validos coincide con el movimiento realizado
    if any((filaDestino == filaOrigen + df and colDestino == colOrigen + dc) for df, dc in movimientosValidos): 
        piezaDestino = tablero[filaDestino][colDestino] #Guarda en piezaDestino la posicion del tablero
        #Si piezaDestino es igual a un espacio en blanco, y el jugador es blanco y la pieza de destino negra o el jugador es negro y la ficha de destino blanca
        if piezaDestino == " " or (jugador == "blanco" and piezaDestino.islower()) or (jugador == "negro" and piezaDestino.isupper()):
            tablero[filaDestino][colDestino] = tablero[filaOrigen][colOrigen] #Reemplaza el contenido de la casilla de destino por la de origen
            tablero[filaOrigen][colOrigen] = " " #Pone en la posicion de origen un espacio en blanco
            return True
        else: #Si el jugador es blanco y la posicion de destino es blanca o lo mismo con negras
            print("No puedes comer tu propia pieza.")
            return False
    else: #Si el movimiento realizado no coincide con ninguno de los movimientos validos para el caballo
        print("Movimiento no valido para el caballo.")
        return False


# Mover Rey
def moverRey(tablero, origen, destino, jugador):
    filaOrigen, colOrigen = origen #Asignación múltiple
    filaDestino, colDestino = destino #Asignación múltiple
    pieza = tablero[filaOrigen][colOrigen] #Guarda en pieza la posición de esta

    if (jugador == "blanco" and pieza != "K") or (jugador == "negro" and pieza != "k"): #Comprueba que sea un rey del color del jugador
        print("La pieza seleccionada no es un rey válido.")
        return False

    #Calcula la distancia de movimiento en filas y columnas
    diferenciaFila = abs(filaDestino - filaOrigen) #Calcula el valor absoluto
    diferenciaColumna = abs(colDestino - colOrigen)

    #Comprueba que el rey se mueve solo una casilla en cualquier dirección
    if diferenciaFila <= 1 and diferenciaColumna <= 1:
        piezaDestino = tablero[filaDestino][colDestino] #Asigna a piezaDestino el contenido de la casilla destino
        #Comprueba que la casilla de destino está vacía o contiene una pieza enemiga
        if piezaDestino == " " or (jugador == "blanco" and piezaDestino.islower()) or (jugador == "negro" and piezaDestino.isupper()):
            tablero[filaDestino][colDestino] = pieza #Coloca el rey en la posición de destino
            tablero[filaOrigen][colOrigen] = " " #Deja vacía la posición de origen
            return True  # Retorna verdadero
        else:
            print("No puedes comer tu propia pieza.") #Agrega el mensaje para no comer la propia pieza
            return False #Retorna falso si el jugador intenta comer su propia pieza
    else:
        #Si el movimiento no es válido, imprime un mensaje de error
        print("Movimiento no válido para el rey.")
        return False

# Mover Reina
def moverReina(tablero, origen, destino, jugador):
    filaOrigen, colOrigen = origen  #Asignación múltiple
    filaDestino, colDestino = destino  #Asignación múltiple
    pieza = tablero[filaOrigen][colOrigen]  #Guarda en pieza la posición de esta

    if (jugador == "blanco" and pieza != "Q") or (jugador == "negro" and pieza != "q"): #Comprueba que sea una reina blanca o negra
        print("La pieza seleccionada no es una reina válida.")
        return False

    #Calcula las diferencias de movimiento
    diferenciaFila = abs(filaDestino - filaOrigen)
    diferenciaColumna = abs(colDestino - colOrigen)

    #Comprueba si el movimiento es válido para una reina
    if diferenciaFila == diferenciaColumna or filaOrigen == filaDestino or colOrigen == colDestino:
        pasoFila = 0 #Inicializa el paso en filas
        pasoColumna = 0 #Inicializa el paso en columnas

        #Define los pasos según la dirección del movimiento
        if filaOrigen != filaDestino:
            pasoFila = 1 if filaDestino > filaOrigen else -1
        if colOrigen != colDestino:
            pasoColumna = 1 if colDestino > colOrigen else -1

        #Verifica que no haya piezas en el camino
        filaActual, colActual = filaOrigen + pasoFila, colOrigen + pasoColumna
        while filaActual != filaDestino or colActual != colDestino:
            if tablero[filaActual][colActual] != " ":
                print("Hay una pieza en el camino.")
                return False
            filaActual += pasoFila
            colActual += pasoColumna

        #Comprueba la casilla de destino
        piezaDestino = tablero[filaDestino][colDestino] #Asigna a pieza destino el contenido de la casilla destino
        if piezaDestino == " " or (jugador == "blanco" and piezaDestino.islower()) or (jugador == "negro" and piezaDestino.isupper()):
            tablero[filaDestino][colDestino] = pieza #Coloca la reina en la posición de destino
            tablero[filaOrigen][colOrigen] = " " #Deja vacía la posición de origen
            return True  #Retorna verdadero
        else: #Si la pieza destino es del mismo color, no puedes comerla
            print("No puedes comer tu propia pieza.")
            return False
    else:
        #Si el movimiento no es válido, imprime un mensaje de error
        print("Movimiento no válido para la reina.")
        return False
    
#Mover Pieza
def moverPieza(tablero, origen, destino, jugador):
    if origen is None or destino is None: #Comprueba que origen y destino no sean nulos
        print("Movimiento no valido")
        return False
    filaOrigen, colOrigen = origen #Se guardan los valores filaOrigen y colOrigen
    pieza = tablero[filaOrigen][colOrigen]

    if pieza == " ": #Comprueba que la pieza de origen no sea un espacio en blanco es decir que la casilla no este vacia
        print("No hay una pieza en la posicion de origen.")
        return False

    #Si el jugador y blanco y la pieza seleccionada es minuscula devuelve falso y da un mensaje de error
    if jugador == "blanco" and pieza.islower(): 
        print("La pieza seleccionada no pertenece al jugador BLANCO.")
        return False
    #Si el jugador es negro y la pieza seleccionada es mayuscula devuelve false y da un mensaje de error
    elif jugador == "negro" and pieza.isupper():
        print("La pieza seleccionada no pertenece al jugador NEGRO.")
        return False

    #Comprobación de la pieza y llamada al método de cada una de ellas pasandole el tablero, la casilla de origen de destino y el jugador
    if pieza.lower() == "p": #Con el .lower ignorarmos que la pieza sea minuscula o mayuscula ya que eso lo hemos comprobado arriba
        return moverPeon(tablero, origen, destino, jugador)
    elif pieza.lower() == "t":
        return moverTorre(tablero, origen, destino, jugador)
    elif pieza.lower() == "a":
        return moverAlfil(tablero, origen, destino, jugador)
    elif pieza.lower() == "c":
        return moverCaballo(tablero, origen, destino, jugador)
    elif pieza.lower() == "k":  # Nueva comprobación para el rey
        return moverRey(tablero, origen, destino, jugador)
    elif pieza.lower()== "q":
        return moverReina(tablero, origen, destino, jugador)

    print("Movimiento no implementado para esta pieza.")
    return False


def guardarMovimiento(turno, origen, destino, pieza):
    #Abrir o crear el archivo 'movimientos.txt' para agregar los movimientos
    with open("movimientos.txt", "a") as archivo:
        archivo.write("¡Partida comenzada!")
        #Escribir el movimiento en el archivo en el formato: Turno, pieza, origen, destino
        archivo.write("Turno: "+str(turno)+" Pieza: " +str(pieza)+ " Origen: "+str (origen)+" Destino: "+str (destino)+"\n")


#Jugar
def jugar():
    turno = "blanco" #Se pone el primer turno a blancas ya que siempre se suele empezar por este turno las partidas
    print("Turno del "+turno.upper()) #Imprimo el primer turno por consola para saber a quien le toca en cada momento
    corriendo = True #Es una variable bandera que controla cuando funciona el bucle while
    origen = None #Inicializo la varibale a nulo
    destino = None #Inicializo la varibale a nulo

    #with open("movimientos.txt","w") as archivo:
        #archivo.write("¡La partida ha comenzado! \n")

    while corriendo: #El bucle se ejcuta mientras qie la variable corriendo no se cambie a false
        dibujarTablero(tablero) #Llama al metodo dibujar tablero y le pasa por parametro el tablero

        for evento in pygame.event.get(): #Este bucle captura los eventos de pygame
            if evento.type == pygame.QUIT: #Si el evento es cerrar la ventana se detiene el juego
                corriendo = False #La variable bandera corriendo pasa a ser False
                pygame.quit() #Cierra pygame
                return
            elif evento.type == pygame.MOUSEBUTTONDOWN: #Esto maneja que el evento sea el clic del raton
                pos = pygame.mouse.get_pos() #Obtiene la posicion del raton en la ventana y lo guarda en la variable pos en forma de coordenadas
                #Convierte las coordenadas de pixeles de la anterior variable en filas y columnas del tablero dividiendo las coordenadas por el tamaño de las casillas
                fila, col = pos[1] // TAMAÑOCASILLA, pos[0] // TAMAÑOCASILLA 
                if origen is None: #Si origen es none
                    origen = (fila, col) #Se asigna los valores del primer clic a la variable origen

                else: #Si ya se ha seleccionado un origen el segundo clic se guarda como destino 
                    destino = (fila, col)

                    #Llama al metodo moverPieza y si devuelve true que quiere decir que se ha ejecutado cambia el turno.
                    if moverPieza(tablero, origen, destino, turno):
                        pieza = tablero[fila][col]  # Determinar la pieza que se movió
                        guardarMovimiento(turno, origen, destino, pieza)  
                        if turno == "blanco":  #Cambia el turno depende de cual este 
                            turno = "negro"
                        else:
                            turno = "blanco"
                        print()
                        #print("La pieza se ha movido de " + str(origen) + " a " + str(destino))
                        print()
                        print ("Turno del "+turno.upper()) #Imprime el proximo turno
                        print()
                 
                    print("La pieza se ha movido de " + str(origen) + " a " + str(destino))


                    #with open("movimientos.txt","a") as archivo:
                        #archivo.write("Turno: "+turno+ " Origen: "+str(origen)+" Destino:"+str(destino)+"\n")

                    #else:
                        #print("Es el turno del jugador "+turno.upper())

                    #Se reestablecen las variables origen y destino para el proximo movimiento
                    origen = None 
                    destino = None

    pygame.quit() #Cierra la ventana de pygame y termina el programa

#Llamar al metodo jugar
jugar()





#Metodos del modo consola que ya no uso: 

#Mostrar Tablero
def mostrarTablero(tablero):
    print()
    print("\t    a | b | c | d | e | f | g | h\n")
    print("\t    -----------------------------")
    for fila in range(8):#Recorre un for de 8 que muestra las filas del tablero y les pone un numero que va del 8 al 1
        print("\t" + str(8 - fila) + "   " + " | ".join(tablero[fila]) + "   " + str(8 - fila))
        print("\t    -----------------------------")
    print("\n\t    A | B | C | D | E | F | G | H") #\n salto de linea y \t tabulador
    print()

#Pedir Movimiento 
def pedirMovimiento(turno):
    movOrigen = input(turno + ", introduce la posicion de origen (ej: A1, B7): ")
    if movOrigen == "FinDePartida": #Si se escribe FinDePartida termina la partida
        return "FinDePartida", None

    movDestino = input(turno + ", introduce la posicion de destino (ej: A1, B7): ")
    origen = convertirCoordenada(movOrigen) #Convierte la variable origen en una coordenada 
    destino = convertirCoordenada(movDestino) #Convierte la variable destino en una coordenada 
    return origen, destino

#Convertir Coordenada
def convertirCoordenada(coordenada):
    try:
        columna = ord(coordenada[0].upper()) - ord('A') #Coge el primer caracter de la coordenada, la pasa a mayuscula y le saca el valor ascii y al restarlo obtenemos el indice correcto
        fila = 8 - int(coordenada[1]) #Coge el segundo caracter de la coordenada que ya debe de ser un numero
        if columna < 0 or columna > 7 or fila < 0 or fila > 7: #Comprueba que la combinacion de columna y fila esten en el rango
            raise ValueError("Posicion fuera de rango.")
        return fila, columna #Retorna el numero de columna y numero de fila
    except (IndexError, ValueError): #Controla la excepcion de un indice fuera del rango y la excepcion de un tipo de variable que no es el aceptado
        print("¡Error!: La posicion que has introducido no es correcta. Por favor usa el formato correcto (ej: A1, B7).")
        return None