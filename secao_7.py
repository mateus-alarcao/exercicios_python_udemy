"""
#1
def numero(inteiro):
    return inteiro * 2

#2
def extenso(data):
    dia, mes, ano = data.split("/")
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    dia = str(int(dia))
    mes_extenso = meses[int(mes) - 1]
    print(f"{dia} de {mes_extenso} de {ano}")

data = input()
extenso(data)

#3
lista_inteiros = list()
def lista(*inteiros):
    for x in range(0, 5):
        num = int(input())
        lista_inteiros.append(num)
    print(max(lista_inteiros))

lista()

"""