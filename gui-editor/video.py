import cv2
from PIL import Image
import numpy as np
from tqdm import tqdm
import time

from film_grain import FilmGrain
from colour_transfer import ColourTransfer
from noise_removal import NoiseRemoval
from colour_correction import ColourCorrection

class Video():
    def __init__(self):
        self.path = None  
        self.layers = []
        self.vid_capture = None

    def load(self, file_path):
        self.path = file_path
        self.layers = []
        self.vid_capture = cv2.VideoCapture(file_path)

    def get_frame(self, frame_num):
        if frame_num > 0:
            self.vid_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_num-1)
        else:
            self.vid_capture = cv2.VideoCapture(self.path)
        ret, frame = self.vid_capture.read()

        for layer in self.layers:
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
        self.layers.append(Layer(process=process, parameters = {'value1': 0, 'value2': 0,'value3': 0}))

    def delete_layer(self, index):
        pass

    def export(self):
        print("Exporting to result/result.mp4")        
        result = cv2.VideoWriter('result/result.mp4', 
                -1,
                self.get_framerate(),
                self.get_framesize())
    
        # Start Time
        start = time.time()

        for frame_num in tqdm(range(self.get_framecount())):
            pil_image = self.get_frame(frame_num)
            open_cv_image = np.array(pil_image) 
            opencv_frame = open_cv_image[:, :, ::-1].copy() 
            result.write(opencv_frame)

        # End Time
        final = time.time() - start
        print ("Time Elapsed: ", final)

        result.release()
        print("Complete!")

    def apply_layer(self, layer, frame):
        if not layer.hidden:
            # Experimental
            if layer.process == "contrast":
                new_frame = layer.adjust_contrast(frame)
                return new_frame
            if layer.process == "brightness":
                new_frame = layer.adjust_brightness(frame)
                return new_frame
            if layer.process == "colour balance":
                new_frame = layer.adjust_colour_balance(frame)
                return new_frame
            # Actual
            if layer.process == "colour correction - histogram manipulation linear":
                new_frame = layer.apply_colour_correction1(frame)
                return new_frame
            if layer.process == "colour correction - histogram manipulation cauchy":
                new_frame = layer.apply_colour_correction2(frame)
                return new_frame
            if layer.process == "colour correction - histogram manipulation logistic":
                new_frame = layer.apply_colour_correction3(frame)
                return new_frame

            if layer.process == "colour transfer - linear histogram matching":
                new_frame = layer.apply_colour_transfer1(frame)
                return new_frame
            if layer.process == "colour transfer - principal component color matching":
                new_frame = layer.apply_colour_transfer2(frame)
                return new_frame
            if layer.process == "colour transfer - reinhard et al.":
                new_frame = layer.apply_colour_transfer3(frame)
                return new_frame
            
            if layer.process == "film grain - gaussian":
                new_frame = layer.adjust_film_grain1(frame)
                return new_frame
            if layer.process == "film grain - varying grain size":
                new_frame = layer.adjust_film_grain2(frame)
                return new_frame
            if layer.process == "film grain - inhomogenous boolean model":
                new_frame = layer.adjust_film_grain3(frame)
                return new_frame
            
            if layer.process == "noise removal - median blur":
                new_frame = layer.adjust_denoise1(frame)
                return new_frame
            if layer.process == "noise removal - bilateral filter":
                new_frame = layer.adjust_denoise2(frame)
                return new_frame
            if layer.process == "noise removal - non local means":
                new_frame = layer.adjust_denoise3(frame)
                return new_frame
            
        return frame

    def update_layer(self, index, parameters = None, process = None, hidden = None):
        if process != None:
            self.layers[int(index)].process = process.lower()
        if parameters != None:
            self.layers[int(index)].parameters = parameters
        if hidden != None:
            self.layers[int(index)].hidden = hidden

    def get_layer_labels(self, layer):
        # Experimental
        if layer.process == "contrast":
            return ["Contrast"]
        if layer.process == "brightness":
            return ["Brightness"]
        if layer.process == "colour balance":
            return ["Red", "Green", "Blue"]

        # Actual
        if layer.process == "colour correction - histogram manipulation linear":
            return []
        if layer.process == "colour correction - histogram manipulation cauchy":
            return ["Mean", "Standard Deviation"]
        if layer.process == "colour correction - histogram manipulation logistic":
            return ["Mean", "Standard Deviation"]
        
        if layer.process == "colour transfer - linear histogram matching":
            return []
        if layer.process == "colour transfer - principal component color matching":
            return []
        if layer.process == "colour transfer - reinhard et al.":
            return []

        if layer.process == "film grain - gaussian":
            return ["Gaussian Mean", "Gaussian Variance"]
        if layer.process == "film grain - varying grain size":
            return ["Intensity", "Min Grain Size", "Max Grain Size"]
        if layer.process == "film grain - inhomogenous boolean model":
            return ["Lambda", "Alpha"]

        if layer.process == "noise removal - median blur":
            return ["Kernel Size"]
        if layer.process == "noise removal - bilateral filter":
            return ["Kernel Size"]
        if layer.process == "noise removal - non local means":
            return ["Kernel Size"]
        

