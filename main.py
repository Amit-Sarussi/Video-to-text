from videoframecutter import getFrames
from time import perf_counter
import time
from imgtotext import itt
# fps = int(input("How many frames per second?"))
# videoFile = input("Where is the video file located?")

if __name__ == '__main__':
    x = []
    start = perf_counter()
    frames = itt(getFrames('BadApple.mp4', 'frames'))
    end = perf_counter()
    for i in range(len(frames)):
        print(frames[i])
        time.sleep(0.15)
    print(f'Time: {end-start} sec')