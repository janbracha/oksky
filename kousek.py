import pyautogui
import win32gui

def screenshot(window_title=PICA):
    if window_title:
        hwnd = win32gui.FindWindow(PICA, window_title)
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im


im = screenshot('Calculator')
if im:
    im.show()

my_window=Tk ()
my_window.title("PICA")
label_venkovni_teplota=Label(my_window,text="OAT Celsius")
label_venkovni_teplota.grid(row=5,column=2)
button_1=Button(my_window,text="Compute W&B",command=screenshot)
button_1.grid(row=16,column=1)

my_window.mainloop ()
