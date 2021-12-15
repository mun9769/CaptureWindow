import win32gui
import pyautogui
from PIL import Image

x1, x2, y1, y2 = 1, 1, 1, 1
flag = False

# garbage code 
def callback(hwnd, extra):
    if win32gui.GetWindowText(hwnd) == "":
        return
    if win32gui.GetWindowText(hwnd)[0] == "M":
        rect = win32gui.GetWindowRect(hwnd)
        if rect[0] == 0:
            return
        global x1, y1, x2, y2, flag
        if flag == True:
            return
        flag = True
        x1 = rect[0] + 70
        y1 = rect[1] + 130
        x2 = rect[2] - 10
        y2 = rect[3] - 50
        print("{0} {1} {2} {3}".format(x1,y1,x2,y2))

win32gui.EnumWindows(callback, None)

for i in range(0,1):
    path = '/Users/moon/Desktop/result{0}.png'.format(i)

    pyautogui.screenshot(path)
    pyautogui.click(x2-50, y2-500)

    im = Image.open(path)
    im = im.crop((x1, y1, x2, y2))
    im.save(path)
