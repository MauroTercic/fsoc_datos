
# Ejercicio 1
def ejercicio_1():
    materias = ["Economia", "Teoria politica y social 1", "Teoria politica y social 2", "Fundamentos 1", "Teoria sociologica", "Teoria y derecho constitucional",
                "Filosofia y metodos", "Metodologia de la investigacion 1", "Metodologia de la investigacion 2", "Historia Argetnina", "Historia contemporanea",
                "Historia latinoamericana"]
    for i in materias:
        print(i)


# Ejercicio 2
def ejercicio_2():
    nums = [5,8,9,4,5,85,4,51,32,17,478,4,9,48,15]
    return sum(nums)


# Ejercicio 3
def ejercicio_3():
    nums = [5,8,9,4,5,85,4,51,32,17,478,4,9,48,15]
    return max(nums)


# Ejercicio 4
def ejercicio_4():
    nums = [5,8,9,4,5,85,4,51,32,17,478,4,9,48,15]
    return sum(nums) // len(nums)


# Ejercicio 5
def ejercicio_5():
    dic = {"mauro": 7, "julieta": 8, "ivan": 4, "mercedes": 7, "facundo":6}
    nombre = input("Ingrese el nombre del estudiante: ").lower()

    if nombre in dic.keys():
        return dic[nombre]
    
    return "No existe tal estudiante"


# Ejercicio 6
def ejercicio_6():
    dic = {"manzana": 10, "banana": 2, "uva": 0, "naranja":14, "mandarina": 7}
    sum = 0
    for i in dic.values():
        sum += i
    return sum

