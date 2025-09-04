import numpy as np
import matplotlib.pyplot as plt
import cv2
# Take notice that OpenCV handles the image as a numpy array when opening it 
img = cv2.imread('shapes.jpg')
out_bgr = img.copy()
mask_blue= (img[:,:,0] > 150) & (img[:,:,1] < 100) & (img[:,:,2] < 100)
mask_red= (img[:,:,0] < 100) & (img[:,:,1] < 100) & (img[:,:,2] > 150)
mask_black= (img[:,:,0] < 50) & (img[:,:,1] < 50) & (img[:,:,2] < 50)
out_bgr[mask_blue]=[0,0,0]
out_bgr[mask_red]=[255,0,0]
out_bgr[mask_black]=[0,0,255]
out = cv2.cvtColor(out_bgr, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(img)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(out)
axes[1].set_title('Processed Image')
axes[1].axis('off')

plt.show() 