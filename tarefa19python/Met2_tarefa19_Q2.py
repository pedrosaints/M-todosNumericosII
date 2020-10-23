import numpy as np
import math

def decoLU(A):
    L = np.copy(A).astype('float')
    U = np.copy(A).astype('float')
    
    #faço L ser um matriz identidade da msm ordem de A
    for i in range(len(L)):
        for j in range(len(L)):
            if(i==j):
                L[i][j] = 1
            else:
                L[i][j] = 0

    #fatoracao de gauss, preenchedo L
    for k in range(len(U) - 1):    
        pivot = U[k][k]
        for i in range(k+1, len(U)):
            n = U[i][k]
            divisor = n/pivot
            L[i][k] = -divisor
            for j in range (k,len(U)):
                U[i][j] = U[i][j] - U[k][j]*divisor
       
       
    #print(L)
    #print(U)
    return L,U

def solverLU(P,b):
    L = np.copy(P[0])
    U = np.copy(P[1])
    #print(L)
    #print(U)
    
    #L*y = b
    #fazendo y ser um vetor de msm tamanho de x
    y = np.copy(b).astype('float')
    for p in range (len(b)):
        y[p]=np.dot(L[p],y)
    
        
    #print(y)   
    #U*x = y
    x = np.copy(y)
    for p in range (len(x)):
        x[p]=1
    for j in range(len(y)-1,-1,-1):
        aux = 0
        for k in range(len(y)-1,j,-1):
            aux = aux + x[k]*U[j][k]
        x[j] = (y[j]-aux)/U[j][j]
    #print(x)  
    return x
    
    
#constantes
N = 8
yi = 0
yf = 1
deltaX = abs(yf-yi)/N
deltaY = abs(yf-yi)/N

def dividir_dominio(yi,yf,deltaX,N):
    x = yi
    y = yi
    e = np.zeros((N-1,N-1,2))
    for j in range(1,N):
        for k in range(1,N):
            e[j-1][k-1][0] = x + j * deltaX
            e[j-1][k-1][1] = y + k * deltaX
    return e;    


 
dominio = dividir_dominio(yi,yf,deltaX,N)    
print('DOMINIO: ')
print(dominio)

#produzindo a matriz A
A = np.zeros((((N-1)**2),((N-1)**2)))
for i in range(int(len(A)/2)):
    if(i%(N/2)!=0):
        A[i][0] = 1/(deltaX**2)  

for j in range(int(len(A)/2)):
    if(j%(N/2)!=0):
        A[0][j] = 1/(deltaX**2)        
        
for i in range(len(A)):
    for j in range(len(A)):
        if (j==0 and i>1):
            
            if(A[i][j]==1/(deltaX**2) ):
                k = j+1
                for p in range(i+1,len(A)):
                    A[p][k] = 1/(deltaX**2)
                    k = k+1
                    
        if (i==0 and j>1):
            
            if(A[i][j]==1/(deltaX**2) ):
                k = i+1
                for p in range(j+1,len(A)):
                    A[k][p] = 1/(deltaX**2)
                    k = k+1                
                
        if (i==j):
            A[i][j] = - 2*(1/(deltaX**2)+1/(deltaY**2))
        if ((i==j+1)or(i+1==j)):
            if (i%(N-1) != 0):
                if(i>j): 
                    A[i][j] = 1/(deltaX**2)
                    A[i-1][j+1] = 1/(deltaX**2)
  

    


print('MATRIZ:')
print(A)

B = np.zeros((N-1)**2)
for j in range(len(B)):
    B[j] = 8

print('B:')
print(B)    

P = decoLU(A)

X = solverLU(P,B)
print('X:')
print(X) 

#def solucao_exata(dominio):
#    r = np.zeros(len(dominio))
#    for j in range(len(r)):
#        r[j] = (1/((math.e**(-1))-math.e))*((math.e**(-dominio[j]))-(math.e**(dominio[j])))
#    return r

#solucao = solucao_exata(dominio)
#print('SOLUCAO:')
#print(solucao) 

teste = np.copy(X).astype('float')
for p in range (len(X)):
    teste[p]=np.dot(A[p],X) 
print('TESTE: A.X')
print(teste)        