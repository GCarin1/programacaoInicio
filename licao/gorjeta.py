#Escreva um programa em Python que leia um valor representando o gasto
#realizado por um cliente do restaurante ComaBem e visualize o valor total a ser pago,
#considerando os 10% do garçom

import time

class init:
  def steps(self):
    self.gorjeta()
   
  def gorjeta(self):
      while True:
        print(f"[Questao] Calcular a gorjeta do graçom R$")
        print(f"...")

        time.sleep(1)

        conta=float(input("\nDigite a conta do cliente em R$\nR$:"))
        
        gorjeta=float((conta/100)*10)

        somacg=conta+gorjeta
      
        

        time.sleep(1)

        
        print(f"\nA gorjeta do Garçom é :\nR${gorjeta}\n A conta mais a gorjeta de 10% é :\nR${somacg}")
        

        time.sleep(1)

        print(f"==============================")
        continua = str(input('[Repeticao]Deseja continuar a calcular a gorjeta ? \n.Se sim\n-Digite (y)\n.Se nao\n-Digite (n)\n:'))
        
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