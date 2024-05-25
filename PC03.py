import random
import math

# Problema 1: Fracción como porcentaje
def calcular_porcentaje(fraccion):
    try:
        x, y = map(int, fraccion.split('/'))
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        porcentaje = (x / y) * 100
        if porcentaje < 1:
            return "E"
        elif porcentaje > 99:
            return "F"
        else:
            return f"{round(porcentaje)}%"
    except ValueError:
        return "Error: Asegúrate de que ambos valores sean enteros y que X sea menor o igual a Y."
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero."

# Problema 2: Lista de calificaciones
def obtener_calificaciones(calificaciones_str):
    try:
        calificaciones = [int(x) for x in calificaciones_str.split(',')]
        return calificaciones
    except ValueError:
        return "Error: Asegúrate de que todas las calificaciones sean números enteros."

# Problema 3: Clase Círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

# Problema 4: Clase Rectángulo
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

# Problema 5: Clase Alumno
class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.nota = None

    def display(self):
        print(f"Nombre: {self.nombre}, Registro: {self.registro}, Edad: {self.edad}, Nota: {self.nota}")

    def set_age(self, edad):
        self.edad = edad

    def set_nota(self, nota):
        self.nota = nota

# Problema 6: Clases Catálogo y Producto
class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Año: {producto.año}")

    def filtrar_por_año(self, año):
        return [producto for producto in self.productos if producto.año == año]

# Problema 8: Módulo de números aleatorios
def generar_numeros_aleatorios():
    numeros = [random.randint(0, 100) for _ in range(20)]
    return numeros

def mostrar_lista(lista):
    print("Lista:", lista)

def ordenar_lista(lista):
    lista.sort()
    return lista

# Problema 9: Módulo de operaciones
def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido."

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido."

def producto(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido."

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        return a / b
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero."
    except TypeError:
        return "Error: Tipo de dato no válido."

# Problema 10: Menú para cálculo de áreas
def menu_areas():
    while True:
        print("\nMenú de cálculo de áreas")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            radio = float(input("Introduce el radio del círculo: "))
            circulo = Circulo(radio)
            print(f"El área del círculo es: {circulo.calcular_area()}")
        elif opcion == "2":
            largo = float(input("Introduce el largo del rectángulo: "))
            ancho = float(input("Introduce el ancho del rectángulo: "))
            rectangulo = Rectangulo(largo, ancho)
            print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
        elif opcion == "3":
            lado = float(input("Introduce el lado del cuadrado: "))
            cuadrado = Rectangulo(lado, lado)
            print(f"El área del cuadrado es: {cuadrado.calcular_area()}")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    while True:
        print("\nMenú Principal")
        print("1. Calcular porcentaje de fracción")
        print("2. Obtener lista de calificaciones")
        print("3. Trabajar con clases (Círculo, Rectángulo, Alumno, Catálogo)")
        print("4. Generar y mostrar números aleatorios")
        print("5. Operaciones matemáticas")
        print("6. Menú para cálculo de áreas")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            fraccion = input("Introduce una fracción en el formato X/Y: ")
            resultado = calcular_porcentaje(fraccion)
            print("Resultado:", resultado)
        elif opcion == "2":
            calificaciones_str = input("Introduce una lista de calificaciones separadas por comas: ")
            calificaciones = obtener_calificaciones(calificaciones_str)
            if isinstance(calificaciones, list):
                print("Calificaciones:", calificaciones)
            else:
                print(calificaciones)
        elif opcion == "3":
            print("\nSubmenú Clases")
            print("1. Crear y mostrar información de un Alumno")
            print("2. Agregar y mostrar productos en un Catálogo")
            subopcion = input("Elige una opción: ")
            if subopcion == "1":
                nombre = input("Introduce el nombre del alumno: ")
                registro = input("Introduce el número de registro: ")
                alumno = Alumno(nombre, registro)
                edad = int(input("Introduce la edad del alumno: "))
                nota = float(input("Introduce la nota del alumno: "))
                alumno.set_age(edad)
                alumno.set_nota(nota)
                alumno.display()
            elif subopcion == "2":
                catalogo = Catalogo()
                while True:
                    nombre = input("Introduce el nombre del producto: ")
                    precio = float(input("Introduce el precio del producto: "))
                    año = int(input("Introduce el año del producto: "))
                    producto = Producto(nombre, precio, año)
                    catalogo.agregar_producto(producto)
                    continuar = input("¿Quieres agregar otro producto? (s/n): ")
                    if continuar.lower() != 's':
                        break
                catalogo.mostrar_productos()
                año_filtro = int(input("Introduce el año para filtrar productos: "))
                productos_filtrados = catalogo.filtrar_por_año(año_filtro)
                for producto in productos_filtrados:
                    print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Año: {producto.año}")
        elif opcion == "4":
            lista = generar_numeros_aleatorios()
            mostrar_lista(lista)
            lista_ordenada = ordenar_lista(lista)
            print("Lista ordenada:", lista_ordenada)
        elif opcion == "5":
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print("Suma:", suma(a, b))
            print("Resta:", resta(a, b))
            print("Producto:", producto(a, b))
            print("División:", division(a, b))
        elif opcion == "6":
            menu_areas()
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 7.")
