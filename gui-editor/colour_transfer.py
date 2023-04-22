import cv2
import numpy as np
# from skimage import exposure
# from skimage.exposure import match_histograms
import colortrans

# A. Rosebrock, color_transfer, GitHub repository, https://github.com/jrosebr1/color_transfer. 

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



    # def image_stats(image):
    #     """
    #     Parameters:
    #     -------
    #     image: NumPy array
    #         OpenCV image in L*a*b* color space
    #     Returns:
    #     -------
    #     Tuple of mean and standard deviations for the L*, a*, and b*
    #     channels, respectively
    #     """
    #     # compute the mean and standard deviation of each channel
    #     (l, a, b) = cv2.split(image)
    #     (lMean, lStd) = (l.mean(), l.std())
    #     (aMean, aStd) = (a.mean(), a.std())
    #     (bMean, bStd) = (b.mean(), b.std())

    #     # return the color statistics
    #     return (lMean, lStd, aMean, aStd, bMean, bStd)
    
    # def _min_max_scale(arr, new_range=(0, 255)):
    #     """
    #     Perform min-max scaling to a NumPy array
    #     Parameters:
    #     -------
    #     arr: NumPy array to be scaled to [new_min, new_max] range
    #     new_range: tuple of form (min, max) specifying range of
    #         transformed array
    #     Returns:
    #     -------
    #     NumPy array that has been scaled to be in
    #     [new_range[0], new_range[1]] range
    #     """
    #     # get array's current min and max
    #     mn = arr.min()
    #     mx = arr.max()

    #     # check if scaling needs to be done to be in new_range
    #     if mn < new_range[0] or mx > new_range[1]:
    #         # perform min-max scaling
    #         scaled = (new_range[1] - new_range[0]) * (arr - mn) / (mx - mn) + new_range[0]
    #     else:
    #         # return array if already in range
    #         scaled = arr

    #     return scaled

    # def _scale_array(arr, clip=True):
    #     """
    #     Trim NumPy array values to be in [0, 255] range with option of
    #     clipping or scaling.
    #     Parameters:
    #     -------
    #     arr: array to be trimmed to [0, 255] range
    #     clip: should array be scaled by np.clip? if False then input
    #         array will be min-max scaled to range
    #         [max([arr.min(), 0]), min([arr.max(), 255])]
    #     Returns:
    #     -------
    #     NumPy array that has been scaled to be in [0, 255] range
    #     """
    #     if clip:
    #         scaled = np.clip(arr, 0, 255)
    #     else:
    #         scale_range = (max([arr.min(), 0]), min([arr.max(), 255]))
    #         scaled = ColourTransfer._min_max_scale(arr, new_range=scale_range)

    #     return scaled

    # def basic_colour_transfer(parameters, frame, target_img=None):
    #     # Load the source and target images
    #     clip = True
    #     target_img = cv2.imread('temp/sunset.jpg')

    #     # convert the images from the RGB to L*ab* color space, being
    #     # sure to utilizing the floating point data type (note: OpenCV
    #     # expects floats to be 32-bit, so use that instead of 64-bit)
    #     source = cv2.cvtColor(target_img, cv2.COLOR_BGR2LAB).astype("float32") # Takes colours from
    #     target = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB).astype("float32") # Transformed into final image

    #     # compute color statistics for the source and target images
    #     (lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = ColourTransfer.image_stats(source)
    #     (lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = ColourTransfer.image_stats(target)

    #     # subtract the means from the target image
    #     (l, a, b) = cv2.split(target)
    #     l -= lMeanTar
    #     a -= aMeanTar
    #     b -= bMeanTar

    #     # scale by the standard deviations using paper proposed factor
    #     l = (lStdTar / lStdSrc) * l
    #     a = (aStdTar / aStdSrc) * a
    #     b = (bStdTar / bStdSrc) * b

    #     # add in the source mean
    #     l += lMeanSrc
    #     a += aMeanSrc
    #     b += bMeanSrc

    #     # clip/scale the pixel intensities to [0, 255] if they fall
    #     # outside this range
    #     l = ColourTransfer._scale_array(l, clip=clip)
    #     a = ColourTransfer._scale_array(a, clip=clip)
    #     b = ColourTransfer._scale_array(b, clip=clip)

    #     # merge the channels together and convert back to the RGB color
    #     # space, being sure to utilize the 8-bit unsigned integer data
    #     # type
    #     transfer = cv2.merge([l, a, b])
    #     transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)
        
    #     # return the color transferred image
    #     return transfer

    # def basic_histogram_matching(parameters, frame):
    #     # Load input and reference images
    #     target_img = cv2.imread('temp/sunset.jpg')
    #     # Perform histogram matching
    #     print(type(frame))

    #     source = cv2.cvtColor(target_img, cv2.COLOR_BGR2LAB).astype("uint8") # Takes colours from
    #     target = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB).astype("uint8") # Transformed into final image

    #     lab_planes_src = cv2.split(source)
    #     lab_planes_tar = cv2.split(target)

    #     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    #     lab_planes_src[0] = clahe.apply(lab_planes_src[0])
    #     lab_planes_src[0] = cv2.LUT(lab_planes_src[0], np.interp(np.arange(256), np.histogram(lab_planes_tar[0], 256)[1], np.histogram(lab_planes_src[0], 256)[1]).astype('uint8'))
    #     # matched_img = match_histograms(frame, target_img ,
    #     #                    multichannel=True)
    #     source = cv2.merge(lab_planes_src)
    #     final = cv2.cvtColor(source, cv2.COLOR_LAB2BGR)
    #     return final
    