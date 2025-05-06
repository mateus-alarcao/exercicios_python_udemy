# Dados:
alunos = ["joão", "lucas", "aline"]
prova1 = [70, 85, 90]
prova2 = [80, 79, 95]

# ➤ Crie um dicionário que associe cada aluno com a média das duas provas (arredondada).
# Resultado esperado (exemplo): {'joão': 75, 'lucas': 82, 'aline': 93}

# ➤ Sua missão: Usar zip(), sum(), round(), dict comprehension

final = {dado[0]: round((dado[1] + dado[2])/2) for dado in zip(alunos, prova1, prova2)}
print(dict(final))