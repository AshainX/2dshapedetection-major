"""
 Extract only the shape outline while removing text.

"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ImageProcessingContours.manualThreshold import manualThresholding
from ImageProcessingContours.largestContour import funLargestContour
from ImageProcessingContours.sobeledge  import sobelED
from datetime import datetime


def shapeExtractionOutline(image_path):
   
    
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) # grayscale image
    if image is None:
        print("Error: Image not found")
        return

    
    image = 255 - image  #invert image 
    binary = manualThresholding(image, threshold=150)
    edges = sobelED(binary)


    largest_contour = funLargestContour(edges) #finding largest contour
    if largest_contour is None:
        print("No valid contour found")
        return

 
    outline_image = np.ones_like(image) * 255  #white background


    for x, y in largest_contour:
        outline_image[x, y] = 0  # Black outline on white background 

    baseDirectory = r"C:\Users\ashut\Documents\GitHub\2dshapedetection-major\ImageProcessingContours\Saved Images"
    t = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    sd = os.path.join(baseDirectory, f"image-{t}")
    os.makedirs(sd, exist_ok=True)
    outlineImgpath = os.path.join(sd, "extracted_image.png")
    cv2.imwrite(outlineImgpath, outline_image)
    print("Outline image saved in")

    # Display the extracted shape outline
    plt.figure(figsize=(6, 6))
    plt.imshow(outline_image, cmap='gray')
    plt.title("Extracted Shape Outline")
    plt.axis("off")
    plt.show()
