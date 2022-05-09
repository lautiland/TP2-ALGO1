import random

def obtener_color(color):
    colores = {
        "Verde": "\x1b[32m",
        "Amarillo": "\x1b[33m",
        "GrisOscuro": "\x1b[90m",
        "Defecto": "\x1b[39m"
    }
    return colores[color]

def color_de_letra(letra, color):
    return obtener_color(color) + letra.upper() + obtener_color("Defecto")

def obtener_palabras_validas():
    return["hogar"]

def verificar_arriesgo():
    while True:
        arriesgo = input("Arriesgo: ")
        if len(arriesgo) != 5 or type(arriesgo) != str:
            arriesgo = input("Ingreso incorrecto.\nArriesgo: ")
            continue
        else:
            return arriesgo

def validacion_letra(arriesgo, solucion):
    output = []
    for i in range(len(arriesgo)):
        if arriesgo[i] == solucion[i]:
            output.append(color_de_letra(arriesgo[i], "Verde"))
        elif arriesgo[i] in solucion:
            output.append(color_de_letra(arriesgo[i], "Amarillo"))
        else:
            output.append(color_de_letra(arriesgo[i], "GrisOscuro"))
    return output

def fiuble():
    solucion = random.choice(obtener_palabras_validas())
    print("Palabra a adivinar: ? ? ? ? ?")
    arriesgo = verificar_arriesgo()
    print("\nPalabra a adivinar:", solucion.upper()[0], solucion.upper()[1], solucion.upper()[2], solucion.upper()[3], solucion.upper()[4])
    intento = validacion_letra(arriesgo, solucion)
    print("Arriesgo:", intento[0], intento[1], intento[2], intento[3], intento[4])
    if arriesgo == solucion:
        print("Ganaste!")
    else:
        print("Perdiste!")