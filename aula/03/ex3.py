

class init:

  def steps(self):
    self.ex3()

  def ex3(self):
    # inverssao de um numero digitado com python 
        num = int(input("Digite um número com três casas decimais\n:"))
        d1=num//100
        d2=num%100//10
        d3=num%10
        inverso=d3*100+d2*10+d1
        print(f'O inverso do muero digitado é\n{inverso}')
              
start = init()
start.steps()