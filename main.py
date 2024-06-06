'''Esse comentado foi eu que fiz...

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


n = int(input("Informe o número de sequências de Fibonacci a ser calculada: "))

print(f'sequências de Fibonacci {n}: {fibonacci(n)}')'''

#Esse código aqui é do professor:

def calcular_fibonnacci(n):
    if n<=1:
        return n
    else:
        return calcular_fibonnacci(n-1)+ calcular_fibonnacci(n-2)

n = int(input("Informe o número de sequências de Fibonacci a ser calculada: "))

for fibo in range(n):
    print(calcular_fibonnacci(fibo))
