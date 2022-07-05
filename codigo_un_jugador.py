import random
import time
import utiles

acumulado = 0
puntaje = [50, 40, 30, 20, 10, -100]


def color_de_letra(letra, color):
    return utiles.obtener_color(color) + letra.upper() + utiles.obtener_color("Defecto")


def verificar_arriesgo():
    arriesgo = input("Arriesgo: ")
    while len(arriesgo) != 5 or not arriesgo.isalpha():
        if not arriesgo.isalpha():
            arriesgo = input(
                "El arriesgo no puede contener numeros, simbolos o espacios.\nArriesgo: "
            )
        elif len(arriesgo) != 5:
            arriesgo = input("La palabra debe contener 5 letras.\nArriesgo: ")
    arriesgo = arriesgo.upper()
    reemplazo = (("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"), ("Ú", "U"))
    for a, b in reemplazo:
        arriesgo = arriesgo.replace(a, b)
    return arriesgo


def verificar_amarillas(arriesgo, solucion):
    letras_verdes = {}
    letras_amarillas = {}
    for i in arriesgo:
        letras_verdes[i] = 0
        letras_amarillas[i] = 0
    for i, j in zip(arriesgo, solucion):
        if i == j:
            letras_verdes[i] += 1
        elif i in solucion:
            letras_amarillas[i] += 1
    for i in letras_amarillas:
        letras_amarillas[i] = solucion.count(i) - letras_verdes[i]
    return letras_amarillas


def validacion_letra(arriesgo, solucion):
    output = []
    amarillas = verificar_amarillas(arriesgo, solucion)
    for i, j in zip(arriesgo, solucion):
        if i == j:
            output.append(color_de_letra(i, "Verde"))
        elif i in amarillas and amarillas[i] > 0:
            output.append(color_de_letra(i, "Amarillo"))
            amarillas[i] -= 1
        else:
            output.append(color_de_letra(i, "GrisOscuro"))
    return output


def iteracion_palabra_a_adivinar(lista_nueva, lista_antigua):
    agregarse = []
    for i, j in zip(lista_nueva, lista_antigua):
        if i != j and (i != "?"):
            agregarse.append(i)
        else:
            agregarse.append(j)
    return agregarse


def validacion_sin_colores(arriesgo, solucion):
    output = []
    for i, j in zip(arriesgo, solucion):
        if i == j:
            output.append(i)
        else:
            output.append("?")
    return output


def fiuble(acumulado):
    cuentaIntentos = 1
    inicio = time.time()
    solucion = random.choice(utiles.obtener_palabras_validas())
    solucion = solucion.upper()
    codigo_oculto = "? ? ? ? ?"
    # parte INICIO palabra a adivinar
    print("Palabra a adivinar: ", codigo_oculto)
    # parte INICIO tablero de signos de interogacion
    tablero = [codigo_oculto for i in range(5)]
    for f in range(5):
        print(f"{tablero[f]} ")
    # parte INICIO te pide que arriesgues tu palabra
    arriesgo = verificar_arriesgo()

    lista_antigua = ['?', '?', '?', '?', '?']
    i = 0

    # iteracion entre arriesgo y solucion
    while i != 5 and arriesgo != solucion:

        palabra_a_adivinar = validacion_sin_colores(arriesgo, solucion)
        lista_antigua = iteracion_palabra_a_adivinar(
            palabra_a_adivinar, lista_antigua)
        if i == 4:
            print(
                "\nPalabra a adivinar:",
                *solucion
            )
        else:
            print(
                "\nPalabra a adivinar:",
                *lista_antigua
                )

        intento = validacion_letra(arriesgo, solucion)
        tablero[i] = f"{intento[0]} {intento[1]} {intento[2]} {intento[3]} {intento[4]}"
        i += 1
        for f in range(5):
            print(f"{tablero[f]} ")
        if i != 5:
            arriesgo = verificar_arriesgo()
            cuentaIntentos += 1
    # parte FINAL, si se acierta con la palabra a adivinar
    if arriesgo == solucion:
        print(
            "\nPalabra a adivinar:",
            *solucion
        )

        intento = validacion_letra(arriesgo, solucion)
        tablero[i] = f"{intento[0]} {intento[1]} {intento[2]} {intento[3]} {intento[4]}"

        for f in range(5):
            print(f"{tablero[f]} ")
        fin = time.time()
        # Tiempo al final - inicio. Se divide por 60 para sacar la cant. de minutos, y su resto son los segundos
        tiempoM = int((fin - inicio) / 60)
        tiempoS = round((fin - inicio) % 60)
        print("Ganaste! Tardaste " + str(tiempoM) +
              " minutos y " + str(tiempoS) + " segundos.\n")
        # Se busca en la lista de puntajes, cual se obtuvo segun cantidad de intentos
        puntosObtenidos = puntaje[cuentaIntentos - 1]
    else:
        puntosObtenidos = puntaje[cuentaIntentos]
        print("Perdiste!\n")

    if acumulado != 0:
        acumulado += puntosObtenidos
        if puntosObtenidos > 0:
            print(
                "Obtuviste un total de "
                + str(puntosObtenidos)
                + ", tenes acumulados "
                + str(acumulado)
                + " puntos.\n"
            )
        else:
            print(
                "Perdiste un total de "
                + str(puntosObtenidos)
                + ", tenes acumulados "
                + str(acumulado)
                + " puntos.\n"
            )
    else:
        acumulado = puntosObtenidos
        if puntosObtenidos > 0:
            print(
                "Obtuviste un total de "
                + str(puntosObtenidos)
                + " puntos.\n"
            )
        else:
            print(
                "Perdiste un total de "
                + str(puntosObtenidos)
                + " puntos.\n"
            )

    caracter = str(input("Desea seguir jugando? (S/N): "))
    Intentos(caracter, acumulado)


def Intentos(juegoNuevo, acumulado):
    # Esta función se encarga de la validación del caracter ingresado y se pasa la variable acumulado(puntaje)
    while juegoNuevo not in "SsNn":
        juegoNuevo = str(
            input("Ingreso un caracter inválido, vuelva a ingresar su respuesta: ")
        )

    if juegoNuevo == "S" or juegoNuevo == "s":
        fiuble(acumulado)
    elif juegoNuevo == "N" or juegoNuevo == "n":
        print("Juego Terminado.")


fiuble(acumulado)
