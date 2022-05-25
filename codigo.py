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


def validacion_sin_colores(arriesgo, solucion):
    output = []
    amarillas = verificar_amarillas(arriesgo, solucion)
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
    i = 0

    # iteracion entre arriesgo y solucion
    while arriesgo != solucion:
        palabra_a_adivinar = validacion_sin_colores(arriesgo, solucion)
        print(
            "\nPalabra a adivinar:",
            palabra_a_adivinar[0],
            palabra_a_adivinar[1],
            palabra_a_adivinar[2],
            palabra_a_adivinar[3],
            palabra_a_adivinar[4],
        )
        intento = validacion_letra(arriesgo, solucion)

        tablero[i] = f"{intento[0]} {intento[1]} {intento[2]} {intento[3]} {intento[4]}"
        i += 1

        for f in range(5):
            print(f"{tablero[f]} ")
        if i == 5:
            print(
                "\nPalabra oculta:",
                solucion[0],
                solucion[1],
                solucion[2],
                solucion[3],
                solucion[4],
            )
            break
        arriesgo = verificar_arriesgo()
        cuentaIntentos += 1

    # parte FINAL, si se acierta con la palabra a adivinar
    if arriesgo == solucion:
        print(
            "\nPalabra a adivinar:",
            solucion[0],
            solucion[1],
            solucion[2],
            solucion[3],
            solucion[4],
        )

        intento = validacion_letra(arriesgo, solucion)
        tablero[i] = f"{intento[0]} {intento[1]} {intento[2]} {intento[3]} {intento[4]}"

        for f in range(5):
            print(f"{tablero[f]} ")
        fin = time.time()
        print("Ganaste!")
        tiempoM = int((fin - inicio) / 60)
        tiempoS = round((fin - inicio) % 60)
        print("Tardaste " + str(tiempoM) + " minutos y " + str(tiempoS) + " segundos.")
        puntosObtenidos = puntaje[cuentaIntentos - 1]
    else:
        puntosObtenidos = puntaje[cuentaIntentos]
        print("Perdiste!")

    if acumulado != 0:
        acumulado += puntosObtenidos
    else:
        acumulado = puntosObtenidos

    print(
        "Obtuviste un total de "
        + str(puntosObtenidos)
        + ", tenes acumulados "
        + str(acumulado)
        + " puntos."
    )
    caracter = str(input("Desea seguir jugando?(S/N):"))
    Intentos(caracter, acumulado)


def Intentos(juegoNuevo, acumulado):
    ###Esta función se encarga del print para volver a jugar y la validación del caracter ingresado
    while juegoNuevo not in "SsNn":
        juegoNuevo = str(
            input("Ingreso un caracter inválido, vuelva a ingresar su respuesta:")
        )

    if juegoNuevo == "S" or juegoNuevo == "s":
        fiuble(acumulado)
    elif juegoNuevo == "N" or juegoNuevo == "n":
        print("Juego Terminado.")


fiuble(acumulado)
