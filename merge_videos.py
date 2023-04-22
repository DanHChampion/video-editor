import cv2
import numpy as np

def combine_videos(vid, algo):
        
        vid1 = cv2.VideoCapture(vid+"_vid.mp4")
        vid2 = cv2.VideoCapture(vid+"_"+algo+"1.mp4")
        vid3 = cv2.VideoCapture(vid+"_"+algo+"2.mp4")
        vid4 = cv2.VideoCapture(vid+"_"+algo+"3.mp4")

        (col,row) = (int(vid1.get(3)), int(vid1.get(4)))
        col = col*2
        row = row*2
        
        print("Combining "+vid+"_"+algo+" ...")
        output = cv2.VideoWriter("combined_"+vid+"_"+algo+".mp4", -1, vid1.get(5), (col,row) , 0)

        while(vid1.isOpened()):
            ret, frame1 = vid1.read()
            ret2, frame2 = vid2.read()
            ret, frame3 = vid3.read()
            ret2, frame4 = vid4.read()
            
            if ret == True:
                # Combine Frames here
                top_row = np.concatenate((frame1, frame2), axis=1)
                bottom_row = np.concatenate((frame3, frame4), axis=1)
                combined_frame = np.concatenate((top_row, bottom_row), axis=0)

                output.write(combined_frame)
                
            else:
                break
        print("Completed!")
        output.release()

VIDEOS = ["sunflower", "dog", "beach"]
TECHNIQUES = ["cc","ct","fg","dn"]

for video in VIDEOS:
     for technique in TECHNIQUES:
          combine_videos(video,technique) 

