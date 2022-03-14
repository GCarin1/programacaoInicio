import time
class init:
  def steps(self):
    self.dolar_real()
   
  def dolar_real(self):
      while True:
        print(f"[Questao] Cotacao do $ para R$")
        cotacaoD=(float(input('[Questao] Qual a cotacao do dolar para real hoje?\n:')))
        real=float(input('Quantia a ser convertida para dolar\n:'))

        convertD=real/cotacaoD
        
        print(f'[Resposta] Seus R${real} são ${convertD}')

        time.sleep(1)

        continua = str(input('Deseja continuar a converter ? \n.Se sim\n-Digite (y)\n.Se nao\n-Digite (n)\n:'))
        
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