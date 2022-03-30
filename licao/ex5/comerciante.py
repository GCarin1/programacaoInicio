import math 

class init:
  def steps(self):
    self.vendas()
   
  def vendas(self):
    nome_prod=input("Digite o nome do produto\n:")
    valor=float(input("Digite o valor \nR$:"))
    

    if(valor<10):
        lucro=valor*1.7
        print(f'Lucro sobre o prduto{nome_prod} é de R$:{lucro}')
        
    elif(valor<=10<30):
        lucro=valor*1.5
        print(f'Lucro sobre o prduto{nome_prod} é de R$:{lucro}')

    elif(valor<=30<50):
        lucro=valor*1.4
        print(f'Lucro sobre o prduto{nome_prod} é de R$:{lucro}')

    elif(valor>=50):
        lucro=valor*1.3
        print(f'Lucro sobre o prduto{nome_prod} é de R$:{lucro}')

   
    

    
 
    
start = init()
start.steps()