import random
import math

# Solicitamos al usuario que ingrese un número
x = input("Por favor ingresa un número: ")

# Validamos que el valor ingresado sea un número
try:
    x = int(x)
except ValueError:
    print("El valor ingresado no es un número válido.")
    exit()

while True:
    # Calculamos rangomax basándonos en la cantidad de dígitos del número ingresado
    rangomax = 10 ** len(str(x)) // 2

    # Creamos una lista vacía para almacenar nuestros números aleatorios
    arrayaleatorios = []

    # Inicializamos el valor máximo permitido para el primer número aleatorio
    max_value = rangomax

    # Generamos números aleatorios hasta que max_value sea menor o igual a 1
    while max_value > 1:
        # Generamos un número aleatorio en el rango (max_value // 2, max_value)
        rand_num = random.randint(max_value // 2, max_value)
        
        # Añadimos el número aleatorio a nuestra lista
        arrayaleatorios.append(rand_num)
        
        # Actualizamos max_value para la siguiente iteración
        max_value = rand_num - 1

    # Creamos un nuevo array basándonos en el número x y arrayaleatorios
    array_nuevo = []
    x_temp = x

    for num in arrayaleatorios:
        x_temp = x_temp - num
        array_nuevo.append(x_temp)

    # Creamos la variable 2x y el array de aleatorios dobles
    x_doble = 2 * x
    arrayaleatorios_dobles = [2 * num for num in arrayaleatorios]

    # Creamos el último array basado en 2x y arrayaleatorios_dobles
    array_nuevo_dobles = []
    x_doble_temp = x_doble

    for num in arrayaleatorios_dobles:
        x_doble_temp = x_doble_temp - num
        array_nuevo_dobles.append(x_doble_temp)

    # Comparamos los arrays "array_nuevo" y "array_nuevo_dobles"
    common_elements = set(array_nuevo) & set(array_nuevo_dobles)

    if common_elements:
        print("")
        print("Los arrays 'Nuevo Array' y 'Nuevo Array Dobles' tienen los siguientes elementos en común:", common_elements)

        # Encuentra el primer elemento en común
        common_element = list(common_elements)[0]
        
        # Encuentra el índice del elemento en común en cada array
        index_nuevo = array_nuevo.index(common_element)
        index_nuevo_dobles = array_nuevo_dobles.index(common_element)
        
        # Suma los elementos de arrayaleatorios y arrayaleatorios_dobles hasta el índice correspondiente
        sum_nuevo = sum(arrayaleatorios[:index_nuevo+1])
        sum_nuevo_dobles = sum(arrayaleatorios_dobles[:index_nuevo_dobles+1])
        
        print("")
        print("Array Aleatorios:", arrayaleatorios)
        print("Nuevo Array:", array_nuevo)

        print("")

        print("Array Aleatorios Dobles:", arrayaleatorios_dobles)
        print("Nuevo Array Dobles:", array_nuevo_dobles)

        print("")

        print("x = ",x)

        print("La suma de los elementos en 'Array Aleatorios' hasta la posición de la coincidencia en 'Nuevo Array' es:", sum_nuevo)

        print("")

        print("La suma de los elementos en 'Array Aleatorios Dobles' hasta la posición de la coincidencia en 'Nuevo Array Dobles' es:", sum_nuevo_dobles)


        print("diferencia = ", (sum_nuevo_dobles - sum_nuevo))

        break
    else:
        print("Los arrays 'Nuevo Array' y 'Nuevo Array Dobles' no tienen elementos en común. Intentando nuevamente...")
