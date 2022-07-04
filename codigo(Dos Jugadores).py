import random
import time
import utiles
from datetime import date
from datetime import datetime

# Definimos los puntos ganados o perdidos segun la cantidad de intentos.
puntaje = [50, 40, 30, 20, 10, -100]
# Modularizacion hecha por Lautaro Jovanovics, Nicolas Serrudo , Diego Lima y Jonathan Pistonesi.


def color_de_letra(letra, color):
    # Utiliza el archivo utiles.py para obtener los colores correspondientes a la validacion de la letra.1
    return utiles.obtener_color(color) + letra.upper() + utiles.obtener_color("Defecto")


# Funcion hecha por Pedro Miguel


def verificar_arriesgo(longitud_palabra):
    # Se encarga de validar que el ingreso de la palabra cumpla con los requisitos, reemplazar las tildes, y minusculas.2
    arriesgo = input("Arriesgo: ")
    while len(arriesgo) != longitud_palabra or not arriesgo.isalpha():
        if not arriesgo.isalpha():
            arriesgo = input(
                "El arriesgo no puede contener numeros, simbolos o espacios.\nArriesgo: "
            )
        elif len(arriesgo) != longitud_palabra:
            arriesgo = input(
                "La palabra debe contener"
                + str(longitud_palabra)
                + "letras.\nArriesgo: "
            )
    arriesgo = arriesgo.upper()
    reemplazo = (("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"), ("Ú", "U"))
    for a, b in reemplazo:
        arriesgo = arriesgo.replace(a, b)
    return arriesgo


# Funcion hecha por Pedro Miguel


def verificar_amarillas(arriesgo, solucion):
    # Funcion encargada de comprobar que la letra exista en la palabra evitando repeticiones, si es que no esta en la posicion correcta.1
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


# Funcion hecha por Pedro Miguel


def validacion_letra(arriesgo, solucion):
    # Usando funciones anteriores, asigna los colores correspondientes a cada letra.1
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


# Funcion hecha por Pedro Miguel


def iteracion_palabra_a_adivinar(lista_nueva, lista_antigua):
    # Funcion encargada de guardar las letras acertadas entre intentos.
    agregarse = []
    for i, j in zip(lista_nueva, lista_antigua):
        if i != j and (i != "?"):
            agregarse.append(i)
        else:
            agregarse.append(j)
    return agregarse


# Funcion hecha por Nicolas Serrudo y Jonathan Pistonesi


def validacion_sin_colores(arriesgo, solucion):
    # Funcion que compara el arriesgo con la solucion, validando las letras pero sin color.
    output = []
    for i, j in zip(arriesgo, solucion):
        if i == j:
            output.append(i)
        else:
            output.append("?")
    return output


# Funcion hecha por Nicolas Serrudo y Jonathan Pistonesi


def volver_a_jugar(
    si_o_no,
    orden_de_inicio,
    jugador_inicial,
    lista_palabras_posibles,
    longitud_palabra,
    maximo_partidas,
    cuenta_partidas,
    aciertos_intentos,
    partidas,
):
    # Esta función se encarga de la validación del caracter ingresado y se pasa la variable acumulado(puntaje)
    print(aciertos_intentos)
    while si_o_no not in "SsNn":
        si_o_no = str(
            input("Ingreso un caracter inválido, vuelva a ingresar su respuesta: ")
        )

    if si_o_no in "Ss":
        if jugador_inicial == orden_de_inicio[0][0]:
            orden_de_inicio[0], orden_de_inicio[1] = (
                orden_de_inicio[1],
                orden_de_inicio[0],
            )
        cuenta_partidas += 1
        fiuble(
            orden_de_inicio,
            lista_palabras_posibles,
            longitud_palabra,
            maximo_partidas,
            cuenta_partidas,
            aciertos_intentos,
            partidas,
        )
    elif si_o_no in "Nn":
        ordenado = sorted(
            aciertos_intentos.items(), key=lambda x: x[1], reverse=True
        )
        print(ordenado)
        j = 0
        for j in range(len(ordenado)):
            partidas.write(
                datetime.today().strftime("%d-%m-%Y")
                + ","
                + datetime.today().strftime("%H:%M")
                + ","
                + ordenado[j][0]
                + ","
                + str(ordenado[j][1][0])
                + ","
                + str(ordenado[j][1][1])
                + "\n"
            )

        if orden_de_inicio[0][1] > orden_de_inicio[1][1]:
            print(
                f"\nEl ganador es {orden_de_inicio[0][0]} con un total de {orden_de_inicio[0][1]}."
            )
        elif orden_de_inicio[1][1] > orden_de_inicio[0][1]:
            print(
                f"\nEl ganador es {orden_de_inicio[1][0]} con un total de {orden_de_inicio[1][1]}."
            )
        else:
            print(
                f"\nAmbos jugadores han empatado con un total de {orden_de_inicio[0][1]} puntos."
            )


