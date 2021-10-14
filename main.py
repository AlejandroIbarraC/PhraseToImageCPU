from compiler import Compiler

if __name__ == '__main__':
    # Open source file
    file = open("source.txt", "r", encoding="utf-8")
    string = file.read()
    file.close()

    # Compile stuff
    Compiler.compile_code(string)

