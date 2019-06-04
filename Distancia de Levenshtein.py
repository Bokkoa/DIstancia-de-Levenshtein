import sys
from termcolor import colored
#Distancia de Levenshtein



P1 = input("Ingresar palabra 1: ")
P2 = input("Ingresar palabra 2: ")

C1 = list(P1)
C2 = list(P2)


Matrix = [[0 for x in range( len(C2)+2 )] for y in range(len(C1)+2 )]

#Visualizar palabra

for i in range (len(C1) ):
    Matrix[i+2][0] = C1[i]

for j in range(len(C2) ):
    Matrix[0][j+2] = C2[j]
    

for i in range (len(C1)+1):
    Matrix[i+1][1] = i

for j in range(len(C2)+1):
    Matrix[1][j+1] = j

#calcular a partir del campo 2

for i in range(len(C1)):
    for j in range(len(C2)):
        Dist1 = 0
        Dist2 = 0
        Dist3 = 0
        
        Dist1 = Matrix[i+1][j+2]+1
        Dist2 = Matrix[i+2][j+1]+1
        
        if(C1[i] == C2[j]):
            Dist3 = Matrix[i+1][j+1]+0
        else:
            Dist3 = Matrix[i+1][j+1]+1
            
        Matrix[i+2][j+2] = min(Dist1, Dist2, Dist3)


print('\n\n'.join(['| ' .join([ '{:6}'.format(item) for item in row]) 
      for row in Matrix]))        

     
