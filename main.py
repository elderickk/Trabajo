from funciones import *

def main():
    cargar_productos()
    opcion = -1
    while opcion != 0:
        opcion = opcionmenu()
        procesar(opcion)
    guardar_productos()

if __name__ == "__main__":
    main()