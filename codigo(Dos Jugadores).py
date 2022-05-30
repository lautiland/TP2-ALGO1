import random
import time
import utiles

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

def volver_a_jugar(si_o_no, orden_de_inicio):
    # Esta función se encarga de la validación del caracter ingresado y se pasa la variable acumulado(puntaje)
    while si_o_no not in "SsNn":
        si_o_no = str(
            input("Ingreso un caracter inválido, vuelva a ingresar su respuesta:")
        )

    if si_o_no in "Ss":
        fiuble(orden_de_inicio)
    elif si_o_no in "Nn":
        print("Juego Terminado.")

def fiuble(orden_de_inicio):

    orden_de_inicio[0],orden_de_inicio[1] = orden_de_inicio[1],orden_de_inicio[0]

    print(f"\nEl primer turno es de {orden_de_inicio[0][0]}")
    
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
            orden_de_inicio[0],orden_de_inicio[1] = orden_de_inicio[1],orden_de_inicio[0] #Intercambio de turnos de los jugadores
            print(f"\nAhora es el turno de {orden_de_inicio[0][0]}")
            print(
            "Palabra a adivinar:",
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
        print(f"El ganador es {orden_de_inicio[0][0]}")
        # Tiempo al final - inicio. Se divide por 60 para sacar la cant. de minutos, y su resto son los segundos
        tiempoM = int((fin - inicio) / 60)
        tiempoS = round((fin - inicio) % 60)
        print("Tardaron " + str(tiempoM) +
              " minutos y " + str(tiempoS) + " segundos.")
        # Se busca en la lista de puntajes, cual se obtuvo segun cantidad de intentos
        puntosObtenidos = puntaje[cuentaIntentos - 1]
    else:
        puntosObtenidos = puntaje[cuentaIntentos]
        print(f"El perdedor es {orden_de_inicio[0][0]}")

    if puntosObtenidos == -100:
        orden_de_inicio[0][1] += puntosObtenidos
        orden_de_inicio[1][1] += int(puntosObtenidos/2)
    else:
        orden_de_inicio[0][1] += puntosObtenidos
        orden_de_inicio[1][1] -= puntosObtenidos
    #Mostramos los resultados    
    print(
        f"El jugador {orden_de_inicio[0][0]} obtuvo un total de {orden_de_inicio[0][1]} puntos\n"
        + f"El jugador {orden_de_inicio[1][0]} obtuvo un total de {orden_de_inicio[1][1]} puntos"
    )

    volver_a_jugar(input("Desea seguir jugando?(S/N): "), orden_de_inicio)
    

def main():
    jugador_1,jugador_2 = str(input("Ingrese el nombre del jugador 1: ")), str(input("Ingrese el nombre del jugador 2: "))
    inicio = jugador_1,jugador_2
    orden_de_inicio = [[random.choice(inicio), 0]]

    if jugador_1 in orden_de_inicio:
        orden_de_inicio.append([jugador_2, 0])
    else:
        orden_de_inicio.append([jugador_1, 0])

    fiuble(orden_de_inicio)

main()
 