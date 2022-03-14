import time

class init:
  def retangulo(self):
    self.perimetro()
    self.area()

  
  def perimetro(self):
    while True:
        print(f"[Questao] Calcular o Perimetro do Retangulo")
        print(f"...")

        time.sleep(1)

        b=int(input("[Pergunta] Digite a base do Retangulo em cm\n"))
        
        h=int(input("[Pergunta] Digite a altura do Retangulo em cm\n"))
        
        p=2*(b+h)
        p=int(p)

        print(f"[Resposta] Perimetro do retangulo é {p} cm")
        time.sleep(1)
        print(f"===============================")

        continua = str(input('Deseja continuar a calcular o perimetro ? \n.Se sim\n-Digite (y)\n.Se nao\n-Digite (n)\n:'))

        if(continua=='y'):
            print(f"Preparando para proxima execução")
            print(f"================================")
            time.sleep(1)
        else:
                time.sleep(1)
                print(f"Finalizando programa...")
                break
  def area(self):
     while True:
        print(f"[Questao] Calcular a Area do Retangulo")
        print(f"...")

        time.sleep(1)

        b=int(input("[Pergunta] Digite a base do Retangulo em cm\n"))

        h=int(input("[Pergunta] Digite a altura do Retangulo em cm\n"))

        a=b*h
        a=int(a)
        
        print(f"[Resposta] Area do retangulo é {a} cm^2")
        time.sleep(1)
        print(f"===============================")

        continua =  str(input('Deseja continuar a calcular a area ? \n.Se sim\n-Digite (y)\n.Se nao\n-Digite (n)\n:'))

        if(continua=='y'):
            print(f"Preparando para proxima execução")
            print(f"================================")
            time.sleep(1)
        else:
                time.sleep(1)
                print(f"Finalizando programa...")
                break
       
start = init()
start.retangulo()