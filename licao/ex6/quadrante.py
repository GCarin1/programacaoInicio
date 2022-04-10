#Faça um programa que solicite as coordenadas de um ponto P, verifique e
#apresente na tela a qual quadrante pertence o ponto, desconsiderando a hipótese
#desse ponto estar sobre um dos eixos. Para tanto, lembre-se que:

class init:
    
    def steps(self):
        self.quadrante()

    def quadrante(self):

        print("Entrada:\n")
        x=float(input("Digite a coordenada x: "))
        y=float(input("Digite a coordenada y: "))
        

        print("\nSaída:")
        if(x>0 and y>0):print(f"O ponto p({x:.2f},{y:.2f}) pertence ao 1 quadrante")
        elif(x<0 and y>0):print(f"O ponto p({x:.2f},{y:.2f}) pertence ao 2 quadrante")
        elif(x<0 and y<0):print(f"O ponto p({x:.2f},{y:.2f}) pertence ao 3 quadrante")
        elif(x>0 and y<0):print(f"O ponto p({x:.2f},{y:.2f}) pertence ao 4 quadrante")
     
start = init()
start.steps()