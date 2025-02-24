import numpy as np

def funLargestContour(binary):
    """Find and return the largest contour from a binary image."""
    height, width = binary.shape
    visited = np.zeros((height, width), dtype=bool)
    contours = []

    def edge_follow(x, y):
        """Follow the contour edges."""
        stack = [(x, y)]
        contour = []
        while stack:
            cx, cy = stack.pop()
            if 0 <= cx < height and 0 <= cy < width and not visited[cx, cy] and binary[cx, cy] == 255:
                visited[cx, cy] = True
                contour.append((cx, cy))
                stack.extend([(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)])
        return contour

    for i in range(height):
        for j in range(width):
            if binary[i, j] == 255 and not visited[i, j]:
                contour = edge_follow(i, j)
                if len(contour) > 200:  # Remove small contours (text)
                    contours.append(contour)

    if contours:
        return max(contours, key=len)  # Return largest contour
    return None
