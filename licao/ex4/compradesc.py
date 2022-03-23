
import time

class init:

    def steps(self):
        self.compra()
    def compra(self):
        comVal=input("Valor da sua compra\nR$:")
        comVal=float(comVal)
        desconto=float(0.2)

        if(comVal >= 200.00):
            descVal=comVal*desconto
            val=comVal-descVal
            descVal=float(descVal)
            print(f'sua compra é valida para o desconto\n-------------------\nSua compra mais o valor do desconto é\nR${val}')
        else:
            print(f'Sua compra não é valida para o desconto\n-------------------\nO valor da sua compra é\nR${comVal}')




        
        
                

start = init()
start.steps()