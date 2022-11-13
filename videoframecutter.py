import os
import cv2
import moviepy.editor

frameList = []
def getFrames(vid, output, rate=0.2, frameName='frame'):
    vidcap = cv2.VideoCapture(vid)
    clip = moviepy.editor.VideoFileClip(vid)

    seconds = clip.duration
    print('durration: ' + str(seconds))
    
    count = 0
    frame = 0
    
    if not os.path.isdir(output):
        os.mkdir(output)
    
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,frame*1000)      
        success,image = vidcap.read()
        try:
            Ximage = cv2.resize(image, (200,150), interpolation = cv2.INTER_NEAREST)
        except Exception as e:
            print(str(e))
        ## Stop when last frame is identified
        print(frame)
        if frame > seconds or not success:
            break
        
        print('extracting frame ' + frameName + '-%d.png' % count)
        frameList.append(Ximage)
        frame += rate
        count += 1
    
    
    return frameList