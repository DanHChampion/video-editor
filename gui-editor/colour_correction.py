import numpy as np
import cv2
from skimage.util import img_as_ubyte
from skimage.exposure import cumulative_distribution
from scipy.stats import cauchy, logistic

# Image Processing with Python: Color Correction using Histogram Manipulation. Jephraim C. Manansala
# https://medium.com/swlh/image-processing-with-python-histogram-manipulation-on-digital-images-d4fb426d3513 

class ColourCorrection:
    
    def linear_distribution(image, channel):
        image_intensity = img_as_ubyte(image[:,:,channel])
        freq, bins = cumulative_distribution(image_intensity)
        if len(freq) < 256:
            freq = np.append(freq, [[255 for i in range(256-len(freq))]])
        target_bins = np.arange(255)
        target_freq = np.linspace(0,1, len(target_bins))
        new_vals = np.interp(freq, target_freq, target_bins)
        return new_vals[image_intensity].astype(np.uint8)
    
    def individual_channel(image, dist, channel):
        if dist == "linear":
            return ColourCorrection.linear_distribution(image, channel)
        im_channel = img_as_ubyte(image[:,:, channel])
        freq, bins = cumulative_distribution(im_channel)
        if len(freq) < 256:
            freq = np.append(freq, [[255 for i in range(256-len(freq))]])
        new_vals = np.interp(freq, dist.cdf(np.arange(0,256)),np.arange(0,256))
        return new_vals[im_channel].astype(np.uint8)


    def distribution(image, function, mean, std):
        if function != "linear":
            dist = function(mean,std)
        else:
            dist = function
        # image_intensity = img_as_ubyte(rgb2gray(image))
        # freq, bins = cumulative_distribution(image_intensity)
        
        # Convert to HSV color space
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Split the channels
        h, s, v = cv2.split(hsv)

        v_eq = ColourCorrection.individual_channel(image, dist, 2)
        
        # Merge the channels back together
        hsv_eq = cv2.merge([h, s, v_eq])
        result = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)

        return result

    # Histogram Manipulation (Jephraim C. Manansala)
    def histogram_manipulation_linear(parameters, frame):
        mean = 0
        std = 0
        return ColourCorrection.distribution(frame, "linear", mean, std)
    
    def histogram_manipulation_cauchy(parameters, frame):
        mean = 120 # parameters['value1'] * 5 # 120
        std = 50 #parameters['value2'] * 5 # 90
        return ColourCorrection.distribution(frame, cauchy, mean, std)
    
    def histogram_manipulation_logistic(parameters, frame):
        mean = 120 # parameters['value1'] * 5 # 120
        std = 50 # parameters['value2'] * 5 # 90
        return ColourCorrection.distribution(frame, logistic, mean, std)