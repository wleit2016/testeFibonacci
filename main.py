if __name__ == '__main__':
    numeroTXT = input("Digite um numero: ")

    numero = int(numeroTXT)

    fib1 = 0
    fib2 = 1

    linha = "Serie Fibonacci -> "

    for i in range(0, numero):
        fib3 = fib1 + fib2
        linha = linha + str(fib1) + ", "
        fib1 = fib2
        fib2 = fib3

    print(linha)