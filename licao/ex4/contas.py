
class init:

    def steps(self):
        self.contas()
    def contas(self):

        agua=int(input(f'Qual o valor da conta de água\n:R$'))
        luz=int(input(f'Qual o valor da conta de luz\n:R$'))
        gas=int(input(f'Qual o valor da conta de gas\n:R$'))
        aluguel=int(input(f'Qual o valor da conta de aluguel\n:R$'))
        condominio=int(input(f'Qual o valor da conta de condominio\n:R$'))
        alimentacao=int(input(f'Qual o valor da conta de alimentação\n:R$'))
        Internet=int(input(f'Qual o valor da conta de internet\n:R$'))
        outros=int(input(f'Qual o valor da conta de outros fins\n:R$'))
        salario=int(input(f'Qual o salario mensal\n:R$'))

       
        contasS=int((agua+luz+gas+aluguel+condominio+alimentacao+Internet+outros))
        
        sobra=int(salario-contasS)
        invest=int(sobra*0.5)
        

        if(salario>contasS):
            anoI=invest*12
            anoI=int(anoI)
            print(f'Seu salario é maior que as contas a serem pagas\n sobra R${sobra} do seu salario')
            print(f'Poderá ser investido por mês R${invest}, seu investimento anual é R${anoI}')
        else:
            divida=sobra*(-1)
            divida=int(divida)
            dividaA=divida*12
            dividaA=int(dividaA)
            print(f'Seu salario não paga as contas\nSeu gasto além do salario é \nR${divida}')
            print(f'Sua divida anula é de \nR${dividaA}')

       


        


start = init()
start.steps()