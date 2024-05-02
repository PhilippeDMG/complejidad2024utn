import math


def sum_divs1(n):
    """suma divisores del nro, sin contar el mismo"""
    if n < 2:
        return n
    divisores = {1}
    powers = set()
    # Itera desde 1 hasta la raíz cuadrada
    m = 0
    lim = math.ceil(n**0.5)
    last = n // lim
    if lim == last:
        divisores.add(last)
    while n % 2 == 0:
        m += 1
        n = n // 2
        powers.add(2**m)
        divisores.add(n)
    lim = math.ceil(n**0.5)
    no_pares = set()
    for i in range(3, lim, 2):
        # Si i es un divisor de n
        if n % i == 0:
            # Agrega i a la lista de divisores
            no_pares.add(i)
            # Si i no es la raíz cuadrada de n, agrega n/i también
            no_pares.add(n // i)
    # Retorna la lista de divisores ordenada
    for elemp in powers:
        for elemn in no_pares:
            divisores.add(elemp * elemn)
    divisores = divisores.union(powers).union(no_pares)
    return sum(divisores)


def factores_primos(n):
    i = 2
    factores = {}
    sqrtn = math.sqrt(n)
    while n > 1:
        if n % i == 0:
            if i in factores:
                factores[i] += 1

            else:
                factores[i] = 1
            n /= i
        else:
            i += 1
            if i > sqrtn:
                if factores == {}:
                    break
    return factores


def sum_divs2(n):
    """suma divisores del nro mediante sus factores primos"""
    if n == 1:
        return 1
    result = 1
    diccio_factores = factores_primos(n)
    if diccio_factores == {}:
        return 1
    for nro, frec in diccio_factores.items():
        result *= (nro ** (frec + 1) - 1) // (nro - 1)

    return int(result - n)


def repl_sdiv():
    print("input x to stop")
    inp = ""
    n = input("insert number\n")
    while n == "":
        n = input("insert number\n")
    n = int(n)
    while True:
        while n != 1:
            aux = sum_divs1(n)
            print(aux)
            n = aux
            inp = input()
            if inp == "x":
                break
        if n == 1:
            print(1)
        inp = input("input another number or exit with x\n")
        while inp == "":
            inp = input("input another number or exit with x\n")
        if inp == "x":
            break
        else:
            n = int(inp)
