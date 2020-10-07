import numpy as np
from math import fabs

def met_pot_inv (A,v0,erro):
    #P = decoLU(A)
    ynovo = 0
    vnovo = v0
    yvelho = ynovo
    vvelho = vnovo
    norm = np.linalg.norm(vvelho)
    xvelho = vvelho/norm
    vnovo = np.dot(np.linalg.inv(A),xvelho)
    #vnovo = solverLU(P,xvelho)
    ynovo = np.dot(xvelho,vnovo)
    while ((abs(ynovo-yvelho))/ynovo > erro):
        yvelho = ynovo
        vvelho = vnovo
        norm = np.linalg.norm(vvelho)
        xvelho = vvelho/norm
        vnovo = np.dot(np.linalg.inv(A),xvelho)
        #vnovo = solverLU(P,xvelho)
        ynovo = np.matmul(xvelho.T, vnovo)
        #ynovo = np.dot(xvelho,vnovo)
        
    #print((ynovo),(xvelho))
    return (1/ynovo),xvelho


def decoLU(A):
    L = np.copy(A)
    U = np.copy(A)
    
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
    y = np.copy(b)
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
    
def met_pot_desl(A,v0,erro,u):
    I = np.copy(A)
    for i in range(len(I)):
        for j in range(len(I)):
            if(i==j):
                I[i][j] = 1
            else:
                I[i][j] = 0

    #print (I*u)
    Alinha = A - (I*u)
    Inv = met_pot_inv(Alinha,v0,erro)
    y = Inv[0] + u
    x = Inv[1]
    return y,x
    
    

    
    
A = np.array([[5,2,1],[2,3,1],[1,1,2]])
print('Matriz:')
print(A)

v = np.array([1,1,1])
print('vetor0:')
print(v)
print('')
print('=================================')

print('met_pot_inv')
metodoinv = met_pot_inv (A,v,0.001)
print('autovalor')
print(metodoinv[0])
print('autovetor')
print(metodoinv[1])

print('')
print('TESTE')
print(np.dot(A,metodoinv[1]))
print(np.dot(metodoinv[0],metodoinv[1]))
print('')
print('=================================')

print('met_pot_desl')
metododesl = met_pot_desl (A,v,0.001,1)
print('autovalor')
print(metododesl[0])
print('autovetor')
print(metododesl[1])

print('')
print('TESTE')
print(np.dot(A,metododesl[1]))
print(np.dot(metododesl[0],metododesl[1]))    





