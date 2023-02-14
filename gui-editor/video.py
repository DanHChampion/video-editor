import cv2
from PIL import Image
import numpy as np

from functions import Functions as f

class Video():
    def __init__(self):
        self.path = None  
        self.layers = []
        # self.temp_path = "temp/"
        self.vid_capture = None

    def load(self, file_path):
        self.path = file_path
        self.layers = []
        self.vid_capture = cv2.VideoCapture(file_path)

    def get_frame(self, frame_num):
        self.vid_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_num-1)
        ret, frame = self.vid_capture.read()

        for layer in self.layers:
            print("bruh")
            frame = self.apply_layer(layer, frame)

        cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(cv2image)

        return frame
    

    def get_framerate(self):
        return int(self.vid_capture.get(5))

    def get_framecount(self):
        return int(self.vid_capture.get(7))

    def get_framesize(self):
        return (int(self.vid_capture.get(3)), int(self.vid_capture.get(4)))


    def create_new_layer(self, process):
        print(f"Applying {process}...")
        self.layers.append(Layer(process=process, parameters = {'value1': 0}))

    def delete_layer(self, index):
        pass

    def apply_layer(self, layer, frame):
        if not layer.hidden:
            if layer.process == "contrast":
                new_frame = layer.adjust_contrast(frame)
                return new_frame
            
            if layer.process == "brightness":
                new_frame = layer.adjust_brightness(frame)
                return new_frame

            if layer.process == "film grain":
                new_frame = layer.adjust_gaussian_noise(frame)
                return new_frame
            
            if layer.process == "noise removal":
                new_frame = layer.adjust_denoise(frame)
                return new_frame

        return frame

    def toggle_hide_layer(self, index):
        pass

    def update_layer(self, index, parameters = None, process = None, hidden = None):
        if process != None:
            self.layers[int(index)].process = process.lower()
        if parameters != None:
            self.layers[int(index)].parameters = parameters
        if hidden != None:
            self.layers[int(index)].hidden = hidden



class Layer: 
    def __init__(self, process , hidden = False, parameters = {}):
        self.process = process
        self.hidden = hidden
        self.parameters = parameters

    def default_params(self, parameters):
        pass
        
    def adjust_brightness(self, frame, brightness_value = 50):
        print("adjusting brightness")
        brightness_value = self.parameters['value1'] 
        # Calculate Value

        # Brightness Value (-255,255)
        if brightness_value != 0:
            if brightness_value > 0:
                shadow = brightness_value
                highlight = 255
            else:
                shadow = 0
                highlight = 255 + brightness_value
            alpha_b = (highlight - shadow)/255
            gamma_b = shadow
            return cv2.addWeighted(frame, alpha_b, frame, 0, gamma_b)
        else:
            return frame.copy()

    def adjust_contrast(self, frame, contrast_value = 50):
        contrast_value = self.parameters['value1'] # Constrast Value (-127,127)
        if contrast_value != 0:
            f = float(131 * (contrast_value + 127)) / (127 * (131 - contrast_value))
            alpha_c = f
            gamma_c = 127*(1-f)
            return cv2.addWeighted(frame, alpha_c, frame, 0, gamma_c)
        return frame.copy()

    def adjust_gaussian_noise(self, frame):
        mean = self.parameters['value1'] # Mean
        sigma = sigma = 10**0.5 # self.parameters['value2'] # Variance
        row, col = frame.shape[:2]

        gaussian = np.random.normal(mean, sigma, (row, col)) #  np.zeros((224, 224), np.float32)

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

    def adjust_denoise(self, frame):
        return cv2.medianBlur(frame, 5)
        

