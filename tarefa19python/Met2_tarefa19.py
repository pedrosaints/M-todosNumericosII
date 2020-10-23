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
        #print(U)
        #print(pivot)
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

def dividir_dominio(yi,yf,deltaX,N):
    e = np.zeros(N-1)
    for j in range(1,N):
        e[j-1] = yi + j * deltaX;
    return e;    

def solucao_exata(dominio):
    r = np.zeros(len(dominio))
    for j in range(len(r)):
        r[j] = (1/((math.e**(-1))-math.e))*((math.e**(-dominio[j]))-(math.e**(dominio[j])))
    return r

def derivada_segunda(dominio,deltaX):
    r = (1/(deltaX**2))*dominio[0] - (2/(deltaX**2)+1)*dominio[1] + (1/(deltaX**2)*dominio)[2]
    return r
    
dominio = dividir_dominio(yi,yf,deltaX,N)    
print('DOMINIO: ')
print(dominio)

#f = derivada_segunda(dominio,deltaX)
#print('F\'\'(x): ')
#print(f)

A = np.array([[- (2/(deltaX**2)+1),(1/(deltaX**2)),0,0,0,0,0],
[(1/(deltaX**2)),- (2/(deltaX**2)+1),(1/(deltaX**2)),0,0,0,0],
[0,(1/(deltaX**2)),- (2/(deltaX**2)+1),(1/(deltaX**2)),0,0,0],
[0,0,(1/(deltaX**2)),- (2/(deltaX**2)+1),(1/(deltaX**2)),0,0],
[0,0,0,(1/(deltaX**2)),- (2/(deltaX**2)+1),(1/(deltaX**2)),0],
[0,0,0,0,(1/(deltaX**2)),- (2/(deltaX**2)+1),(1/(deltaX**2))],
[0,0,0,0,0,(1/(deltaX**2)),- (2/(deltaX**2)+1)]])
print('MATRIZ:')
print(A)

B = np.array([0,0,0,0,0,0,-(1/(deltaX**2))])
print('B:')
print(B)     
   

#A = np.array([[(-20/0.125**6)+1,(15/0.125**6),(-6/0.125**6),(1/0.125**6),0,0,0],
#[(15/0.125**6),(-20/0.125**6)+1,(15/0.125**6),(-6/0.125**6),(1/0.125**6),0,0],
#[(-6/0.125**6),(15/0.125**6),(-20/0.125**6)+1,(15/0.125**6),(-6/0.125**6),(1/0.125**6),0],
#[(1/0.125**6),(-6/0.125**6),(15/0.125**6),(-20/0.125**6)+1,(15/0.125**6),(-6/0.125**6),(1/0.125**6)],
#[0,(1/0.125**6),(-6/0.125**6),(15/0.125**6),(-20/0.125**6)+1,(15/0.125**6),(-6/0.125**6)],
#[0,0,(1/0.125**6),(-6/0.125**6),(15/0.125**6),(-20/0.125**6)+1,(15/0.125**6)],
#[0,0,0,(1/0.125**6),(-6/0.125**6),(15/0.125**6),(-20/0.125**6)+1]])
#print('MATRIZ:')
#print(A)

#B = np.array([0,0,0,0,
#-(1/0.125**6),
#-((1/0.125**6)+(-6/0.125**6))
#,-((1/0.125**6)+(-6/0.125**6)+(15/0.125**6))])
#print('B:')
#print(B)     


P = decoLU(A)

X = solverLU(P,B)
print('X:')
print(X) 

solucao = solucao_exata(dominio)
print('SOLUCAO:')
print(solucao) 

teste = np.copy(X).astype('float')
for p in range (len(X)):
    teste[p]=np.dot(A[p],solucao) 
print('TESTE: A.X')
print(teste)     

