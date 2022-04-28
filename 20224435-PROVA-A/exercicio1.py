# Nome: Guilheme Carini 
# RGM: 20224435
# Prova A

class init:
    
  def steps(self):
    self.compraAli()
   
  def compraAli(self):
      item1=float(input("Digite o valor do primeiro item em dólares US: "))
      item2=float(input("Digite o valor do primeiro item em dólares US: "))
      cotacao=float(input("Digite a cotação do dólar hoje: R$ "))
      print("\n")
      calc=float(item1+item2)*cotacao
      
      print(f"Valor a ser pago em reais: R$ {calc:.2f}")

    
        
start = init()
start.steps()