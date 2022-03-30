import math 

class init:
  def steps(self):
    self.segundo()
   
  def segundo(self):

    a=float(input("Digite o valor de A\n:"))
    b=float(input("Digite o valor de B\n:"))
    c=float(input("Digite o valor de C\n:"))

    x=((-b)+-math.sqrt(b**-(4*a*c))/2*a)
   
    equa=a*x**+(b*x)+c
    print(f'resultado da equação de segundo gradu é :{equa}')
 
    
start = init()
start.steps()