# Nome: Guilheme Carini 
# RGM: 20224435
# Prova A
#Faça um programa no Python que solicite ao usuário o salário bruto (sbruto) de um funcionário e, calcule
#e mostre o salário líquido (sliquido) a receber. Sabe-se que este é composto pelo salário bruto com desconto de 11%, e
#acrescido de gratificação, conforme a tabela a seguir


class init:
    
  def steps(self):
    self.salarios()
   
  def salarios(self):
      
        bruto=float(input("Digite o salário bruto R$: "))
        liqdo=float(((bruto*11)/100))
        print("\n")
      
        if(liqdo<1100):
            salario=(bruto-liqdo)+200
            print(f"Salário líquido a receber: R$ {salario:.2f}")
        
        elif(liqdo>=1100 and liqdo<1250):
            salario=(bruto-liqdo)+150
            print(f"Salário líquido a receber: R$ {salario:.2f}")
            
        elif(liqdo>=1250 and liqdo<1750):
            salario=(bruto-liqdo)+100
            print(f"Salário líquido a receber: R$ {salario:.2f}")
            
        elif(liqdo>=1750):
            salario=(bruto-liqdo)+75
            print(f"Salário líquido a receber: R$ {salario:.2f}")
    
 
start = init()
start.steps()