#Faça um programa em Python que calcule e mostre o valor do volume do
#tronco de uma pirâmide, para isso o programa deve solicitar ao usuário os
#valores da altura do tronco da pirâmide (h), o valor da base menor (Bmenor) e o
#da base maior (Bmaior) e calcular a seguinte expressão:

import time 

class init:
  def steps(self):
    self.volume_piramide()
   
  def volume_piramide(self):
      while True:
        h=float(input("Digite a Altura\n:"))
        Bmaior=float(input("Digite a base maior\n:"))
        Bmenor=float(input("Digite a base menor\n:"))
        volume = float(h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5))
        print(f'O volume da piramide é\n:{volume}')

        continua = str(input('Deseja continuar a calcular ? \n(Se sim)\n-(Digite (y))\n(Se nao)\n-(Digite (n))\n:'))
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