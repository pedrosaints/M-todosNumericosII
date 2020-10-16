
#constantes
t0 = 0
v0 = 5
y0 = 200
k = 0.25
m = 2
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
def Runge_Kutta(T0,V0,Y0,DeltaT,K,M,G):
    #contador de passo
    cont = 0
    #variaveis da altura maxima
    Ymax = Y0
    Tmax = T0
    Y = Y0
    V = V0
    T = T0
    cont = cont + 1
    #pego o Scont com base no Scont-1
    F1 = F(G,V,K,M)
    #preciso somente de v de S pra calcular o proximo F
    vaux = V + (DeltaT/2)*F1[0]
    F2 = F(G,vaux,K,M)
    #print(F2)
    vaux = V + (DeltaT/2)*F2[0]
    F3 = F(G,vaux,K,M)
    #print(F3)
    vaux = V + (DeltaT)*F3[0]
    F4 = F(G,vaux,K,M)  
        
    vaux = V +  (DeltaT/24)*(-(F1[0]*9)+(F2[0]*37)-(F3[0]*59)+(F4[0]*55))
    F5 = F(G,vaux,K,M)
    V =  V + DeltaT*((F2[0])+(F3[0]*2)+(F4[0]*2)+(F5[0]))/6
    Y = Y + DeltaT*((F2[0])+(F3[0]*2)+(F4[0]*2)+(F5[0]))/6
    T = T + DeltaT
    if (Y > Ymax):
        Ymax = Y
        Tmax = T
    while (Y>0):
        cont = cont + 1
        #pego o Scont com base no Scont-1
        F1 = F2
        F2 = F3
        F3 = F4
        F4 = F5      
        vaux = V +  (DeltaT/24)*(-(F1[0]*9)+(F2[0]*37)-(F3[0]*59)+(F4[0]*55))
        F5 = F(G,vaux,K,M)
        #while()
        V =  V + DeltaT*((F2[0])+(F3[0]*2)+(F4[0]*2)+(F5[0]))/6
        Y = Y + DeltaT*((F2[1])+(F3[1]*2)+(F4[1]*2)+(F5[1]))/6
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
    




print('METODO RUNGE-KUTTA')
print('')
print('DELTA = 0.1 seg')
print('')
a = Runge_Kutta(t0,v0,y0,dt1,k,m,g)
print('')
print('DELTA = 0.01 seg')
print('')
a = Runge_Kutta(t0,v0,y0,dt2,k,m,g)
print('')
print('DELTA = 0.001 seg')
print('')
a = Runge_Kutta(t0,v0,y0,dt3,k,m,g)
print('')
print('DELTA = 0.0001 seg')
print('')
a = Runge_Kutta(t0,v0,y0,dt4,k,m,g)

