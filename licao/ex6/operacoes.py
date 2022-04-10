#Faça um programa que solicite dois números reais e execute as operações
#listadas a seguir de acordo com a escolha do usuário:
#Escolha do usuário Operação
#1 Média entre os números digitados
#2 Diferença entre o maior e o menor número digitado
#3 Produto entre os números digitados
#4 Divisão do primeiro pelo segundo


class init:
    
    def steps(self):
        self.opera()

    def opera(self):

        print("Entrada:\n")
        n1=float(input("Digite o primeiro número: "))
        n2=float(input("Digite o segundo número: "))

        choice=int(input("[1] Média\n[2] Diferença maior-menor\n[3] Produto\n[4] Divisão n1/n2\nDigite uma opção: "))

        print("\nSaída:")
        if(choice>4 or choice<1):

            print(f'Opção invalida!')

        elif(choice==1):

            media=int((n1+n2)/2)
            print(f'Média = {media}')

        elif(choice==2):
            if(n1>n2):

                dif=n1-n2
                print(f'Diferença = {dif}')

            elif(n1<n2):

                dif=n2-n1
                print(f'Diferença = {dif}')

        elif(choice==3):
            
            prod=n1*n2
            print(f'Produto = {prod}')
        
        elif(choice==4):

            if(n1==0 or n2==0):
                print(f"Impossivel dividir por zero!!!")
            else:
                div=float(n1/n2)
                print(f'Divisão = {div:.3f}')

            
            
        
            
       
     
start = init()
start.steps()