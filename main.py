import numpy as np
import cv2 as cv


def getIndexes(isHeight,image, limitT):
    if isHeight:
        indexMatrix = image >= limitT
    else:
        indexMatrix = image < limitT
    return indexMatrix



def treshold(image, limitT, isHeight, brightness,imgPath):
   
    indexMatrix = getIndexes(isHeight,image, limitT)
    image = image.astype(int)

    if brightness > 0:
      image[indexMatrix] = np.minimum(image[indexMatrix] + brightness, 255)
    else:
      image[indexMatrix] = np.maximum(image[indexMatrix] + brightness, 0)

    image = image.astype(np.uint8)
    cv.imshow('image',image)
    cv.imwrite('./results/'+imgPath,image)
    cv.waitKey(5000)
    return
    


def getUserData():
    imgPath = input("Digite o nome da Imagem(dentro da pasta images) = ")
    img  = cv.imread('./images/'+imgPath, 0)
    limitT = int(input("T = "))
    isHeight = int(input("(0) Abaixo do Limite (1) Acima do Limete  =  "))
    if(isHeight<1):
        isHeight = False
    else:
        isHeight = True
    print(isHeight)
    brightness = int(input("Brilho = "))
    return img,limitT,isHeight,brightness,imgPath
    

def main():
    image,limitT,isHeight,brightness,imgPath = getUserData()
    treshold(image, limitT, isHeight, brightness,imgPath)

if __name__ ==  '__main__':
    main()