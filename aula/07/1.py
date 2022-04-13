idade = int(input('Digite a idade:'))

if idade<16:
    catergoria = 'Não eleitor'
elif idade>=18 and idade<=65:
    categoria = 'Eleitor obrigatório'
else:
    categoria = 'Eleitor facultativo'
    
print(f'Sua classe eleitorial é {categoria}')