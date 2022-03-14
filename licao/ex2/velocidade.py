#Escreva um programa em Python que solicite ao usuário
#a distância entre duas cidades e o tempo de viagem. O
#programa deverá calcular e exibir a velocidade média de
#um carro que vai de uma cidade para outra.

import time

class init:
  def fisica(self):
    self.velocidade_media()
   

  
  def velocidade_media(self):

    while True:
        print(f"[Questao] Calcule a velocidade média de um carro que vai de uma cidade para outra")
        print(f"...")

        d=int(input("[Pergunta] Digite a distancia entre as cidades (Metros)\n:"))
        t=int(input("[Pergunta] Digite o tempo de viagem (Segundos)\n:"))
      
        time.sleep(1)

        velocidadeMedia=d/t
        velocidadeMedia=float(velocidadeMedia)
        
        print(f"[Resposta] A velocidade media de um carro que vai de uma cidade a outra é de \n{velocidadeMedia} m/s")
        continua = str(input('Deseja continuar a calcular a velocidade media ? \n.Se sim\n-Digite (y)\n.Se nao\n-Digite (n)\n:'))
    
        if(continua=='y'):
            print(f"Preparando para proxima execução")
            print(f"================================")

            time.sleep(1)

        else:
                time.sleep(1)
                print(f"Finalizando programa...")
                break
     
start = init()
start.fisica()