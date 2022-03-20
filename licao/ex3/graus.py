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
    self.grauss()

  def grauss(self):
         #Vamos criar um programa que solicite um número real, calcule e que apresente:
    graus=float(input("Digite o número em graus \n:"))
    rad=float(math.radians(graus))
    sin=math.sin(rad)
    cos=math.cos(rad)
    tan=math.tan(rad)
    print(f'seno {sin}\ncosseno {cos}\ntangente {tan}')

start = init()
start.steps()