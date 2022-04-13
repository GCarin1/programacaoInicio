soma = 0
for i in range(3):
    nota = float(input(f'Digite a {i+1}° nota:'))
    soma = soma+nota
    
media = soma/3
print(f'A média do aluno é {media}')