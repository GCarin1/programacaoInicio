
class init:
  def steps(self):
    self.eleitoral()
   
  def eleitoral(self,idade):

    idade=int(input("Digite a sua idade\n:"))
   
    
    match idade:
        case idade<16:
            print("não-eleitor")
        case idade>=18 and idade<=65:
            print("eleitor obrigatório")
        case idade<18 and idade>65:
            print("eleitor facultativo")
        
      
    
start = init()
start.steps()