# Funcion hecha por Pedro Perez

# imprime en pantalla los turnos, el intento de palabra, y solucion
def print_text_while(solucion, orden_de_inicio, lista_antigua, i):
    if i == 4:
        print("\nPalabra a adivinar:", *solucion)
    else:
        # Intercambio de turnos de los jugadores
        orden_de_inicio[0], orden_de_inicio[1] = orden_de_inicio[1], orden_de_inicio[0]
        print(f"\nAhora es el turno de {orden_de_inicio[0][0]}")
        print("Palabra a adivinar:", *lista_antigua)


# funcion que retorna constantes y un print iteracion inicio del juego
def constantes_y_print_prewhile(longitud_palabra):
    cuenta = 1
    cuenta2 = 0
    codigo_oculto = "? "
    lista_antigua = ["?"]
    while cuenta < longitud_palabra:
        codigo_oculto += "? "
        cuenta += 1

    # parte INICIO palabra a adivinar
    print("Palabra a adivinar: ", codigo_oculto)
    # parte INICIO tablero de signos de interogacion
    tablero = [codigo_oculto for i in range(5)]
    for f in range(5):
        print(f"{tablero[f]} ")
    # parte INICIO te pide que arriesgues tu palabra
    arriesgo = verificar_arriesgo(longitud_palabra)

    for cuenta2 in range(longitud_palabra - 1):
        lista_antigua.append("?")
        cuenta2 += 1
    i = 0
    return arriesgo, lista_antigua, i, tablero


# Asigna los puntos a los jugadores
def asignar_puntos(puntos_obtenidos, orden_de_inicio):
    if puntos_obtenidos == -100:
        orden_de_inicio[0][1] += puntos_obtenidos
        orden_de_inicio[1][1] += int(puntos_obtenidos / 2)
    else:
        orden_de_inicio[0][1] += puntos_obtenidos
        orden_de_inicio[1][1] -= puntos_obtenidos
    return orden_de_inicio


# Funcion hecha por Pedro Miguel


def leer_linea_archivo(archivo, default):
    linea = archivo.readline()
    lista = linea.lstrip(" ¡¿-_").rstrip(" .;:-_),?!\n").split(" ")
    i = 0
    palabras = []
    while i < len(lista):
        palabras.append(lista[i].lower().lstrip("¡¿-_").rstrip(".;:-_),?!"))
        i += 1
    return palabras if palabras[0] != "" else default


def leer_linea_csv(archivo, default):
    linea = archivo.readline()
    return linea if linea else default


def obtener_config(archivoConfig):
    archivoConfig.seek(0)
    linea = leer_linea_csv(archivoConfig, "longitud_palabra_secreta,5")
    aux, longitud_palabra = linea.rstrip("\n").split(",")
    linea = leer_linea_csv(archivoConfig, "maximo_partidas,5")
    aux, maximo_partidas = linea.rstrip("\n").split(",")
    linea = leer_linea_csv(archivoConfig, "reiniciar_archivo,False")
    aux, reiniciar_archivo_partidas = linea.rstrip("\n").split(",")
    return int(longitud_palabra), int(maximo_partidas), reiniciar_archivo_partidas


