#Faça um programa que solicite ao usuário um número inteiro, verifique e se
#ele é positivo, negativo ou nulo.

class init:
    
    def posnulneg(num):

        print("Saída:\n")
        if(num==0):print(f"O númmero {num} é Nulo")
        elif(num>0):print(f"O númmero {num} é Positivo")
        elif(num<0):print(f"O númmero {num} é Negativo")

    print("Entrada:") 
    n=int(input("Digite um numero inteiro ")) 
    print(posnulneg(n))