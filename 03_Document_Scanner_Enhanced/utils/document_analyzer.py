import cv2, numpy as np

def analyze(gray):
    blur=cv2.Laplacian(gray,cv2.CV_64F).var()
    brightness=float(np.mean(gray))
    status='GOOD'
    if brightness<70: status='DARK'
    return blur, brightness, status
