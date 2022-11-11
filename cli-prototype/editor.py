import cv2
import sys
from functions import Functions

LINE_BREAK = "--------------------"
DEFAULT_PATH = 'resources/happy_seal.mp4'
path = ""

def open_file():
    vid_capture = cv2.VideoCapture(path)
    if (vid_capture.isOpened() == False):
        print("Error Opening the Video File")
        exit()
    else:
        print("Successfully loaded:", path, "\n")

def get_video_info():
    vid_capture = cv2.VideoCapture(path)

    print ("--- Information ---\n")
    # Get File Name
    print ("Video Name:", Functions.get_video_name(path))
    
    # Get frame rate 
    print("Frame Rate : ", Functions.get_framerate(vid_capture),"frames per second")  
    
    # Get frame count
    print("Frame Count : ", Functions.get_framecount(vid_capture))

    # Get frame size
    print ("Frame Size:", Functions.get_framesize(vid_capture))

    _ = input()


def get_user_input():

    print (LINE_BREAK)
    vid_capture = cv2.VideoCapture(path)

    print("""
What would you like to do?
    [1] Get Video Info
    [2] Convert to Greyscale
    [3] Adjust Brightness
    [4] Adjust Constrast
    [5] Add Film Grain
    [6] Remove Noise
    [exit] Exit Program
    """)
    user_input = input(">> ")

    if user_input == '1':
        get_video_info()
    elif user_input == '2':
        Functions.convert_to_greyscale(vid_capture, path)
    elif user_input == '3':
        Functions.adjust_brightness(vid_capture, path)
    elif user_input == '4':
        Functions.adjust_contrast(vid_capture, path)
    elif user_input == '5':
        noise_type = input("Choose type of noise ([1] Gaussian Noise ; [2] Simplex  Noise ; [3] Artifcial Film Grain): ")
        if noise_type == '1':
            Functions.gaussian_noise(vid_capture,path)
    elif user_input == 'exit':
        exit()
    
    get_user_input()



def write_video():
    # VideoWriter(filename, apiPreference, fourcc, fps, frameSize[, isColor])
    print("New Video Saved in \"/results\"")

print('Starting Editor...')

try:
    path = sys.argv[1]
except:
    print ("No Video Path Specified. Loading Default Video...")
    path = DEFAULT_PATH

open_file()
get_user_input()