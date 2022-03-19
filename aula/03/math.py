# icomandos do import math para equações matematicas no python
#math.fabs(x) Retorna o valor absoluto, não negativo de x.
#math.floor(x) Retorna o maior número inteiro menor ou igual a x.
#math.ceil(x) Retorna o menor número inteiro maior ou igual a x
#math.sqrt(x) Retorna a raiz quadrada de x.
#math.trunc(x) Retorna a parte inteira de x.
#math.factorial(x) Retorna o produto de um inteiro x e todos os inteiros positivos menor que x. 
#math.radians(x) Retorna o valor da conversão de um ângulo de graus em radianos.
#math.sin(x) Retorna um valor representando o seno de um ângulo x.
#math.cos(x) Retorna um valor representando o cosseno de um ângulo x.
#math.tan(x) Retorna um valor representando a tangente de um ângulo x.
#math.asin(x) Retorna o arco-seno de um valor numérico.
#math.acos(x) Retorna o arco-cosseno de um valor numérico.
#math.atan(x) Retorna o arco-tangente de um valor numérico.
#math.hypot(x,y) Retorna a hipotenusa dos números (catetos) fornecidos.
#math.log(x,[base]) Retorna o log de um dado número x na base em questão.
#math.pow(x,y)Retorna o valor de x elevado à potência y Se quisermos o resultado em inteiro, devemos usar a função embutida de Python, pow(), ou o operador **.
#math.pi Retorna o valor do número pi

import math

class init:

  def steps(self):
    self.math()

  def math(self):
         #Vamos criar um programa que solicite um número real, calcule e que apresente:
    num=int(input("Digíte um número\n:"))
    
    absoluto=int(math.fabs(num))
    inteiro=int(math.trunc(num))
    raiz2=int(math.sqrt(absoluto))
    raiz3=num**2
   #fatorial=int(math.factorial(math.fabs(inteiro)))
    

    print(f'Resultado ao quadrado \n:{raiz2}')
    print(f'Resultado absoluto \n:{absoluto}')
    print(f'Resultado inteiro \n:{inteiro}')
    print(f'Resultado inteiro \n:{raiz3}')
    #print(f'Resultado fatorial \n:{fatorial}')


       
    

        
              
start = init()
start.steps()