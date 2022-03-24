import math

class init:

  def steps(self):
    self.ex4()

  def ex4(self):
      
    a=float(input('Digite o angulo em graus \n: '))
    sombra = float(input('Digite o comprimento da sobra em metros\n: '))
    a=math.radians(a)

    h=sombra*math.tan(a)
    print(f'A altura do predio é {h:.2f}m') 


start = init()
start.steps() 