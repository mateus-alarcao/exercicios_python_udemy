#1
lista = list()
for x in range(1,7):
    res = int(input())
    lista.append(res)
print(lista)


#2
lista = list()
for x in range(1,7):
    num = int(input())
    lista.append(num)
soma = lista[0] + lista[1] + lista[5]
print("soma: ", soma)
nume = int(input("num: "))
lista[5] = nume
for numeros in lista:
    print(numeros)


#3
cont = 0
lista = list()
for x in range(1, 11):
    res = int(input())
    lista.append(res)
    if res % 2 == 0:
        cont += 1
print(cont)
