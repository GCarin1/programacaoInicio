#Crie um programa em Python que solicite ao usuário a sua idade expressa
#em anos, meses e dias (variáveis separadas). Calcule e mostre a idade expressa
#apenas em dias. Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.
import time 

class init:
  def steps(self):
    self.idadedm()
   
  def idadedm(self):
      while True:
        ano=int(input("Digite a sua idade\n:"))
        meses=int(input("Digite meses desde o seu aniversario\n: "))
        dias=int(input("Digite desde o seu aniversario\n:"))

        cal=int((ano*360)+(meses*30)+dias)

        print(f"Sua idade em dias é \n:{cal} dias")


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