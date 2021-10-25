# Python 3 program for Bresenham’s Line Generation
# Assumptions :
# 1) Line is drawn from left to right.
# 2) x1 < x2 and y1 < y2
# 3) Slope of the line is between 0 and 1.
# We draw a line from lower left to upper
# right.


# function for line generation
import math
import sys
sys.setrecursionlimit(10000)

def txt_a_Lista(nombre):
    file = open(nombre + ".txt", "r")
    datos = file.read().split("\n")
    datos=[int(x, 16) for x in datos]
    file.close()
    return datos



def saltarlinea():
    global Y , X
    Y += 6
    X = 0
    verificarCampo(X, wordIndex)

def finlinea():
    global wordIndex
    if ListaLetras[wordIndex]==32:
        wordIndex += 1
    saltarlinea()


def siguienteLetra():
    global X, wordIndex
    X += 6
    wordIndex += 1
    if wordIndex == cantidadLetras:
        firmar()
    else:
        comprobarFinLinea()

def escribirLetra():
    global X,wordIndex
    if ListaLetras[wordIndex] == 32:
        X += 6
        wordIndex += 1
        verificarCampo(X,wordIndex)
    else:
        siguienteLetra()

def comprobarFinLinea():
    if X >= 240:
        finlinea()
    else:
        escribirLetra()


def verificarCampoLoop(x, wordindex):
    while x<=240:
        if x==240:
            saltarlinea()
            break
        elif ListaLetras[wordindex]==32:
            comprobarFinLinea()
            break
        else:
            if (wordindex+1)==cantidadLetras:
                comprobarFinLinea()
                break
            else:
                x+=6
                wordindex+=1



def terminar():
    yTotal = Y
    cantidadBits= yTotal * 240 + cantidadLetras * 8 + 2 + 1
    cantidadBloques = yTotal * 240 + cantidadLetras  + 2 + 1
    bitsRepresentacion= (math.log(cantidadBloques,2))
    if (bitsRepresentacion-int(bitsRepresentacion)) == 0:
        bitsRepresentacion=int(bitsRepresentacion)
    else:
        bitsRepresentacion=int(bitsRepresentacion)+1
    print("Datos obtenidos para la memoria:")
    print("cantidad de letras de 8 bits: ", cantidadLetras)
    print("cantidad de lineas en y con X=240: ", yTotal)
    print("total de bits necesarios para la imagen: ", yTotal * 240)
    print("1 bit para el switch de inicio del sistema: ")
    print("1 bit para indicar escritura en el GPIO: ")
    print("1 bit para indicar el valor del bit de la imagen en el GPIO")
    print("tamaño total de la memoria en bits: ", cantidadBits)
    print("tamaño total de bloques de memoria: ", cantidadBloques)
    print("bits necesarios para representar el tamaño de memoria: ", bitsRepresentacion)

def firmar():
    global X,Y
    if X==240:
        Y=+6
    terminar()


def verificarCampo (x,wordindex):
    if wordindex >= cantidadLetras:
        firmar()
    else:
        verificarCampoLoop(x,wordindex)


wordIndex=0
X=0
Y=0
ListaLetras = txt_a_Lista("ROM")
cantidadLetras = len(ListaLetras)





verificarCampo(X,wordIndex)














