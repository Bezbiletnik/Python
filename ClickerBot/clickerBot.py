import pyautogui
import time 
import keyboard
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    img = pyautogui.screenshot(region=(405 , 250 , 1050 , 640))
    width, height = img.size
    #Color: (122 , 138 , 162)
    for x in range (0 , width, 5):
        for y in range (0 , height , 5):
            r,g,b = img.getpixel(x, y)
            if r == 122:
                click(x+405 , y+250)
