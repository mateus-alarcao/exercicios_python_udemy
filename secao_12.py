"""
#1

while True:
    print("MANIPULAÇÃO DE ARQUIVO")
    print('=-' * 30)
    print("1: escrever algo no arquivo")
    print("2: apagar tudo o que está escrito no arquivo")
    print("3: ver o que está escrito no arquivo")
    print("4: sair")
    print('=-' * 30)
    res = int(input("o que quer fazer? "))

    if res == 1:
        print('=-' * 30)
        with open("arq.txt", 'a') as arquivo:
            arquivo.write(input("escreva algo no arquivo: ") + "\n")


    if res == 2:
        print('=-' * 30)
        with open("arq.txt", 'w') as arquivo:
            print("Conteúdo apagado com sucesso.")


    if res == 3:
        print('=-' * 30)
        with open("arq.txt", 'r') as arquivo:
            print(arquivo.read())

    if res == 4:
        break


#2

vogais = 'AEIOUaeiou'
tvogal = 0
tconso = 0

nome = str(input("digite noma do arquivo: "))

with open(nome, 'w') as arquivo:
    arquivo.write(str(input("escreva algo no arquivo: ")))

with open(nome, 'r') as arquivo:
    conteudo = arquivo.read()
    for palavras in conteudo:
        for letras in palavras:
            if letras in vogais:
                tvogal += 1
            else:
                tconso += 1
print(f'nesse arquivo há: {tvogal} vogais e {tconso} consoantes')


#3
nome = input("Digite o nome do arquivo: ")

# Escrevendo no arquivo (modo append)
with open(nome, 'a') as arquivo:
    texto = input("Escreva algo no arquivo: ")
    arquivo.write(texto + '\n')

# Lendo o arquivo para contar as linhas
with open(nome, 'r') as arquivo:
    linhas = arquivo.readlines()
    print(f'O arquivo tem {len(linhas)} linha(s).')
    arquivo.seek(0)
    print("arquivo: ", arquivo.read())
    
"""