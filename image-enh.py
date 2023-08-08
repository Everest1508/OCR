import cv2
import numpy as np

# Load the image
img = cv2.imread('handwritng1.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply median filter for noise reduction
denoised = cv2.medianBlur(gray, 3)

# Enhance the image using histogram equalization
equalized = cv2.equalizeHist(denoised)

# Apply sharpening filter
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpened = cv2.filter2D(equalized, -1, kernel)


# Display the results
cv2.imshow('Original', img)
cv2.imshow('Denoised', denoised)
cv2.imshow('Enhanced', equalized)
cv2.imshow('Sharpened', sharpened)
# cv2.imwrite('new.jpg',sharpened)
cv2.waitKey(0)
