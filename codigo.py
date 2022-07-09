import random
import time
import utiles
from cgitb import grey
from re import M, T
from datetime import date
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from setuptools import Command

# Definimos los puntos ganados o perdidos segun la cantidad de intentos.
puntaje = [50, 40, 30, 20, 10, -100]

def leer_archivo(archivo):
    #Función encargada de en base a un nombre de un archivo ya abrierto en algun formato de lectura, devolver las lineas del mismo
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = "",""

    return devolver
def cerrar_ventana(ventana):
    #Funcion encargada de cerrar una ventana especificada
    ventana.destroy()
# Funcion hecha por Lautaro Jovanovics

def login(jugador):
    #Funcion maestra del login, que añade la interfaz gráfica al inicio de sesión y registro

    raiz = Tk()
    raiz.config(bg="light grey")
    raiz.title("Login")

    frame1 = Frame(raiz, width=1200, height= 850)
    frame1.pack()
    raiz.resizable(False, False)

    def register():
        #Funcion que permite registrar un usuario y contraseña

        ventana_2 = Toplevel()
        ventana_2.title("Register")
        ventana_2.resizable(False, False)

        usuario_registro = StringVar()
        clave1_registro = StringVar()
        clave2_registro = StringVar()

        nombre = Label(ventana_2, text="Usuario:")
        nombre.grid(row=0, column=0, sticky= "e", padx= 10, pady=10)

        nombre_entry = Entry(ventana_2, textvariable=usuario_registro)
        nombre_entry.grid(row=0 , column= 1, padx= 10, pady=10)
        nombre_entry.config(bd=5, relief=GROOVE)

        clave1 = Label(ventana_2, text="Clave:")
        clave1.grid(row=1, column=0, sticky= "e", padx= 10, pady=10)

        clave1_entry = Entry(ventana_2, textvariable=clave1_registro)
        clave1_entry.grid(row=1, column=1, padx= 10, pady=10)
        clave1_entry.config(bd=5, relief=GROOVE, show="*")

        clave2 = Label(ventana_2, text="Repitir clave:")
        clave2.grid(row=2, column=0, sticky= "e", padx= 10, pady=10)

        clave2_entry = Entry(ventana_2, textvariable=clave2_registro)
        clave2_entry.grid(row=2, column=1, padx= 10, pady=10)
        clave2_entry.config(bd=5, relief=GROOVE, show="*")

        cerrar_ventana2 = Button(ventana_2, text = "Cerrar", command= ventana_2.destroy)
        cerrar_ventana2.grid(row = 3, column= 0, padx= 10, pady=10 )
        cerrar_ventana2.config(bd=5, relief=GROOVE, bg="light blue", cursor="hand2")

        def comprobar_registro():

            archivo = open("usuarios.csv", "r+")

            usuario, clave = leer_archivo(archivo)
            usu_comp_reg = usuario_registro.get()
            clav1_comp_reg = clave1_registro.get()
            clav2_comp_reg = clave2_registro.get()
            estado_reg = True

            if clav1_comp_reg != clav2_comp_reg:
                estado_reg =  False
                messagebox.showerror(message="Las contraseñas son diferentes")

            if usu_comp_reg and estado_reg:
                condicion_alpha = True
                condicion_largo = False

                if 4<=len(usu_comp_reg)<=15:
                    condicion_largo = True

                for x in usu_comp_reg :
                    if (x in " #!$%&/()=?¡*¨¨][}{+-.,;:"):
                        condicion_alpha = False
                if (not condicion_largo) or (not condicion_alpha):
                    estado_reg = False
                    messagebox.showerror(message="El nombre no cumple los requisitos")

            if clav1_comp_reg and estado_reg:
                condicion_general = True
                condicion_mayuscula = False
                condicion_minuscula = False
                condicion_numero = False
                condicion_guion = False
                condicion_len = False

                if 8<=len(clav1_comp_reg)<=12:
                    condicion_len = True

                for x in clav1_comp_reg:
                    if x in "ÁÉÍÓÚáéíóú":
                        condicion_general = False
                    if x in "_-":
                        condicion_guion = True
                    if x.isnumeric():
                        condicion_numero = True
                    if x.isupper():
                        condicion_mayuscula = True
                    if x.islower():
                        condicion_minuscula = True

                if (not condicion_len) or (not condicion_general) or (not condicion_mayuscula) or (not condicion_minuscula) or (not condicion_numero) or (not condicion_guion):
                    estado_reg = False
                    messagebox.showerror(message="La contraseña no cumple los requisitos")

            while usuario and estado_reg:
                if usu_comp_reg == usuario:
                    estado_reg = False
                    messagebox.showerror(message="Ya existe un usuario con ese nombre")

                while usuario and estado_reg and usu_comp_reg != usuario:
                    usuario, clave = leer_archivo(archivo)
                    if usu_comp_reg == usuario:
                        estado_reg = False
                        messagebox.showerror(message="Ya existe un usuario con ese nombre")

            if estado_reg:

                archivo.seek(0,2)
                archivo.write(usu_comp_reg + "," + clav1_comp_reg + "\n")

                messagebox.showinfo(message="Registro Exitoso!")

                cerrar_ventana(ventana_2)

            archivo.close()

        def register_enter(event):
            comprobar_registro()

        aceptar = Button(ventana_2, text= "Aceptar", command= comprobar_registro)
        aceptar.grid(row = 3 , column= 1, padx= 10, pady=10 )
        aceptar.config(bd=5, relief=GROOVE, bg="light blue", cursor="hand2")
        clave2_entry.bind("<Return>", register_enter)

    usuario_ingresado = StringVar()
    clave_ingresada = StringVar()

    if jugador == 1:
        titulo1 = Label(frame1, text="Primer Jugador")
        titulo1.grid(row=0, column=1, sticky= "e", padx= 50, pady=10)
    elif jugador == 2:
        titulo2 = Label(frame1, text="Segundo Jugador")
        titulo2.grid(row=0, column=1, sticky= "e", padx= 50, pady=10)

    nombre = Label(frame1, text="Usuario :")
    nombre.grid(row=1, column=0, sticky= "e", padx= 10, pady=10)

    nombre_entry = Entry(frame1, textvariable=usuario_ingresado)
    nombre_entry.grid(row=1 , column= 1, padx= 10, pady=10)
    nombre_entry.config(bd=5, relief=GROOVE)

    clave = Label(frame1, text="Clave :")
    clave.grid(row=2, column=0, sticky= "e", padx= 10, pady=10)

    clave_entry = Entry(frame1, textvariable=clave_ingresada)
    clave_entry.grid(row=2, column=1, padx= 10, pady=10)
    clave_entry.config(bd=5, relief=GROOVE, show="*")

    def comprobar():

        global user

        archivo = open("usuarios.csv", "rt")
        
        usu_comp_log = usuario_ingresado.get()
        clav_comp_log = clave_ingresada.get()

        estado = False

        usuario, clave = leer_archivo(archivo)
        
        while usuario and clave and not estado:

            if usu_comp_log == usuario and clav_comp_log == clave:
                estado = True

            while (usuario and clave and not estado) and ((usu_comp_log != usuario) or (clav_comp_log != clave)):
                usuario, clave = leer_archivo(archivo)
                if (usu_comp_log == usuario) and (clav_comp_log == clave):
                    estado = True
                

        if estado and usu_comp_log and clav_comp_log:
            messagebox.showinfo(message="Ingresado Exitoso!")
            user = usuario
            cerrar_ventana(frame1)
            cerrar_ventana(raiz)
                
        else: 
            messagebox.showerror(message="Usuario o clave incorrectos")

            user = ""

        
        archivo.close()

    def login_enter(event):
        comprobar()

    boton1 = Button(frame1, text=" Ingresar ", command= comprobar)
    boton1.grid(row = 3, column = 0, padx= 10, pady=10 )
    boton1.config(bd=5, relief=GROOVE, bg="light blue", cursor="hand2")
    clave_entry.bind("<Return>", login_enter)

    boton2 = Button(frame1, text="Registrarse",command = register)
    boton2.grid(row = 3, column = 1, padx= 10, pady=10)
    boton2.config(bd=5, relief=GROOVE, bg="light blue", cursor="hand2")

    raiz.mainloop()
