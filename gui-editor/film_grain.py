import numpy as np
import cv2
import math

class FilmGrain:
    # Basic Gaussian Noise Filter
    def gaussian_noise(parameters, frame):
        mean = 1 # parameters['value1'] # Mean
        sigma = 10 # parameters['value2'] * 0.5 # Standard Deviation
        if sigma < 0:
            sigma = 0

        row, col = frame.shape[:2]

        gaussian = np.random.normal(mean, sigma, (row, col)) # np.zeros((224, 224), np.float32)

        noisy_image = np.zeros(frame.shape, np.float32)

        if len(frame.shape) == 2:
            noisy_image = frame + gaussian
        else:
            noisy_image[:, :, 0] = frame[:, :, 0] + gaussian
            noisy_image[:, :, 1] = frame[:, :, 1] + gaussian
            noisy_image[:, :, 2] = frame[:, :, 2] + gaussian

        cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
        noisy_image = noisy_image.astype(np.uint8)
        return noisy_image
    
    # Varying Grain Size Noise
    def varying_grain_size(parameters, frame):
        size_range = (4,6) # (math.floor(parameters['value2']*0.5), math.floor(parameters['value3']*0.5))
        intensity = 0.05 # parameters['value1'] * 0.01

        # Convert image to float in range [0, 1]
        image = frame.astype(np.float32) / 255.0
        
        # Calculate random grain size for each pixel
        sizes = np.random.randint(size_range[0], size_range[1]+1, size=image.shape[:2])
        
        # Calculate random grain values for each pixel
        noise = np.random.rand(*image.shape[:2])
        noise = (noise - 0.5) * intensity
        
        # Apply grain to image
        for i in range(image.shape[2]):
            image[:,:,i] += noise * sizes
            
        # Clip image to range [0, 1]
        image = np.clip(image, 0, 1)
        
        # Convert back to uint8
        image = (image * 255).astype(np.uint8)
        
        return image

    # Inhomogenous Boolean Model
    def inhomogenous_boolean_model(parameters, frame):
        height, width = frame.shape[:2]
        lambda0 = 2 #parameters['value1'] * 0.05 # 2.0
        alpha = 1# parameters['value2'] * 0.05 # 1.0

        # Generate a homogeneous Poisson point process
        N = np.random.poisson(lambda0 * width * height)
        X = np.random.uniform(0, width, N)
        Y = np.random.uniform(0, height, N)

        # Generate an inhomogeneous Boolean model
        mask = np.zeros((height, width), dtype=bool)
        for i in range(height):
            for j in range(width):
                if np.random.uniform(0, 1) < alpha * np.exp(-lambda0):
                    mask[i, j] = True
                else:
                    mask[i, j] = False

        # Draw the film grain
        grain = np.zeros((height, width))
        for i in range(N):
            if mask[int(Y[i]), int(X[i])]:
                grain[int(Y[i]), int(X[i])] = 255.0

        grain = (grain - 0.5) * 0.25
        noisy_image = np.zeros(frame.shape, np.float32)

        if len(frame.shape) == 2:
            noisy_image = frame + grain
        else:
            noisy_image[:, :, 0] = frame[:, :, 0] + grain
            noisy_image[:, :, 1] = frame[:, :, 1] + grain
            noisy_image[:, :, 2] = frame[:, :, 2] + grain

        cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
        noisy_image = noisy_image.astype(np.uint8)
        return noisy_image