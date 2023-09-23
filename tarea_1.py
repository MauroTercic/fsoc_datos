
# Ejercicio 1

def ejercicio_1():
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    return f"Hola, {nombre}. Tienes {edad} años."


# Ejercicio 2

def ejercicio_2():
    num = float(input(("Ingrese un número: ")))
    if num >= 1:
        return "El número es positivo."
    elif num == 0:
        return "El número es 0."
    else:
        return "El número es negativo."


# Ejercicio 3

def ejercicio_3():
    num_1 = float(input("Ingrese el primer número: "))
    num_2 = float(input("Ingrese el segundo número: "))

    if num_1 > num_2:
        return f"{num_1} es más grande que {num_2}"
    elif num_1 == num_2:
        return "Los 2 números son iguales"
    else:
        return f"{num_2} es más grande que {num_1}"
    

# Ejercicio 4

def ejercicio_4():

    notas = {tuple(range(0,61)): "F", tuple(range(60,70)): "D", tuple(range(70,80)): "C", tuple(range(80,90)): "B", tuple(range(90,101)): "A"}
    calificacion = int(input("Ingresa tu nota: "))

    for i in notas.keys():
        if calificacion in i:
            return notas[i]


# Ejercicio 5
'''
Un array es una forma de almacenar información en memoria de manera seguida.
La iteración son loops como el while o el for que sirven para hacer mas de una operación seguida hasta que se cumpla una condición

'''
