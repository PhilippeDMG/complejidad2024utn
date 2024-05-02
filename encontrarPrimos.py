# Generar set con numeros primos menores a 100_000
# Algoritmo de la criba de Eratostenes

def encontrarPrimos(n):
    # Crear una lista de booleanos para representar si un número es primo o no
    # Inicializada con todos los números como primos (True)
    esPrimo = [True] * (n+1)
    esPrimo[0] = esPrimo[1] = False  # 0 y 1 no son primos

    # Empezar desde el primer número primo conocido (2)
    p = 2
    while p * p <= n:
        # Si es primo, marcar sus múltiplos como no primos
        if esPrimo[p]:
            for i in range(p * p, n+1, p):
                esPrimo[i] = False
        p += 1

    # Generar un set de números primos
    primos = set()
    for i in range(2, n+1):
        if esPrimo[i]:
            primos.add(i)

    return primos

print("Números primos menores a 100,000:")
print(encontrarPrimos(100000))
