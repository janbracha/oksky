from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# Adding widgets to the root window
#Label(root, text = 'GeeksforGeeks', font =(
#  'Verdana', 15)).pack(side = TOP, pady = 10)



# Creating a photoimage object to use image
photo = PhotoImage(file = "pac750PNG.png")
label_1=Label(root, image = photo)
label_1.grid(row=0,column=0)
# here, image option is used to
# set image on button

#Label(root, image = photo).pack(side = TOP)

mainloop()
