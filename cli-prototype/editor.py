import cv2
import sys
from functions import Functions as f

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
    print ("Video Name:", f.get_video_name(path))
    
    # Get frame rate 
    print("Frame Rate : ", f.get_framerate(vid_capture),"frames per second")  
    
    # Get frame count
    print("Frame Count : ", f.get_framecount(vid_capture))

    # Get frame size
    print ("Frame Size:", f.get_framesize(vid_capture))

    _ = input()


def get_user_input():

    print (LINE_BREAK)
    vid_capture = cv2.VideoCapture(path)

    print("""
What would you like to do?

    [1] Get Video Info
    [2] Convert to Greyscale
    [3] Combine Videos
    ------------------------
    [4] Adjust Brightness
    [5] Adjust Constrast
    [6] Add Film Grain
    [7] Remove Noise
    ------------------------
    [exit] Exit Program
    """)
    user_input = input(">> ")

    if user_input == '1':
        get_video_info()
    elif user_input == '2':
        f.convert_to_greyscale(vid_capture, path)
    elif user_input == '3':
        f.combine_videos(vid_capture, path)
    elif user_input == '4':
        f.adjust_brightness(vid_capture, path)
    elif user_input == '5':
        f.adjust_contrast(vid_capture, path)
    elif user_input == '6':
        noise_type = input("Choose type of noise ([1] Gaussian Noise ; [2] Modified Gaussian ; [3] Boolean Model): ")
        if noise_type == '1':
            f.gaussian_noise(vid_capture,path)
        if noise_type == '2':
            f.gaussian_noise(vid_capture,path)
    elif user_input == '7':
        noise_type = input("Choose denoising algorithm ([1] Median Filtering ; [2]  ; [3] ): ")
        if noise_type == '1':
            f.median_blur(vid_capture,path)
    elif user_input == 'exit':
        exit()
    
    get_user_input()

print('Starting Editor...')

try:
    path = sys.argv[1]
except:
    print ("No Video Path Specified. Loading Default Video...")
    path = DEFAULT_PATH

open_file()
get_user_input()