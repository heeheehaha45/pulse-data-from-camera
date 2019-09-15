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
    
   # print(img.shape)
    H, W ,dim= img.shape

    #chop image
    y=70
    newY=259
    crop_img = img[y:newY, ]
    cv2.imshow("cropped", crop_img)
    #cv2.waitKey(0)
    
    success=cv2.imwrite('output/chop/img'+str(nFrame)+'.png',crop_img)

    nFrame=nFrame+1
    
 

cv2.destroyAllWindows()

