import numpy as np
import math

#constantes
t0 = 0
v0 = 3
y0 = 150
k = 0.5
m = 0.5
g = 10

#deltat
dt1 = 0.1
dt2 = 0.01
dt3 = 0.001
dt4 = 0.0001

#F(S(t),t)
def F(G,Vi,K,M):
    Vii = -G - ((K/M)*Vi)
    return (Vii,Vi)
    
#somente para problema de queda, pois o laço ira parar com y > 0    
def Euler_Explic(T0,V0,Y0,DeltaT,K,M,G):
    #contador de passo
    cont = 0
    #variaveis da altura maxima
    Ymax = Y0
    Tmax = T0
    Y = Y0
    V = V0
    T = T0
    while (Y > 0):
        cont = cont + 1
        #pego o Scont com base no Scont-1
        aux = F(G,V,K,M)
        V =  V + DeltaT*aux[0]
        Y = Y +DeltaT*aux[1]
        T = T + DeltaT
        if (Y > Ymax):
            Ymax = Y
            Tmax = T
        #print(Y)
        #print('')    
    
    print('Em',end=' ')
    print(cont,end=' ')
    print('passos')
    print('')
    print('Altura maxima atingida foi ',end=' ')
    print(Ymax,end='')
    print('m em ',end=' ')
    print(Tmax,end='')
    print('seg')
    print('')
    print('Velocidade no momento do impacto com o mar foi ',end=' ')
    print(V,end='')
    print('m/seg em ',end='')
    print(T,end=' ')
    print('seg')
    print('')
    
    
    return 0
    
def Euler_Implic(T0,V0,Y0,DeltaT,K,M,G):
    #contador de passo
    cont = 0
    #variaveis da altura maxima
    Ymax = Y0
    Tmax = T0
    Y = Y0
    V = V0
    T = T0
    while (Y > 0):
        cont = cont + 1       
        V =  (M/(M+(K*DeltaT)))*(V-(G*DeltaT))
        Y = Y + V*DeltaT
        T = T + DeltaT
        if (Y > Ymax):
            Ymax = Y
            Tmax = T
        #print(Y)
        #print('')    
    
    print('Em',end=' ')
    print(cont,end=' ')
    print('passos')
    print('')
    print('Altura maxima atingida foi ',end=' ')
    print(Ymax,end='')
    print('m em ',end=' ')
    print(Tmax,end='')
    print('seg')
    print('')
    print('Velocidade no momento do impacto com o mar foi ',end=' ')
    print(V,end='')
    print('m/seg em ',end='')
    print(T,end=' ')
    print('seg')
    print('')
    
    
    return 0



print('METODO EULER EXPLICITO')
print('')
print('DELTA = 0.1 seg')
print('')
a = Euler_Explic(t0,v0,y0,dt1,k,m,g)
print('')
print('DELTA = 0.01 seg')
print('')
a = Euler_Explic(t0,v0,y0,dt2,k,m,g)
print('')
print('DELTA = 0.001 seg')
print('')
a = Euler_Explic(t0,v0,y0,dt3,k,m,g)
print('')
print('DELTA = 0.0001 seg')
print('')
a = Euler_Explic(t0,v0,y0,dt4,k,m,g)
print('')
print('')
print('METODO EULER IMPLICITO')
print('')
print('DELTA = 0.1 seg')
print('')
a = Euler_Implic(t0,v0,y0,dt1,k,m,g)
print('')
print('DELTA = 0.01 seg')
print('')
a = Euler_Implic(t0,v0,y0,dt2,k,m,g)
print('')
print('DELTA = 0.001 seg')
print('')
a = Euler_Implic(t0,v0,y0,dt3,k,m,g)
print('')
print('DELTA = 0.0001 seg')
print('')
a = Euler_Implic(t0,v0,y0,dt4,k,m,g)

