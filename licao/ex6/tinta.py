#Faça um programa em Python para uma loja de tintas. O programa deverá
#pedir o tamanho em metros quadrados da área a ser pintada. Considere que a
#cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
#vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
#quantidades de latas de tinta a serem compradas e o preço total.

import math

class init:
    
    def steps(self):
        self.tintas()

    def tintas(self):

        print("Entrada:\n")

        a=float(input("Digite a área a ser pintada (em m^2): "))
        math.ceil(a)
        lataporM=int(3*18)
        latas=math.ceil(a/lataporM)
        val=float(latas*80)
        print("Saída:\n")
        print(f'Você precisa comprar {latas} latas')
        print(f'O valor total a pagar será de R$ {val:.2f}')


        
        
start = init()
start.steps()