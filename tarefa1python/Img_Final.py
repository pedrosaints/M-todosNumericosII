
#Tarefa 1 da dupla 16: 
#415083	PEDRO HENRIQUE SANTOS BARROS 
#405052	JOSE GEOVANE SOARES DE OLIVEIRA


from PIL import Image
import numpy as np


def central(x,y,arr):
    #print(x,y)
    ar = np.copy(arr)
    for i in range(0,x):
        for k in range (0,y):
            ar[i,k] = abs((arr[i+1,k])/2 - (arr[i-1,k])/2) + abs((arr[i,k+1])/2 - (arr[i,k-1])/2)
    return ar


def Blurr(x,y,arr):
    #print(x,y)
    ar = np.copy(arr)
    for i in range(0,x):
        for k in range (0,y):
            ar[i,k] = (arr[i+1,k]/8 + arr[i-1,k]/8 + arr[i,k+1]/8 + arr[i,k-1]/8 + arr[i-1,k-1]/8 + arr[i-1,k+1]/8 + arr[i+1,k-1]/8 + arr[i+1,k+1]/8)
    return ar


def ExpandArray(ar,x,y):
    araux = np.arange(x*y+4+2*x+2*y).reshape(x+2,y+2)
    for i in range(x+2):
        for j in range(y+2):
            if((i==0) or (i == x+1) or (j==0) or (j == y+1)):
                araux[i][j] = 0
            else:
                araux[i][j] = ar[i-1][j-1]
    aux = np.copy(araux)            
    return aux


#abre a imagem
image = Image.open('img.jpg')

#converte para cinza
image = image.convert('L')
image.show()
nu = np.asarray(image)
x,y = nu.shape
aux = np.copy(nu)

#expande a imagem
aux = ExpandArray(aux,x,y)
image_antes = Image.fromarray(np.absolute(aux))
image_antes.show()
image_antes = image_antes.convert('L')
image_antes.save("img_antes.jpg")

#aplica o blurr
blurr_image = Blurr(x,y,aux)
newi = Image.fromarray(np.absolute(blurr_image))
newi.show()

#aplica o filtro de contorno
final_image = central(x,y,blurr_image)
newi2 = Image.fromarray(np.absolute(final_image))
newi2 = newi2.convert('L')
newi2.save("img_depois.jpg")
newi2.show()

#imagem -> converte para escala de cinza -> adiciona uma "borda" -> aplica o blurr -> aplica o filtro de contorno






