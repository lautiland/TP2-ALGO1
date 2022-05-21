import random
import utiles

def color_de_letra(letra, color):
    return utiles.obtener_color(color) + letra.upper() + utiles.obtener_color("Defecto")

def verificar_arriesgo():
    arriesgo = input("Arriesgo: ")
    while len(arriesgo) != 5 or not arriesgo.isalpha():
        if not arriesgo.isalpha():
            arriesgo = input("El arriesgo no puede contener numeros o simbolos.\nArriesgo: ")
        elif len(arriesgo) != 5:
            arriesgo = input("La palabra debe contener 5 letras.\nArriesgo: ")
    reemplazo = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    for a, b in reemplazo:
        arriesgo = arriesgo.replace(a, b).replace(a.upper(), b.upper())
    return arriesgo.upper()

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

def fiuble():
    solucion = random.choice(utiles.obtener_palabras_validas())
    solucion = solucion.upper()
    print("Palabra a adivinar: ? ? ? ? ?")
    arriesgo = verificar_arriesgo()
    print("\nPalabra a adivinar:", solucion[0], solucion[1], solucion[2], solucion[3], solucion[4])
    intento = validacion_letra(arriesgo, solucion)
    print("Arriesgo:", intento[0], intento[1], intento[2], intento[3], intento[4])
    if arriesgo == solucion:
        print("Ganaste!")
    else:
        print("Perdiste!")

fiuble()