# Funcion hecha por Jonathan Pistonesi y Lautaro Jovanovics

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
                "La palabra debe contener "
                + str(longitud_palabra)
                + " letras.\nArriesgo: "
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

        print(f"El jugador {ordenado[0][0]} tiene {ordenado[0][1][0]} aciertos y {ordenado[0][1][1]} intentos")
        print(f"El jugador {ordenado[1][0]} tiene {ordenado[1][1][0]} aciertos y {ordenado[1][1][1]} intentos")
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
# Funcion hecha por Pedro Miguel

def leer_linea_csv(archivo, default):
    linea = archivo.readline()
    defecto_o_configuracion = True
    if linea == "\n" or linea == "" or linea ==" ":
       linea = default
       defecto_o_configuracion = False
    return linea,defecto_o_configuracion
# Funcion hecha por Pedro Miguel

def obtener_config(archivoConfig):
    archivoConfig.seek(0)

    linea,defecto_o_configuracion = leer_linea_csv(archivoConfig, "longitud_palabra_secreta,5")
    aux, longitud_palabra = linea.strip("\n").split(",")
    if not(longitud_palabra) or defecto_o_configuracion == False:
        longitud_palabra = 5
        print("---- Longitud de palabra, valor por defecto")
    elif longitud_palabra:
        print("---- Longitud de palabra, valor por configuracion")


    linea,defecto_o_configuracion = leer_linea_csv(archivoConfig, "maximo_partidas,5")
    aux, maximo_partidas = linea.strip("\n").split(",")
    if not(maximo_partidas) or defecto_o_configuracion == False:
        maximo_partidas = 5
        print("---- Maxima cantidad de partidas, valor por defecto")
    elif maximo_partidas:
        print("---- Maxima cantidad de partidas, valor por configuracion")


    linea,defecto_o_configuracion = leer_linea_csv(archivoConfig, "reiniciar_archivo,False")
    aux, reiniciar_archivo_partidas = linea.strip("\n").split(",")

    if (reiniciar_archivo_partidas == False )and defecto_o_configuracion == False:
        reiniciar_archivo_partidas = "a"
        valor_reinicio= "Deshabilitado"
        print("---- Reinicio arhivo registro de partidas, valor por defecto")
        print("=============================================")
    elif reiniciar_archivo_partidas=="False" and defecto_o_configuracion == True:
        reiniciar_archivo_partidas = "a"
        valor_reinicio= "Deshabilitado"
        print("---- Reinicio archivo registro de partidas, valor por configuracion")
        print("=============================================")
    elif (reiniciar_archivo_partidas) and defecto_o_configuracion == True:
        reiniciar_archivo_partidas = "w"
        valor_reinicio= "Habilitado"
        print("---- Reinicio archivo registro de partidas, valor por configuracion")
        print("=============================================")
    
    print("Longitud de palabras: {} - Maximo de partidas de: {} - El reinicio del archivo registro de partidas fue {}".format(longitud_palabra, maximo_partidas,valor_reinicio))
    print("---------------------------------------------")

    return int(longitud_palabra), int(maximo_partidas), reiniciar_archivo_partidas
