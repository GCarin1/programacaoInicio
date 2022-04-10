#Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas.
#Faça um programa em Python que receba o salário fixo do funcionário e o valor
#de suas vendas, calcule e mostre a comissão e o salário final do funcionário.

class init:

    def steps(self):
        self.salcom()
    def salcom(self):
        print("Entrada:\n")
        salarioFix=float(input("Digite o salário fixo: R$ "))
        vendaVal=float(input("Digite o valor da venda: R$ "))
        comissao=float((vendaVal/100)*4)
        salariofim=float(comissao+salarioFix)
        print("\n")
        print("Saída:\n")
        print(f'Comissão: R${comissao}')
        print(f'Salário final: R${salariofim}')
    
start = init()
start.steps()