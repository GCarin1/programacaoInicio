#Faça um programa que lê as duas notas parciais obtidas por um aluno numa
#disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos

class init:
    
    def steps(self):
        self.conceito()

    def conceito(self):

        print("Entrada:\n")
        nota1=float(input("Digite a primeira nota parcial: "))
        nota2=float(input("Digite a segunda nota parcial: "))
        media=float(nota1+nota2)/2

        print("\nSaída:")
        if(media<4):print("Conceito: E\nMensagem: REPROVADO")
        elif(media>=4 and media<=5.9):print("Conceito: D\nMensagem: REPROVADO")
        elif(media>=6 and media<=7.4):print("Conceito: C\nMensagem: APROVADO")
        elif(media>=7.5 and media<=8.9):print("Conceito: B\nMensagem: APROVADO")
        elif(media>=9 and media<=10):print("Conceito: A\nMensagem: APROVADO")
     
start = init()
start.steps()