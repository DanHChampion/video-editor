import cv2
import numpy as np
# from skimage import exposure
# from skimage.exposure import match_histograms
import colortrans

# dstein64, colortrans, GitHub repository, https://github.com/dstein64/colortrans

class ColourTransfer:
    # All functionality is used from colortrans package

    def colour_transfer_lhm(parameters, frame):
        # Linear Histogram Matching [1] (default)
        # Load the source and target images

        ref = cv2.imread('temp/sunset.jpg')
        output_lhm = colortrans.transfer_lhm(frame, ref)
        return output_lhm
    
    def colour_transfer_pccm(parameters, frame):
        #Load the source and target images
        ref = cv2.imread('temp/sunset.jpg')
        output_pccm = colortrans.transfer_pccm(frame, ref)
        return output_pccm
    
    def colour_transfer_reinhard(parameters, frame):
        #Load the source and target images
        ref = cv2.imread('temp/sunset.jpg')
        output_reinhard = colortrans.transfer_reinhard(frame, ref)
        return output_reinhard

    
