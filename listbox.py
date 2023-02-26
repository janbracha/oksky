from tkinter import *

OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc

master = Tk()

variable = StringVar(master)
#variable.set(OPTIONS[0]) # default value
print (variable.get())
w = OptionMenu(master, variable, *OPTIONS)
w.pack()
print (variable.get())

def ok():
    print (variable.get())

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()
