import numpy as np

#A = np.array([[1,2],[3,4],[5,6]])
#B = np.array([2,2])

#print(A)
#print(len(A)) #linha
#print(len(A[0])) #coluna

#print(B)
#print(len(B))
#print(np.dot(A,B))

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
    print((ynovo),(xvelho))
#return 0    

A = np.array([[40,8,4,2,1],[8,30,12,6,2],[4,12,20,1,2],[2,6,1,25,4],[1,2,2,4,5]])
print('Matriz:')
print(A)
v = np.array([1,1,1,1,1])
print('vetor0:')
print(v)

print('autovalor  - autovetor')
met_pot_regular (A,v,0.001)