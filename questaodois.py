num = int(input("Digite um número: "))

# Inicializando os valores iniciais da sequência de Fibonacci
fib1 = 0
fib2 = 1

# Verificando se o número informado é igual a algum dos valores iniciais da sequência
if num == fib1 or num == fib2:
    print(num, "pertence à sequência de Fibonacci.")
else:
    # Calculando a sequência de Fibonacci até que o próximo número seja maior do que o número informado
    while fib2 < num:
        fib_next = fib1 + fib2
        fib1 = fib2
        fib2 = fib_next

    # Verificando se o número informado é igual ao próximo número da sequência
    if num == fib2:
        print(num, "pertence à sequência de Fibonacci.")
    else:
        print(num, "não pertence à sequência de Fibonacci.")