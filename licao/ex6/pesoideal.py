#Faça um programa em Python que solicite ao usuário sua altura e sexo,
#calcule e imprima o seu peso ideal. Utilize a seguinte convenção:


class init:

    def steps(self):
        self.pesoideal()

    def pesoideal(self):

        print("Entrada:\n")

        h=float(input("Digite a altura em metros:  "))
        sexo=input("Digite o sexo da pessoa m/f: ")

        print("\nSaída:\n")

        if(sexo=='m'):
            peso=(72.7*h)-58
            print(f'O peso ideal dessa pessoa é :{peso:.2f}kg')
        if(sexo=='f'):
            peso=(62.1*h)-44.7
            print(f'O peso ideal dessa pessoa é :{peso:.2f}kg')
        print("\n")
        
start = init()
start.steps()