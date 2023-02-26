from tkinter import *


def clear_form():
    label_2.grid_forget()
#    label_16=Label(my_window,text="")

my_window=Tk ()

label_1=Label(my_window,text="Pilot Name:")
label_1.grid(row=0,column=0)
label_2=Label(my_window,text="BLABLA")
label_2.grid(row=0,column=1)

button_2=Button(my_window,text="Vymazat formular",command=clear_form)
button_2.grid(row=1,column=0)

my_window.mainloop ()
