import cv2
from PIL import Image

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
        self.layers.append(Layer(process=process, parameters = {'contrast': 40}))
        pass

    def delete_layer(self, index):
        pass

    def apply_layer(self, layer, frame):
        if layer.hidden:
            return frame
        
        if layer.process == "contrast":
            contrast_value = layer.parameters['contrast']
            if contrast_value != 0:
                    f = float(131 * (contrast_value + 127)) / (127 * (131 - contrast_value))
                    alpha_c = f
                    gamma_c = 127*(1-f)
            new_frame = cv2.addWeighted(frame, alpha_c, frame, 0, gamma_c)
            return new_frame

    def toggle_hide_layer(self, index):
        pass

    def update_layer(self, index, parameters):
        pass



class Layer: 
    def __init__(self, process , hidden = False, parameters = {}):
        self.process = process
        self.hidden = hidden
        self.parameters = parameters
        pass

