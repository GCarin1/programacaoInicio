# Nome: Guilheme Carini 
# RGM: 20224435
# Prova A
import math

class init:
    
  def steps(self):
    self.compvol()
   
  def compvol(self):
      raio=float(input("Digite o raio da esfera em cm: "))
      
      c=float(2*math.pi*raio)
      v=float((4*(math.pi*raio**3))/3)
      print("\n")
        
      print(f"Comprimento da circunferencia da esfera: {c:.2f} cm²")
      print(f"Volume da esfera: {v:.2f} cm³")
      

    
        
start = init()
start.steps()