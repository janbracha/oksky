from tkinter import *
import pyautogui
from PIL import ImageGrab
from ctypes import windll

if windll.user32.OpenClipboard(None):
    windll.user32.EmptyClipboard()


def screenshot ():
    pyautogui.hotkey('alt', 'printscreen')
    img = ImageGrab.grabclipboard()
    img.save('blabla.png', 'PNG')
    img1 = ImageGrab.grabclipboard()
    img1.save('test.jpg', 'JPEG')



my_window=Tk ()
my_window.title("PICA")
label_venkovni_teplota=Label(my_window,text="fffgrerewgssssssffff")
label_venkovni_teplota.grid(row=5,column=2)
button_1=Button(my_window,text="Compute W&B",command=screenshot)
button_1.grid(row=16,column=1)

my_window.mainloop ()

#im1 = Image.open(r"C:\Users\sadow984\Desktop\download2.JPG")