class Layer: 
    def __init__(self, process , hidden = False, parameters = {}):
        self.process = process
        self.hidden = hidden
        self.parameters = parameters

    def default_params(self, parameters):
        pass

    def apply_colour_correction1(self, frame):
        pass
        
    def apply_colour_correction1(self, frame):
        return ColourCorrection.histogram_manipulation_linear(self.parameters, frame)
    def apply_colour_correction2(self, frame):
        return ColourCorrection.histogram_manipulation_cauchy(self.parameters, frame)
    def apply_colour_correction3(self, frame):
        return ColourCorrection.histogram_manipulation_logistic(self.parameters, frame)
    
    def apply_colour_transfer1(self, frame):
        return ColourTransfer.colour_transfer_lhm(self.parameters, frame)
    def apply_colour_transfer2(self, frame):
        return ColourTransfer.colour_transfer_pccm(self.parameters, frame)
    def apply_colour_transfer3(self, frame):
        return ColourTransfer.colour_transfer_reinhard(self.parameters, frame)

    def adjust_film_grain1(self, frame):
        return FilmGrain.gaussian_noise(self.parameters, frame)
    def adjust_film_grain2(self, frame):
        return FilmGrain.varying_grain_size(self.parameters, frame)
    def adjust_film_grain3(self, frame):
        return FilmGrain.inhomogenous_boolean_model(self.parameters, frame)

    def adjust_denoise1(self, frame):
        return NoiseRemoval.median_blur(self.parameters, frame)
    def adjust_denoise2(self, frame):
        return NoiseRemoval.bilateral_filter(self.parameters, frame)
    def adjust_denoise3(self, frame):
        return NoiseRemoval.non_local_means(self.parameters, frame)

    def adjust_brightness(self, frame, brightness_value = 50):
        brightness_value = self.parameters['value1'] * 3
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
        contrast_value = self.parameters['value1'] * 1.5 # Constrast Value (-127,127)
        if contrast_value != 0:
            f = float(131 * (contrast_value + 127)) / (127 * (131 - contrast_value))
            alpha_c = f
            gamma_c = 127*(1-f)
            return cv2.addWeighted(frame, alpha_c, frame, 0, gamma_c)
        return frame.copy()

    def adjust_colour_balance(self,frame):
        r_value = self.parameters['value1'] * 2 # Red Value
        g_value = self.parameters['value2'] * 2 # Green Value
        b_value = self.parameters['value3'] * 2 # Blue Value

        # Extract RGB Channels
        height, width = frame.shape[:2]
        frame = frame.astype(np.float)
        frame_R, frame_G, frame_B = cv2.split(frame)

        if r_value != 0:
            if r_value > 0:
                shadow = r_value
                highlight = 255
            else:
                shadow = 0
                highlight = 255 + r_value
            alpha_b = (highlight - shadow)/255
            gamma_b = shadow
            frame_R = cv2.addWeighted(frame_R, alpha_b, frame_R, 0, gamma_b)

        if r_value != 0:
            if r_value > 0:
                shadow = g_value
                highlight = 255
            else:
                shadow = 0
                highlight = 255 + g_value
            alpha_b = (highlight - shadow)/255
            gamma_b = shadow
            frame_G = cv2.addWeighted(frame_G, alpha_b, frame_G, 0, gamma_b)

        if r_value != 0:
            if r_value > 0:
                shadow = b_value
                highlight = 255
            else:
                shadow = 0
                highlight = 255 + b_value
            alpha_b = (highlight - shadow)/255
            gamma_b = shadow
            frame_B = cv2.addWeighted(frame_B, alpha_b, frame_B, 0, gamma_b)

        output = cv2.merge((frame_R, frame_G, frame_B))
        output = np.minimum(output, 255).astype(np.uint8)
        return output

