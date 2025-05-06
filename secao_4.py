"""
#1
numeros = list()
cont = 2
while cont != 0:
    cont -=1
    num = int(input())
    numeros.append(num)
print(max(numeros))

#2
num = int(input("digite numeros positivo: "))
if num > 0:
    raiz = num ** 0.5
    print(raiz)
else:
    print("erro, numero negativo. Tente novamente")

#3
num = int(input())
if num % 2 == 0:
    print('par')
else: print('impar')

"""