def obtener_palabras(archivo1, archivo2, archivo3, archivoNuevo, longitud_palabra):
    archivo1.seek(0)
    archivo2.seek(0)
    archivo3.seek(0)
    dicc_palabras = {}
    linea1 = leer_linea_archivo(archivo1, "")

    while linea1 != ["fin"]:
        if linea1 != "":
            for elemento in linea1.copy():
                if not elemento.isalpha() or len(elemento) != longitud_palabra:
                    linea1.remove(elemento)
                else:
                    if elemento not in dicc_palabras:
                        dicc_palabras[elemento] = [1, 0, 0]
                    else:
                        dicc_palabras[elemento][0] += 1
            linea1 = leer_linea_archivo(archivo1, "")
        else:
            linea1 = leer_linea_archivo(archivo1, "")

    linea2 = leer_linea_archivo(archivo2, "")
    while linea2 != ["fin", "del", "tomo", "primero"]:
        if linea2 != "":
            for elemento in linea2.copy():
                if not elemento.isalpha() or len(elemento) != longitud_palabra:
                    linea2.remove(elemento)
                else:
                    if elemento not in dicc_palabras:
                        dicc_palabras[elemento] = [0, 1, 0]
                    else:
                        dicc_palabras[elemento][1] += 1
            linea2 = leer_linea_archivo(archivo2, "")
        else:
            linea2 = leer_linea_archivo(archivo2, "")

    linea3 = leer_linea_archivo(archivo3, "")
    while linea3 != ["fin"]:
        if linea3 != "":
            for elemento in linea3.copy():
                if not elemento.isalpha() or len(elemento) != longitud_palabra:
                    linea3.remove(elemento)
                else:
                    if elemento not in dicc_palabras:
                        dicc_palabras[elemento] = [0, 0, 1]
                    else:
                        dicc_palabras[elemento][2] += 1
            linea3 = leer_linea_archivo(archivo3, "")
        else:
            linea3 = leer_linea_archivo(archivo3, "")

    lista_palabras = sorted(dicc_palabras.keys())

    for elemento in lista_palabras:
        archivoNuevo.write(
            elemento
            + ","
            + str(dicc_palabras[elemento][0])
            + ","
            + str(dicc_palabras[elemento][1])
            + ","
            + str(dicc_palabras[elemento][2])
            + "\n"
        )
    return lista_palabras


