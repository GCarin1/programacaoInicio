#Aula5
import time

class init:
    def step(self):
        while True:
            print("Escolha qual calculo voce quer fazer")
            r=input("1-soma 2-subtracao 3-divisao 4-multiplicação\n:")
            r=int(r)
            
            if(r==1):self.soma()
            if(r==2):self.subtracao()
            if(r==3):self.divisao()
            if(r==4):self.multiplicacao()

            continua = str(input('Deseja continuar a calcular ? \ny-Sim n-Não\n:'))
            if(continua=='y'):
                print(f"Preparando para proxima execução")
                print(f"================================")
                time.sleep(1)
            else:
                time.sleep(1)
                print(f"Finalizando programa...")
                break

    def soma(self):
        print("Função Soma Selecionado\n")
        a=input("Digite o valor de A  \n:")
        a=int(a)
        b=input("Digite o valor de B  \n:")
        b=int(b)
        soma=a+b
        print(f'Soma de a com b é\n:{soma}')

    def subtracao(self):
        print("Função Subtração Selecionado\n")
        a=input("Digite o valor de A  \n:")
        a=int(a)
        b=input("Digite o valor de B  \n:")
        b=int(b)
        sub=a-b
        print(f'Subtração de a com b é\n:{sub}')

    def divisao(self):
        print("Função divisão Selecionado\n")
        a=input("Digite o valor de A  \n:")
        a=float(a)
        b=input("Digite o valor de B  \n:")
        b=float(b)
        divi=float(a/b)

        print(f'Divisão de a com b é\n:{divi:.2f}')

    def multiplicacao(self):
        print("Função multiplicação Selecionado\n")
        a=input("Digite o valor de A  \n:")
        a=int(a)
        b=input("Digite o valor de B  \n:")
        b=int(b)
        mult=a*b
        print(f'Multiplicação de a com b é\n:{mult}')
    
    

start=init()
start.step()