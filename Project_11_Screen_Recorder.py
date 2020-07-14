import numpy as np
import cv2

from PIL import ImageGrab

def ScreenRec():
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter("output.avi",fourcc,5.0,(1366,7680))
    while True:
        img=ImageGrab.grab()
        img_np=np.array(img)
        frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
        cv2.imshow("Screen Recorder",frame)
        out.write(frame)

        if(cv2.waitKey(1))==27:
            break
    out.release()
    cv2.destroyAllWindows()

ScreenRec()