def fiuble(
    orden_de_inicio,
    lista_palabras,
    longitud_palabra,
    maximo_partidas,
    cuenta_partidas,
    aciertos_intentos,
    partidas,
):

    # Funcion encargada de llevar a cabo el desempeño del juego, usando funciones anteriores.
    jugador_inicial = orden_de_inicio[0][0]
    print(cuenta_partidas)
    print(f"\nEl primer turno es de {jugador_inicial}")

    cuentaIntentos = 1
    inicio = time.time()
    solucion = random.choice(lista_palabras)
    solucion = solucion.upper()
    reemplazo = (("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"), ("Ú", "U"))
    for a, b in reemplazo:
        solucion = solucion.replace(a, b)   
    print(solucion)

    arriesgo, lista_antigua, i, tablero = constantes_y_print_prewhile(longitud_palabra)

    # iteracion entre arriesgo y solucion
    while i != 5 and arriesgo != solucion:
        print(orden_de_inicio)
        palabra_a_adivinar = validacion_sin_colores(arriesgo, solucion)
        lista_antigua = iteracion_palabra_a_adivinar(palabra_a_adivinar, lista_antigua)
        print_text_while(solucion, orden_de_inicio, lista_antigua, i)
        intento = validacion_letra(arriesgo, solucion)
        largo = 0
        tablero_aux = ""

        while largo < len(intento):
            tablero_aux += intento[largo] + " "
            largo += 1

        tablero[i] = tablero_aux

        i += 1

        for f in range(5):
            print(f"{tablero[f]} ")
        if i != 5:
            arriesgo = verificar_arriesgo(longitud_palabra)
            cuentaIntentos += 1
        aciertos_intentos[orden_de_inicio[0][0]][1] += 1
    # parte FINAL, si se acierta con la palabra a adivinar
    if arriesgo == solucion:
        print("\nPalabra a adivinar:", *solucion)

        intento = validacion_letra(arriesgo, solucion)

        largo2 = 0
        tablero_aux2 = ""

        while largo2 < len(intento):
            tablero_aux2 += intento[largo2] + " "
            largo2 += 1

        tablero[i] = tablero_aux2

        for f in range(5):
            print(f"{tablero[f]} ")
        fin = time.time()
        aciertos_intentos[orden_de_inicio[0][0]][0] += 1
        print(f"El ganador es {orden_de_inicio[0][0]}\n")
        # Tiempo al final - inicio. Se divide por 60 para sacar la cant. de minutos, y su resto son los segundos
        tiempoM = int((fin - inicio) / 60)
        tiempoS = round((fin - inicio) % 60)
        print(
            "Tardaron " + str(tiempoM) + " minutos y " + str(tiempoS) + " segundos.\n"
        )
        # Se busca en la lista de puntajes, cual se obtuvo segun cantidad de intentos
        puntosObtenidos = puntaje[cuentaIntentos - 1]
    else:
        puntosObtenidos = puntaje[cuentaIntentos]
        print("Ambos jugadores han perdido.\n")

    orden_de_inicio = asignar_puntos(puntosObtenidos, orden_de_inicio)
    # Mostramos los resultados
    print(
        f"El jugador {orden_de_inicio[0][0]} obtuvo un total de {orden_de_inicio[0][1]} puntos\n"
        + f"El jugador {orden_de_inicio[1][0]} obtuvo un total de {orden_de_inicio[1][1]} puntos\n"
    )

    if cuenta_partidas < maximo_partidas:
        volver_a_jugar(
            input("Desea seguir jugando? (S/N): "),
            orden_de_inicio,
            jugador_inicial,
            lista_palabras,
            longitud_palabra,
            maximo_partidas,
            cuenta_partidas,
            aciertos_intentos,
            partidas,
        )
    else:
        print("Ha llegado al maximo de partidas que es: " + str(maximo_partidas))
        volver_a_jugar(
            "N",
            orden_de_inicio,
            jugador_inicial,
            lista_palabras,
            longitud_palabra,
            maximo_partidas,
            cuenta_partidas,
            aciertos_intentos,
            partidas,
        )


# Funcion hecha por Pedro Miguel, Nicolas Serrudo, Diego Lima, Lautaro Jovanovics, Pedro Perez y Jonathan Pistonesi.


def main():
    # Funcion principal, encargada de tomar los nombres de los jugadores, mezclarlos, y luego ejecutar el juego.
    config = open("configuracion.csv", "r+")
    longitud_palabra, maximo_partidas, reinciar_archivo_partidas = obtener_config(
        config
    )
    config.close()

    jugador_1, jugador_2 = str(input("Ingrese el nombre del jugador 1: ")), str(
        input("Ingrese el nombre del jugador 2: ")
    )
    inicio = jugador_1, jugador_2
    orden_de_inicio = [[random.choice(inicio), 0]]

    if jugador_1 in orden_de_inicio[0][0]:
        orden_de_inicio.append([jugador_2, 0])
    else:
        orden_de_inicio.append([jugador_1, 0])
    aciertos_intentos = {jugador_1: [0, 0], jugador_2: [0, 0]}

    archivo1 = open("Cuentos.txt", "r", encoding="utf8")
    archivo2 = open("La araña negra - tomo 1.txt", "r", encoding="utf8")
    archivo3 = open("Las 1000 Noches y 1 Noche.txt", "r", encoding="utf8")
    archivoNuevo = open("palabras.csv", "w", encoding="utf8")
    partidas = open("partidas.csv", "w")
    lista_palabras_posibles = obtener_palabras(
        archivo1, archivo2, archivo3, archivoNuevo, longitud_palabra
    )
    print("FUNCIONAAAAAAAAAA (creo)")
   
    archivo1.close()
    archivo2.close()
    archivo3.close()
    archivoNuevo.close()
    cuenta_partidas = 1
    fiuble(
        orden_de_inicio,
        lista_palabras_posibles,
        longitud_palabra,
        maximo_partidas,
        cuenta_partidas,
        aciertos_intentos,
        partidas,
    )


main()
