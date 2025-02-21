import cv2
import numpy as np
import matplotlib.pyplot as plt
from manualThreshold import manualThreshold

def extractShape(image_path):
    '''  Extract the outline out while removing the text '''
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Try loading image")
        return
    
    img=255-img #invert
    binaryImage = manualThreshold(img, threshold=150)
    edges=sobel(binary)
    largestContour = funLargestContour(edges)
    if largestContour is None:
        print("no contour")
        return
    
    outline = np.ones_like(img)*255

    for x,y in largestContour:
        outline[x,y] = 0  #makes the pixels black

    saveimagepath=""
    cv2.imwrite(saveimagepath, outline)
    print("Image saved")

image = #path
extractShape(image)
