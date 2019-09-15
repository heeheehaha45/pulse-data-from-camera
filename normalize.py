import cv2
import argparse
import numpy as np

startFrame=15
endFrame=136

nFrame=startFrame



maxi=0
mini=255

#find max and mini
for count in range(startFrame, endFrame):
    print (maxi)
    print (mini)
    img = cv2.imread('output/img'+str(nFrame)+'.png')
    img[:,:,0] = 0
    img[:,:,2] = 0
   # print(img.shape)
    H, W ,dim= img.shape
    #print(img)
    
    #find max from each pixel from each picture
    for x in range(0, H):
        for y in range(0, W):
                if img[x][y][1]>maxi:
                    maxi=img[x][y][1]
                if img[x][y][1]<mini:
                    mini=img[x][y][1]

               #print (img[x][y])
        
   # cv2.imshow('image',img)
   # cv2.waitKey(0)
    nFrame=nFrame+1
 
 
nFrame=startFrame
#normalize each pixel at each image
for count in range(startFrame, endFrame):
   
    img = cv2.imread('output/img'+str(nFrame)+'.png')
    H, W,dim = img.shape
    print([H,W])
    print("at each pixel...")
    for x in range(0, H):
        for y in range(0, W):
              # print(img[x][y][1])
              # print(int( 255*(img[x][y][1]-mini)/(maxi-mini) ))
               img[x][y][1] =int( 255*(img[x][y][1]-mini)/(maxi-mini) )
               #print (img[x][y])
        

 #  print(img.shape)
    img[:, :, 0] = 0
    img[:, :, 2] = 0
    success=cv2.imwrite('output_after_process/img'+str(nFrame)+'.png',img)
    print('--------------------------------------------------------------------------------')
    cv2.imshow('image',img)
   # cv2.waitKey(0)
    nFrame=nFrame+1


 
print (maxi)
print (mini)

cv2.destroyAllWindows()

