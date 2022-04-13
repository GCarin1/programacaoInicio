soma=0
contador=0
while True:
    num = int(input('Digite um número inteiro (0 para sair):'))
    soma=soma+num
    if num==0:
        break
    contador=contador+1
media = soma/contador
print(f'A média dos números digitados é:{media:.2f}')