def saludar(x):
    print("Hola", x)

saludar("lauti")


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

def validacion_letra(arriesgo, solucion):
    output = ""
    for i in range(len(arriesgo)):
        if arriesgo[i] == solucion[i]:
            output += color_de_letra(arriesgo[i], "Verde")
        elif arriesgo[i] in solucion:
            output += color_de_letra(arriesgo[i], "Amarillo")
        else:
            output += color_de_letra(arriesgo[i], "GrisOscuro")
    print(output)
    return output

def fiuble():
    solucion = "hogar"
    print("Palabra a adivinar: ? ? ? ? ?")
    arriesgo = input("Arriesgo: ")
    print("Palabra a adivinar:", )
    validacion_letra(arriesgo, solucion)