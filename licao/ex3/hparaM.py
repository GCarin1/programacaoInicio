#Crie um programa em Python que solicite o valor em horas para o usuário,
#calcule e mostre o valor em minutos, sabendo que 1 hora tem 60 minutos

import time 

class init:
  def steps(self):
    self.hparam()
   
  def hparam(self):
      while True:
        h=int(input("Digite a quantidade de Horas \n:"))
        m=h*60
        print(f'covertendo Horas para minuto é \n:{m} m')

        continua = str(input('Deseja continuar a calcular  ? \n(Se sim)\n-(Digite (y))\n(Se nao)\n-(Digite (n))\n:'))
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