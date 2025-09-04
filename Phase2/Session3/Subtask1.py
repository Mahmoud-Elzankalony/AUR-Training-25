# Setup Commands: (inside VSCode terminal)
## (one-time) python -m venv .venv
## (Windows: every re-open) ./.venv/Scripts/activate.bat
## (Other systems: every re-open) ./.venv/Scripts/activate
## (one-time) pip install matplotlib opencv-python numpy
import numpy as np
import matplotlib.pyplot as plt
import cv2
def convolve(image, kernel):
    kernel_flipped=kernel[::-1,::-1]
    kernel_nrows=kernel.shape[0]
    kernel_ncol=kernel.shape[1]
    image_paded=np.pad(image,((kernel_nrows//2,kernel_nrows//2),(kernel_ncol//2,kernel_ncol//2)),mode='constant')
    image_output=np.zeros((image.shape[0],image.shape[1]),dtype=np.float64)
    for i in range(image.shape[0]) :
        for j in range(image.shape[1]) :
            image_output[i][j]=np.sum(image_paded[i:i+kernel_nrows,j:j+kernel_ncol] * kernel_flipped)
    return np.clip(image_output, 0, 255).astype(np.uint8)
def median_filter(image, kernel_size):
    kernel_nrows=kernel_size
    kernel_ncol=kernel_size
    image_paded=np.pad(image,((kernel_nrows//2,kernel_nrows//2),(kernel_ncol//2,kernel_ncol//2)),mode='constant')
    image_output=np.zeros((image.shape[0],image.shape[1]),dtype=np.float64)
    for i in range(image.shape[0]) :
        for j in range(image.shape[1]) :
           image_output[i][j]=np.median(image_paded[i:i+kernel_nrows,j:j+kernel_ncol])
    return np.clip(image_output, 0, 255).astype(np.uint8) 

# Take notice that OpenCV handles the image as a numpy array when opening it
img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(convolve(img, np.ones((5, 5)) / 25), cmap='gray')
axes[0, 1].set_title('Box Filter')
axes[0, 1].axis('off')

axes[0, 2].imshow(convolve(img, np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])), cmap='gray')
axes[0, 2].set_title('Horizontal Sobel Filter')
axes[0, 2].axis('off')

axes[1, 0].imshow(convolve(img, np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])), cmap='gray')
axes[1, 0].set_title('Vertical Sobel Filter')
axes[1, 0].axis('off')

axes[1, 1].imshow(median_filter(img, 3), cmap='gray')
axes[1, 1].set_title('Median Filter (3x3)')
axes[1, 1].axis('off')

axes[1, 2].imshow(median_filter(img, 5), cmap='gray')
axes[1, 2].set_title('Median Filter (5x5)')
axes[1, 2].axis('off')

plt.show()