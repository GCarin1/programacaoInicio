#Escreva um programa em Python que calcule as duas
#raízes de uma equação de 2º grau ax²+bx+c, conhecendo os
#valores dos coeficientes da mesma (a, b, c). Suponha que
#as raízes são reais. Lembre-se que para calcular as duas
#raízes

import time

class init:
  def steps(self):
    self.raizes()
   
  def raizes(self):
    while True:
        
        print('[Questao] Calculando as raízes de uma equação de 2º grau\n')
        a = float(input('[Pergunta]Entre com o valor de a: '))
        b = float(input('[Pergunta]Entre com o valor de b: '))
        c = float(input('[Pergunta]Entre com o valor de c: '))

        D = (b**2-4*a*c)
        x1 = (-b+D**(1/2))/(2*a)
        x2 = (-b-D**(1/2))/(2*a)
        
        

        print(f'\n[Resposta] Valor de x1: {x1}')
        print(f'[Resposta] Valor de x2: {x2}')

        continua = input('Deseja continuar a calcular outras Raizes ? \n.Se sim\n-Digite (y)\n.Se nao\n-Digite (n)\n:')
        continua=str(continua)

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


