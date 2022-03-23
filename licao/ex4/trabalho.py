
import time

class init:
  def steps(self):
    self.trabalho()
   
  def trabalho(self):

        hinit=int(input("horario de inicio de trabalho\n:"))
        hfim=int(input("horario de saida de trabalho\n:"))
        hjornada=int(input("Digite a jornada de trabalho\n:"))
        n=int(hjornada-1)
        hrtrab=int(hfim-hinit)
        cporh=float('37.50')
        cporhextra=float('45.00')

        
        if(n<=hrtrab):
            
            print(f"Hora trabalhada é igual a \n:R${cporh}")
            val=float(hrtrab*cporh)
            print(f"Valor recebido sem hora extra é\n:R${val}")
           
        else:
            
            print(f"Hora trabalhada é igual a \n:R${cporhextra}")
            val=float(hrtrab*cporhextra)
            print(f"Valor recebido sem hora extra é\n:R${val}")
                
   
start = init()
start.steps()