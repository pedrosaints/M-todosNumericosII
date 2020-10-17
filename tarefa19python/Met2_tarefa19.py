import numpy as np
import math

#constantes
N = 4
yi = 0
yf = 1
deltaX = abs(yf-yi)/N

def dividir_dominio(yi,yf,deltaX,N):
    e = np.zeros(N-1)
    for j in range(1,N):
        e[j-1] = yi + j * deltaX;
    return e;    

def derivada_segunda(dominio,deltaX):
    r = (1/(deltaX**2))*dominio[0] - (2/(deltaX**2)+1)*dominio[1] + (1/(deltaX**2)*dominio)[2]
    return r
    
dominio = dividir_dominio(yi,yf,deltaX,N)    
print('DOMINIO: ')
print(dominio)

f = derivada_segunda(dominio,deltaX)
print('F\'\'(x): ')
print(f)

A = np.array([[-33,16,0],[16,-33,16],[0,16,-33]])
print('MATRIZ:')
print(A)

B = np.array([0,0,-16])
print('B:')
print(B)