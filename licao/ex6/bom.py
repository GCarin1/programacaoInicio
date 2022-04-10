#Faça um programa que solicite o nome da pessoa e que horas são (apenas
#horas). Posteriormente mostre na tela uma mensagem de “Bom dia”, “Boa tarde” ou
#“Boa noite” ao usuário. Para tanto, considere que:

class init:
    
    def steps(self):
        self.bom()

    def bom(self):

        print("Entrada:\n")
        nome=str(input("Qual seu nome?: "))
        hr=int(input("Que horas são [0-23]?: "))
        

        print("\nSaída:")
        if(hr<0 or hr>23):print(" horario não é valida")
        elif(hr>=5 and hr<=12):print(f"Bom dia {nome}")
        elif(hr>=13 and hr<=18):print(f"Bom tarde {nome}")
        elif(hr>=19 and hr<=4):print(f"Boa noite {nome}")
     
start = init()
start.steps()