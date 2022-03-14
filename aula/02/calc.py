
class init:
  def steps(self):
    self.ex()

  def ex(self):
      print("==========CALCULADORA==========\n")
      question1=input('adição?[y,n]\n')
      if(question1=='y'):
          num1=input('primeiro numero\n')
          num1=int(num1)
          num2=input('segundo numero\n')
          num2=int(num2)
          result1=num1+num2
          print(f'={result1}')
          
      
          question2=input('subtração?[y,n]\n')
      if(question2=='y'):
          num1=input('primeiro numero\n')
          num1=int(num1)
          num2=input('segundo numero\n')
          num2=int(num2)
          result1=num1-num2
          print(f'={result1}')
      
          question3=input('multiplicação?[y,n]\n')
      if(question3=='y'):
          num1=input('primeiro numero\n')
          num1=int(num1)
          num2=input('segundo numero\n')
          num2=int(num2)
          result1=num1*num2
          print(f'={result1}')
      
          question4=input('divisão?[y,n]\n')  
      if(question4=='y'):
          num1=input('primeiro numero\n')
          num1=int(num1)
          num2=input('segundo numero\n')
          num2=int(num2)
          result1=num1/num2
          print(f'={result1}')
      
         
        
        
        
        
start = init()
start.steps()