import cv2 
import numpy as np
import matplotlib.pyplot as plt 

def manualThresholding(image, threshold=150):
    h, w = image.shape
    binary = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if image[i,j]<threshold:
                binary[i,j]=255
            else:
                binary[i,j]=0
    return binary

