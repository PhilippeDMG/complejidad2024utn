import math


def sum_divs1(n):
    """suma divisores del nro, sin contar el mismo"""
    orig = n
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
    if n == 1:
        return sum(divisores.union(powers))
    m = 0
    powers_3 = set()
    while n % 3 == 0:
        m += 1
        n = n // 3
        powers_3.add(3**m)
        divisores.add(n)
    if n == 1:
        for elemp3 in powers_3:
            for elemp in powers:
                if orig == elemp * elemp3:
                    continue
                divisores.add(elemp * elemp3)
        return sum(divisores.union(powers).union(powers_3))
    lim = math.ceil(n**0.5)
    no_pares = set()
    # print(powers_3, powers)
    # print("divisores", divisores)
    for i in range(5, lim, 6):
        # Si i es un divisor de n
        aux = i + 2
        if n % i == 0:
            # Agrega i a la lista de divisores
            no_pares.add(i)
            # Si i no es la raíz cuadrada de n, agrega n/i también
            no_pares.add(n // i)
        if n % aux == 0:
            no_pares.add(aux)
            no_pares.add(n // aux)
    # Retorna la lista de divisores ordenada
    for elemp in powers:
        for elemn in no_pares:
            divisores.add(elemp * elemn)
    for elemp3 in powers_3:
        for elemn in no_pares:
            divisores.add(elemp3 * elemn)
    for elemp in powers:
        for elemp3 in powers_3:
            divisores.add(elemp3 * elemp)

    for elemp in powers:
        for elemp3 in powers_3:
            for elemn in no_pares:
                divisores.add(elemp3 * elemp * elemn)
    divisores = divisores.union(powers).union(no_pares).union(powers_3)
    return sum(divisores)


def factores_primos(n):
    """algo"""
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
