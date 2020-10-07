import numpy as np
import math


def met_calc_H( A, i, n):
    w = np.zeros(n)
    wlinha = np.zeros(n)
    e = np.zeros(n)
    for j in range(i+1,n):
        w[j] = A[j][i]
    Lw = comprimento(w)
    wlinha[i+1] = Lw
    N = w - wlinha
    no = N / comprimento(N)
    #criando identidade
    I = np.zeros((n,n))
    for j in range(n):
        I[j][j]=1
    aux = np.zeros((1,n))
    for j in range(n):
        aux[0][j] = no[j]
    H = I - 2 *(TranspostaVetor(no).dot(aux))
    return H
    
def met_householder(A,n):
    #H = I
    H = np.zeros((n,n))
    for j in range(n):
        H[j][j]=1
    A_ant = A
    for i in range(0,n-2):
        H_atual = met_calc_H( A_ant, i, n)
        A_atual = multiplica( multiplica(H_atual, A_ant), H_atual)
        A_ant = A_atual
        H = H.dot(H_atual)
    Ã = A_atual
    return(Ã,H)

def comprimento(w):
    return math.sqrt(sum( [ w.dot(w) ] ))

def TranspostaVetor(vetor):
    n = len(vetor)
    T = np.zeros((n,1))
    for i in range(n):
        T[i][0]=vetor[i]
    return T
    
    n = len(matriz)
    T = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            T[i][j]=matriz[j][i]
    return T    

def multiplica(m1, m2):
    n = len(m1)
    if n != len(m2):
        print("erro dimensão")
        return None
    result = np.zeros((n,n))
    for i in range(n):
        for k in range(n):
            somatorio = 0
            for j in range(n):
                somatorio += m1[i][j] * m2[j][k]
            result[i][k] = somatorio
    return result

def met_pot_regular (A,v0,erro):
    ynovo = 0
    vnovo = v0
    yvelho = ynovo
    vvelho = vnovo
    norm = np.linalg.norm(vvelho)
    xvelho = vvelho/norm
    vnovo = np.dot(A,xvelho)
    ynovo = np.dot(xvelho,vnovo)
    while ((abs(ynovo-yvelho))/ynovo > erro):
        yvelho = ynovo
        vvelho = vnovo
        norm = np.linalg.norm(vvelho)
        xvelho = vvelho/norm
        vnovo = np.dot(A,xvelho)
        ynovo = np.dot(xvelho,vnovo)
    return(ynovo),(xvelho)
   
    
A = np.array([[40,8,4,2,1],[8,30,12,6,2],[4,12,20,1,2],[2,6,1,25,4],[1,2,2,4,5]])
print('MATRIZ:')
print(A)

print('QUESTAO 1')
print('METODO DE HOUSEHOLDER')
metodoHH = met_householder(A,5)
print('')
print('Ã: ')
print(metodoHH[0])
print('')
print('H: ')
print(metodoHH[1])
print('')
print('')
print('QUESTAO 3')
print('METODO DA POTENCIA REGULAR EM Ã')
v = np.array([1,1,1,1,1])
metodo = met_pot_regular (metodoHH[0],v,0.001)
print('autovalor')
print(metodo[0])
print('autovetor')
print(metodo[1])
print('')
print('TESTE')
print(np.dot(metodoHH[0],metodo[1]))
print(np.dot(metodo[0],metodo[1]))   

print('')
print('')
print('QUESTAO 4 E 5')
print('AUTOVALOR DE A')
print(metodo[0])
print('')
print('AUTOVETOR DE A')
print(np.dot(metodoHH[1],metodo[1]))   

print('')
print('TESTE')
print(np.dot(A,np.dot(metodoHH[1],metodo[1])))
print(np.dot(metodo[0],np.dot(metodoHH[1],metodo[1])))   




