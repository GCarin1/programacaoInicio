
class init:
  def steps(self):
    self.ex()

  def ex(self):
        nome='guilheme '
        nota=10
        
        
        print(f'A nota de {nome} foi {nota}') # F print 
        print('A nota de ',nome,'foi',nota) # virgula
        
        nota=str(nota)
        print('A note de '+nome+'foi '+nota)
        
        
        
start = init()
start.steps()