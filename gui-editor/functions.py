import cv2 
import numpy as np

class Functions:

    def get_video_name(path):
        return path.split("/")[-1]

    def get_framerate(vid):
        return int(vid.get(5))

    def get_framecount(vid):
        return int(vid.get(7))

    def get_framesize(vid):
        return (int(vid.get(3)), int(vid.get(4)))

    def intialize_output(name,vid,path):
        # Create Video Output
        return cv2.VideoWriter('results/'+name+'_'+ Functions.get_video_name(path), -1, Functions.get_framerate(vid), Functions.get_framesize(vid) , 0)
        
    def convert_to_greyscale(vid,path):
        print("Converting Video to Grey Scale...")
        name = "greyscale"
        output = Functions.intialize_output(name,vid,path)

        while(vid.isOpened()):
            ret, frame = vid.read()
            if ret == True:
                grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                output.write(grey_frame)
            else:
                break
        
        print("Completed!")
        output.release()
    
    def adjust_brightness(vid,path):
        brightness_value = int(input("Brightness Value (-255,255): "))
        name = "brightness" + str(brightness_value)
        print("Adjusting Brightness by "+str(brightness_value)+" ...")
        output = Functions.intialize_output(name,vid,path)
        
        while(vid.isOpened()):
            ret, frame = vid.read()
            if ret == True:
                # Adjust Brightness Here 
                if brightness_value != 0:
                    if brightness_value > 0:
                        shadow = brightness_value
                        highlight = 255
                    else:
                        shadow = 0
                        highlight = 255 + brightness_value
                    alpha_b = (highlight - shadow)/255
                    gamma_b = shadow
                    new_frame = cv2.addWeighted(frame, alpha_b, frame, 0, gamma_b)
                else:
                    new_frame = frame.copy()
                
                output.write(new_frame)
            else:
                break
        
        print("Completed!")
        output.release()

    def adjust_contrast(vid,path):
        constrast_value = int(input("Constrast Value (-127,127): "))
        name = "contrast" + str(constrast_value)
        print("Adjusting Constrast by "+str(constrast_value)+" ...")
        output = Functions.intialize_output(name,vid,path)
        
        if constrast_value != 0:
                    f = float(131 * (constrast_value + 127)) / (127 * (131 - constrast_value))
                    alpha_c = f
                    gamma_c = 127*(1-f)
        
        while(vid.isOpened()):
            ret, frame = vid.read()
            if ret == True:
                # Adjust Constrast Here
                new_frame = cv2.addWeighted(frame, alpha_c, frame, 0, gamma_c)
                output.write(new_frame)
            else:
                break
        
        print("Completed!")
        output.release()

    def gaussian_noise(vid,path):
        name = "gaussiannoise"
        print("Adding Gaussian Noise...")
        output = Functions.intialize_output(name,vid,path)
        
        col,row = Functions.get_framesize(vid)
        mean = 0
        sigma = 10**0.5

        while(vid.isOpened()):
            ret, frame = vid.read()
            if ret == True:
                # Add Gaussian Noise Here
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
                output.write(noisy_image)

                # gauss = np.random.normal(mean,sigma,(row,col)).astype("uint8")* 255
                # grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # noisy_frame = grey_frame + gauss
                # # cv2.normalize(noisy_frame, noisy_frame, 0, 255, cv2.NORM_MINMAX)
                # output.write(gauss)
                
            else:
                break
        print("Completed!")
        output.release()

    def median_blur(vid,path):
        name = "medianblur"
        print("Removing noise through Median Filtering...")
        output = Functions.intialize_output(name,vid,path)

        while(vid.isOpened()):
            ret, frame = vid.read()
            if ret == True:
                # Add Median Blur Here
                grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                new_frame = cv2.medianBlur(grey_frame, 5)
                output.write(new_frame)
                
            else:
                break
        print("Completed!")
        output.release()

    def combine_videos(vid, path):
        name="combine"
        new_vid_path = input("Video Path: ")

        col,row = Functions.get_framesize(vid)
        col = col*2
        new_capture = cv2.VideoCapture(new_vid_path)

        if (Functions.get_framecount(vid)== Functions.get_framecount(new_capture) and Functions.get_framerate(vid)== Functions.get_framerate(new_capture)):
            print("Combining "+ Functions.get_video_name(path) + "&"+  Functions.get_video_name(new_vid_path)+" ...")
            output = cv2.VideoWriter('results/'+name+'.mp4', -1, Functions.get_framerate(vid), (col,row) , 0)

            while(vid.isOpened()):
                ret, org = vid.read()
                ret2, new = new_capture.read()
                if ret == True:
                    # Combine Frames here
                    combined_frame = np.concatenate((org, new), axis=1)

                    output.write(combined_frame)
                    
                else:
                    break
            print("Completed!")
            output.release()
        else:
            print("Videos must have the same size, framerate, and framecount")

# References

# ***************************************************************************************/
# *    Title: CHANGE THE BRIGHTNESS AND CONTRAST OF IMAGES USING OPENCV PYTHON
# *    Author: Life2Coding
# *    Date: 2022
# *    Availability: https://www.life2coding.com/change-brightness-and-contrast-of-images-using-opencv-python/
# *
# ***************************************************************************************/