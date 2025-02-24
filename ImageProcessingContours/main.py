import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ImageProcessingContours.process import shapeExtractionOutline

if __name__ == "__main__":
    image_path = r"C:\Users\ashut\Documents\GitHub\2dshapedetection-major\TEST\1.png"
    shapeExtractionOutline(image_path)
