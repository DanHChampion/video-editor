import numpy as np
import cv2

class NoiseRemoval:
    # Median Blur
    def median_blur(parameters, frame):
        kernel_size = 7 # parameters['value1']
        if kernel_size <= 0:
            return frame.copy()
        return cv2.medianBlur(frame, round(np.ceil(kernel_size) // 2 * 2 + 1)) # odd numbers only
    
    # Bilateral Filter
    def bilateral_filter(parameters, frame):
        kernel_size = 7 # parameters['value1']
        if kernel_size <= 0:
            return frame.copy()
        return cv2.bilateralFilter(frame, round(np.ceil(kernel_size) // 2 * 2 + 1),75,75) # odd numbers only

    # Non Local Means
    def non_local_means(parameters, frame):
        kernel_size = 7 # parameters['value1']
        if kernel_size <= 0:
            return frame.copy()
        rounded_kernel_size = round(np.ceil(kernel_size) // 2 * 2 + 1)
        return cv2.fastNlMeansDenoisingColored(frame, None, 3, 3, rounded_kernel_size, rounded_kernel_size*3)