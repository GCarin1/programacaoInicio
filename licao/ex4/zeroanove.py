


class init:
  def steps(self):
    self.zeroanove()
   
  def zeroanove(self):
      
        num=int(input("Digite um numero de 0 a 9\n:"))
        if(num<=9):

            print(f"numero é menor ou igual a nove")
            print(f"================================")
           
        else:
            
            print(f"número não é menor ou igual a nove")
                
   
start = init()
start.steps()