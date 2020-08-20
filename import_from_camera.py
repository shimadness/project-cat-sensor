import cv2
from datetime import datetime as dt
import time
import os
import datetime
import glob

def capture_from_camera(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap_cam = cv2.VideoCapture(device_num)
#    print(type(cap_cam))
    # <class 'cv2.VideoCapture'>

    if not cap_cam.isOpened():
        return
    #    print("camera error!!!")

    os.makedirs(dir_path, exist_ok=True)
    base_path=os.path.join(dir_path, basename)

    print(cap_cam.isOpened())
    # True

    n=0
    while True:
        ret, frame = cap_cam.read()
        #cv2.imshow(window_name,frame)
        datetime=dt.now()
        tstr= datetime.strftime('%Y%m%d%H%M%S')
        cv2.imwrite('{}_{}.{}'.format(base_path, tstr, ext), frame)
        time.sleep(1)
        #cv2.destroyAllWindows()
        n=n+1
        # Escキーを入力したら終了
        if cv2.waitKey(1) == 27:
            break
        if n == 10:
            break
    
    #cap_cum.release()
    #cv2.destroyAllWindows()

def remove_glob(pathname, recursive=True):
    for p in glob.glob(pathname, recursive=recursive):
        if os.path.isfile(p):
            os.remove(p)

capture_from_camera(1, 'data/temp', 'camera_capture')
remove_glob('data/temp/*.jpg')
