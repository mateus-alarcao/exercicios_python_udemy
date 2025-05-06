"""
#1
print("você digitou: " ,int(input("digite numero inteiro ")))

#2
print("digite 3 valores inteiros")
soma = list()
for x in range(0, 3):
    num = int(input())
    soma.append(num)
print("soma dos numeros: ", sum(soma))

#3
soma = 0
for x in range(0, 3):
    num = int(input())
    quadrado = num ** 2
    soma += quadrado
print(soma)
"""