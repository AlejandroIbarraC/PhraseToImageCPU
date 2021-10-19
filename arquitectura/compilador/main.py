import compiler.Compiler as Compiler
if __name__ == '__main__':
    # Open source file
    file = open("codigo.txt", "r", encoding="utf-8")
    string = file.read()
    file.close()

    # Compile stuff
    Compiler.compile_code(string)


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