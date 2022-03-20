#Escreva um programa em Python para calcular o valor de uma prestação em
#atraso (prestacao). Para isso, obtenha o valor da prestação (valorPrestacao), a
#porcentagem de multa pelo atraso (multa) e a quantidade de dias de atraso
#(qtdeDias)

import time 

class init:
  def steps(self):
    self.prestacao()
   
  def prestacao(self):
      while True:
        valorPrestacao=float(input("Qual o valor da prestacao\n:"))
        multa=int(input("porcentagem da multa por atraso\n:%"))
        qtdeDias=int(input("Quantidade de dias em Atraso\n:"))
        prestação = valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

        print(f"Sua prestacao por multa de atraso é \n:{prestação}")


        continua = str(input('Deseja continuar a calcular ? \n-(Digite (y))\n-(Digite (n))\n:'))
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