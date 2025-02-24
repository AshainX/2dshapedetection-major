"""

Manually compute Sobel edge detection.

"""

import numpy as np

def sobelED(image):
    
    height, width = image.shape
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # X-direction
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])  # Y-direction

    edim = np.zeros((height, width), dtype=np.uint8)

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            gx = np.sum(image[i - 1:i + 2, j - 1:j + 2] * sobel_x)
            gy = np.sum(image[i - 1:i + 2, j - 1:j + 2] * sobel_y)
            magnitude = np.sqrt(gx**2 + gy**2)

            if magnitude > 100:  # Edge threshold
                edim[i, j] = 255  # Edge detected

    return edim
