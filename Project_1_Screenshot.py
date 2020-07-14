import time
import pyautogui

def screenshot():
    name=int(round(time.time()*1000))
    name='D:/College/OTHERS/Udemy/Python 20plus projects Arbaz/screenshots_data/{}.png'.format(name)

    time.sleep(5)
    img=pyautogui.screenshot(name)
    img.show()

screenshot()