# Nome: Guilheme Carini 
# RGM: 20224435
# Prova A
class init:
    
  def steps(self):
    self.sala()
   
  def sala(self):
      
    qtdAluno=int(input("Digite a quantidade de alunos da turma: "))
    print("\n")
    
    for i in range(qtdAluno):
        i=i+1
        x=0
        y=0
        
        medias=float(input(f"Digite a  media  do {i}° aluno: "))
        if(medias>=6):
            x=x+1
        elif(medias>=1 or medias<6):
            y=y+1
        mediageral=float(medias/qtdAluno)
        
               
    print(f"Quantidade de aprovados: {i} alunos")
    print(f"Média geral dos alunos: {mediageral:.2f} alunos")
    print(f"Quantidade de avaliação final: {i} alunos")
        
        
            
        
        
        
    

    
        
start = init()
start.steps()