MaxInventario = 1000

class Producto:
    def __init__(self, marca, modelo, tipo, year, precio):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.year = year
        self.precio = precio

productos = []
CantProductos = 0

def cargar_productos():
    global CantProductos
    try:
        with open('inventario.txt', 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(',')
                productos.append(Producto(datos[0], datos[1], datos[2], int(datos[3]), float(datos[4])))
                CantProductos += 1
    except FileNotFoundError:
        with open('inventario.txt', 'w') as archivo:
            pass

def guardar_productos():
    with open('inventario.txt', 'w') as archivo:
        for producto in productos:
            archivo.write(f"{producto.marca},{producto.modelo},{producto.tipo},{producto.year},{producto.precio}\n")

def opcionmenu():
    print("Seleccione una opcion:")
    print("1. Ingresar auto")
    print("2. Editar auto")
    print("3. Buscar autos")
    print("4. Mostrar autos")
    print("5. Eliminar auto")
    print("0. Salir")
    return int(input("Opcion: "))

def procesar(opcion):
    if opcion == 1:
        ingresar()
    elif opcion == 2:
        editar(CantProductos)
    elif opcion == 3:
        buscar(CantProductos)
    elif opcion == 4:
        mostrar(CantProductos)
    elif opcion == 5:
        eliminar(CantProductos)
    elif opcion == 0:
        pass
    else:
        print("Opción inválida.")

def ingresar():
    global CantProductos
    if CantProductos < MaxInventario:
        marca = input("Ingrese la marca del auto: ")
        modelo = input("Ingrese el modelo del auto: ")
        tipo = input("Ingrese el tipo de auto: ")
        year = int(input("Ingrese el año: "))
        precio = float(input("Ingrese el precio: $"))
        productos.append(Producto(marca, modelo, tipo, year, precio))
        CantProductos += 1
        guardar_productos()

def editar(cantidadproductos):
    if cantidadproductos > 0:
        mostrar(cantidadproductos)
        index = int(input("Numero de auto a editar: ")) - 1

        print("Ingrese los nuevos datos")
        productos[index].marca = input("Marca del auto: ")
        productos[index].modelo = input("Modelo del auto: ")
        productos[index].tipo = input("Tipo del auto: ")
        productos[index].year = int(input("Año: "))
        productos[index].precio = float(input("Precio: $"))
        guardar_productos()
    else:
        print("No existen autos para editar.")

def eliminar(cantidadproductos):
    if cantidadproductos > 0:
        mostrar(cantidadproductos)
        index = int(input("Numero de auto a eliminar: ")) - 1
        del productos[index]
        global CantProductos
        CantProductos -= 1
        guardar_productos()
        print("Producto eliminado exitosamente.")
    else:
        print("No existen autos para eliminar.")

def buscar(cantidadproductos):
    if cantidadproductos > 0:
        print("1. Tipo")
        print("2. Modelo")
        print("3. Año")
        opcionb = int(input("Seleccione una opcion: "))
        procesarbuscar(opcionb)

        input_val = input("Seleccione una opcion: ")
        numero = input_val.isdigit()

        if numero:
            num = int(input_val)
            for i in range(CantProductos):
                if num == productos[i].year:
                    print(f"Auto {i+1}")
                    print(f"Tipo: {productos[i].tipo}")
                    print(f"Modelo: {productos[i].modelo}")
                    print(f"Año: {productos[i].year}")
        else:
            for i in range(CantProductos):
                if input_val == productos[i].tipo or input_val == productos[i].modelo:
                    print(f"Auto {i+1}")
                    print(f"Tipo: {productos[i].tipo}")
                    print(f"Modelo: {productos[i].modelo}")
                    print(f"Año: {productos[i].year}")

def procesarbuscar(opcion):
    if opcion == 1:
        marca()
    elif opcion == 2:
        modelo()
    elif opcion == 3:
        year()
    else:
        print("Opción inválida.")

def marca():
    for i in range(CantProductos):
        if all(productos[i].tipo != productos[j].tipo for j in range(i+1, CantProductos)):
            print(f"Tipo: {productos[i].tipo}")

def modelo():
    for i in range(CantProductos):
        if all(productos[i].modelo != productos[j].modelo for j in range(i+1, CantProductos)):
            print(f"Modelo: {productos[i].modelo}")

def year():
    for i in range(CantProductos):
        if all(productos[i].year != productos[j].year for j in range(i+1, CantProductos)):
            print(f"Año: {productos[i].year}")

def mostrar(cantidadproductos):
    if cantidadproductos > 0:
        for i in range(cantidadproductos):
            print(f"--Auto {i+1}--")
            print(f"Marca: {productos[i].marca}")
            print(f"Modelo: {productos[i].modelo}")
            print(f"Tipo: {productos[i].tipo}")
            print(f"Año: {productos[i].year}")
            print(f"Precio: ${productos[i].precio:.2f}")
    else:
        print("No existen productos para mostrar.")