# Funcion hecha por Nicolas Serrudo y Pedro Perez

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
# Funcion hecha por Pedro Miguel

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
    print(f"Partida Numero: {cuenta_partidas}")
    print(f"\nEl primer turno es de {jugador_inicial}")

    cuentaIntentos = 1
    inicio = time.time()
    solucion = random.choice(lista_palabras)
    solucion = solucion.upper()
    reemplazo = (("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"), ("Ú", "U"))
    for a, b in reemplazo:
        solucion = solucion.replace(a, b)   

    #print(solucion)##########Solucion Palabra a Adivinar###########

    arriesgo, lista_antigua, i, tablero = constantes_y_print_prewhile(longitud_palabra)

    # iteracion entre arriesgo y solucion
    while i != 5 and arriesgo != solucion:
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
    
    try:
        archivo = open("usuarios.csv", "r")
        archivo.close()
    except FileNotFoundError:
        archivo = open("usuarios.csv", "w")
        archivo.close

    login(1)
    jugador_1 = user
    if user:
        login(2)
        jugador_2 = user

    if jugador_1 and jugador_2:
        config = open("configuracion.csv", "r+")
        longitud_palabra, maximo_partidas, reinciar_archivo_partidas = obtener_config(
            config
        )
        config.close()

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
        partidas = open("partidas.csv", reinciar_archivo_partidas)
        lista_palabras_posibles = obtener_palabras(
            archivo1, archivo2, archivo3, archivoNuevo, longitud_palabra
        )

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

#-----------------------------------------------------------------------------------------------------------------#
#------- Modularizacion hecha por Lautaro Jovanovics, Nicolas Serrudo , Diego Lima y Jonathan Pistonesi.----------#
#-----------------------------------------------------------------------------------------------------------------#