#implementação do
#Input
#Print f
#armazenamento de variaveis str e int
#calculo de media

class init:
  def steps(self):
    self.ex2()
    #self.respostas()

  def ex2(self):
      
        nome=input('Digite seu nome\n')
        disciplina=input('Digite a disciplina\n')
        nota1=input('Digite nota 1\n')
        nota1=int(nota1)
        nota2=input('Digite nota 2\n')
        nota2=int(nota2)
        
        media=(nota1+nota2)/2
        
        if(media>6):
            print(f'Voce foi aprovado Sua media é {media}')
        else:
            print(f'Voce foi reprovado Sua media é {media}, precisa fazer AF\n')
            af=input('Qual sua nota AF\n')
            af=int(af)
            if(nota1<nota2):
                media=nota2/af
                if(media<6):
                    print(f'Aluno {nome}, do curso {disciplina}, foi reprovado com media de {media}')
                else:
                    print(f'Aluno {nome}, do curso {disciplina}, foi aprovado com media de {media}')
            else:
                media=nota1/af
                if(media<6):
                    print(f'Aluno {nome}, do curso {disciplina}, foi reprovado com media de {media}')
                else:
                    print(f'Aluno {nome}, do curso {disciplina}, foi aprovado com media de {media}')   
        
  #def respostas(self)          
          
start = init()
start.steps()