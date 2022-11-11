import cv2 

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
                output.write(frame)
            else:
                break
        
        print("Completed!")
        output.release()

    def adjust_contrast(vid,path):
        constrast_value = int(input("Constrast Value (-255,255): "))
        name = "contrast" + str(constrast_value)
        print("Adjusting Constrast by "+str(constrast_value)+" ...")
        output = Functions.intialize_output(name,vid,path)
        
        while(vid.isOpened()):
            ret, frame = vid.read()
            if ret == True:
                # Adjust Constrast Here
                output.write(frame)
            else:
                break
        
        print("Completed!")
        output.release()

