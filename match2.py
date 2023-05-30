import random

# 1. Pedir al usuario un número
num_usuario = int(input("Por favor, ingresa un número: "))
num_usuario_original = num_usuario

# Crear una nueva variable que es el doble del número ingresado por el usuario
num_doble = num_usuario * 2
num_doble_original = num_doble

# 3. Preguntar al usuario cuántas veces se realizará la resta
num_veces = int(input("¿Cuántas veces se realizará la resta? "))

# 4. Realizar la resta y 5. Guardar los resultados en un array
resultados = []
resultados_doble = []
numeros_generados = []
numeros_generados_doble = []
for _ in range(num_veces):
    # 2. Generar un número aleatorio
    num_aleatorio = random.randint(1, num_usuario // 2)
    num_aleatorio_doble = num_aleatorio * 2
    numeros_generados.append(num_aleatorio)
    numeros_generados_doble.append(num_aleatorio_doble)
    num_usuario -= num_aleatorio
    num_doble -= num_aleatorio_doble
    resultados.append(num_usuario)
    resultados_doble.append(num_doble)

# Imprimir los números generados y todos los resultados
print("\nNúmero usuario: ", num_usuario_original)
print("Números generados: ", numeros_generados)
print("Resultados: ", resultados)
print("\nNúmero doble: ", num_doble_original)
print("Números generados dobles: ", numeros_generados_doble)
print("Resultados dobles: ", resultados_doble)

# Comparar los arrays de resultados y resultados dobles
elementos_iguales = set(resultados) & set(resultados_doble)

suma_generados = 0
suma_generados_doble = 0

if elementos_iguales:
    print("\nHay elementos iguales en ambos arrays de resultados: ", elementos_iguales)
    indice_coincidencia_resultados = resultados.index(list(elementos_iguales)[0])
    indice_coincidencia_resultados_doble = resultados_doble.index(list(elementos_iguales)[0])
    suma_generados = sum(numeros_generados[:indice_coincidencia_resultados + 1])
    suma_generados_doble = sum(numeros_generados_doble[:indice_coincidencia_resultados_doble + 1])
    print("\nSuma de los números generados hasta la coincidencia en resultados: ", suma_generados)
    print("Suma de los números generados dobles hasta la coincidencia en resultados dobles: ", suma_generados_doble)
else:
    print("\nNo hay elementos iguales en ambos arrays de resultados.")
