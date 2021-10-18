def limpiar_hex():
    inicial = "e3\\xa0\\x90\\x00\\xe3\\xa0\\x0c\\x01\\xe3\\xa0\\x10\\x00\\xe3\\xa0\\x7c\\x01\\xe3\\xa0\\x2f\\x87\\xe5\\x92\\x60\\x00\\xe3\\x56\\x00\\x01\\x0a\\x00\\x00\\x00\\xea\\xff\\xff\\xfa\\xe3\\xa0\\x2e\\x21\\xe5\\x92\\x60\\x00\\xe3\\x56\\x00\\x01\\x0a\\x00\\x00\\x08\\xe3\\xa0\\x2f\\x85\\xe5\\x92\\x60\\x00\\xe3\\x56\\x00\\x01\\x0a\\x00\\x00\\x17\\xe3\\xa0\\x2f\\x86\\xe5\\x92\\x60\\x00\\xe3\\x56\\x00\\x01\\x0a\\x00\\x00\\x1c\\xea\\x00\\x00\\x24\\xe3\\xa0\\x2f\\x81\\xe5\\x92\\x30\\x00\\xe3\\xa0\\x2f\\x82\\xe5\\x92\\x40\\x00\\xe3\\xa0\\x2f\\x83\\xe5\\x92\\x50\\x00\\xe1\\xa0\\x31\\x03\\xe1\\xa0\\x40\\x84\\xe0\\x83\\x30\\x04\\xe0\\x83\\x30\\x05\\xe1\\x59\\x00\\x00\\x0a\\x00\\x00\\x18\\xe5\\x91\\x60\\x00\\xe0\\x26\\x80\\x03\\xe5\\x87\\x80\\x00\\xe2\\x87\\x70\\x01\\xe2\\x81\\x10\\x01\\xe2\\x89\\x90\\x01\\xea\\xff\\xff\\xf6\\xe1\\x59\\x00\\x00\\x0a\\x00\\x00\\x0f\\xe5\\x91\\x60\\x00\\xe2\\x28\\x80\\xff\\xe5\\x87\\x80\\x00\\xe2\\x87\\x70\\x01\\xe2\\x81\\x10\\x01\\xe2\\x89\\x90\\x01\\xea\\xff\\xff\\xf6\\xe1\\x59\\x00\\x00\\x0a\\x00\\x00\\x06\\xe5\\x91\\x60\\x00\\xe2\\x86\\x80\\x02\\xe5\\x87\\x80\\x00\\xe2\\x87\\x70\\x01\\xe2\\x81\\x10\\x01\\xe2\\x89\\x90\\x01\\xea\\xff\\xff\\xf6\\xea\\xff\\xff\\xfe"
    lista = inicial.split("\\x")
    fin=[]
    for i in range(int(len(inicial)/4)):
        a=''.join(lista[i*4:(i+1)*4])
        fin.append(a)
    print('\n'.join(fin))

#limpiar_hex()

def codificacionXOR(a_string):

    ASCII_values = []
    for character in a_string:
        ASCII_values.append(ord(character))
    print(ASCII_values)
    HEX_values = []
    for i in ASCII_values:
        HEX_values.append(hex(i))
    print(HEX_values)
    llave = 3

    while (len(HEX_values)<256):
        HEX_values.append('0x20')

    codificado = []
    for x in HEX_values:
        codificado.append(hex(int(x,16) ^ llave))

    print(codificado)

    a="".join(codificado).split("0x")
    for i in range(len(a)):
        if len(a[i])==1:
            a[i]="0"+a[i]

    print('\n'.join(a))

    return codificado

def codificacionADD(a_string):

    ASCII_values = []
    for character in a_string:
        ASCII_values.append(ord(character))
    print(ASCII_values)
    HEX_values = []
    for i in ASCII_values:
        HEX_values.append(hex(i))
    print(HEX_values)
    llave = 2

    while (len(HEX_values)<256):
        HEX_values.append('0x20')

    codificado = []
    for x in HEX_values:
        if int(x,16) > 1:
            codificado.append(hex(int(x,16) - llave))
        else:
            codificado.append(hex(0x100 +int(x, 16) - llave))
    print(codificado)

    a="".join(codificado).split("0x")
    for i in range(len(a)):
        if len(a[i])==1:
            a[i]="0"+a[i]

    print('\n'.join(a))

    return codificado



def codificacionNOT(a_string):

    ASCII_values = []
    for character in a_string:
        ASCII_values.append(ord(character))
    print(ASCII_values)
    HEX_values = []
    for i in ASCII_values:
        HEX_values.append(hex(i))

    print(HEX_values)

    while (len(HEX_values)<256):
        HEX_values.append('0x1e')

    codificado = []
    for x in HEX_values:
        codificado.append(hex(int(x,16) ^ 0xff))

    print(codificado)

    a="".join(HEX_values).split("0x")
    for i in range(len(a)):
        if len(a[i])==1:
            a[i]="0"+a[i]

    print('\n'.join(a))

    return codificado

def ASCIItoHEXline(a_string):
    ASCII_values = []
    for character in a_string:
        ASCII_values.append(ord(character))
    print(ASCII_values)
    HEX_values = []
    for i in ASCII_values:
        HEX_values.append(hex(i))

    while (len(HEX_values)<64):
        HEX_values.append('0x20')

    a="".join(HEX_values).split("0x")
    for i in range(len(a)):
        if len(a[i])==1:
            a[i]="0"+a[i]

    lista_a_txt(a[1:],"ROM")




def crearimagen():
    datos= txtbin_a_listafloat("imagen")
    print(len(datos))
    lineas=[]
    for i in range(240):
        lineas.append("".join(datos[i*240:(i+1)*240]))
    print(len(lineas))
    lista_a_txt(lineas,"imagenbien")
    return 0


def lista_a_txt(lista,nombre):
    file = open(nombre+".txt", "w")
    file.write("\n".join(lista))
    file.close()

def txtbin_a_listafloat(nombre):
    file = open(nombre + ".txt", "r")
    datos = file.read().split("\n")
    file.close()
    datos = datos[:len(datos) - 1]
    return datos

#ASCIItoHEXline("ALICE WAS BEGINNING TO GET VERY TIRED OF SITTING BY HER SISTER ON THE ABCD EFGH IJKL MNOPQ RSTUV XYZ")

crearimagen()
