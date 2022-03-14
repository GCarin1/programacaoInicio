#Escreva um programa em Python que obtenha uma temperatura em graus Celsius,
#calcule e mostre a respectiva temperatura nas escalas Fahrenheit e Kelvin. 

import time
class init:
  def steps(self):
    self.tconverter()
   
  def tconverter(self):
      while True:
        print(f"[Questao] Converter Celsius para Fahrenheit e Kelvin ")
        print(f"...")

        time.sleep(1)

        tc=float(input("\nDigite a Temperatura em C\nC:"))

        tf=float((1.8*tc)+32)
        tk=float((tc+273))

        time.sleep(1)

        
        print(f"\nA Temperatura em Celsius inserida foi :\n:C{tc}\n A conversao para Fahrenheit é :\n:F{tf}\n A conversao para Kelvin é :\n:K{tk}")
        

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