
#Escreva um programa em Python que solicite ao usuário
#o salário atual e mostre o salário acrescido de 5% de
#comissão

import time

class init:
  def steps(self):
    self.salario()
   
  def salario(self):
      while True:
        print(f"[Questao] Calcular a comissao em R$")
        print(f"...")

        time.sleep(1)

        salario=float(input("Digite o seu salario em R$"))
        
        comissao=float((salario*5)/100)
      
        salario_atual=salario+comissao
        salario_atual=float(salario_atual)\

        time.sleep(1)

        print(f"...")
        print(f"Sua comissao é R${comissao}")
        print(f"Seu salario mais a sua comissao é R${salario_atual}")

        time.sleep(1)

        continua = str(input('Deseja continuar a calcular a comissao ? \n.Se sim\n-Digite (y)\n.Se nao\n-Digite (n)\n:'))
        
        if(continua=='y'):
            print(f"Preparando para proxima execução")
            print(f"================================")
            time.sleep(1)
        else:
                time.sleep(1)
                print(f"Finalizando programa...")
                break
   
start = init()
start.steps()