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

def criar_sistema():

    #criando a matriz K, formulas resumidas
    #d = K11 = K22
    #o = K12 = K21
    d = (8/(3*8*N))+(N)
    o = (4/(3*8*N))-(N)

    a = np.zeros(((N-1),(N-1)))  
    b = np.zeros((N-1)) 
    
    for i in range(N - 1):
        for j in range(N - 1):
            if (i == j):
                a[i][j] = d+d
                if(i > 0):
                    a[i][j-1] = o
                    a[i-1][j] = o
        if (i == (N - 2)):
            b[i] = -o
    
    return a,b
    
dominio = dividir_dominio(yi,yf,deltaX,N)    
print('DOMINIO: ')
print(dominio)

P = criar_sistema()
A = P[0]
print('MATRIZ:')
print(A)

B = P[1]
print('B:')
print(B)     

P = decoLU(A)

X = solverLU(P,B)
print('X:')
print(X) 

solucao = solucao_exata(dominio)
print('SOLUCAO:')
print(solucao) 

erro = np.copy(X).astype('float')
for p in range (len(X)):
    erro[p]= math.fabs(X[p]-solucao[p])/X[p]
print('ERRO RELATIVO:')
print(erro) 


teste = np.copy(X).astype('float')
for p in range (len(X)):
    teste[p]=np.dot(A[p],X) 
print('TESTE: A.X')
print(teste)     

