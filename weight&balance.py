from tkinter import *

def clear_form():

def weight_balance():
    pocet_skokanu = entry_2.get()
    prazdna_hmotnost = 3500
    pocet_litru = entry_3.get()
    vaha_skokanu =  float(pocet_skokanu) * 200
    vaha_paliva = float(pocet_litru) * 0.78
    vaha_pilota = entry_4.get()
    vaha_pilota_pounds =float(vaha_pilota) * 2.2
    vzletova_hmotnost= vaha_paliva + vaha_skokanu + vaha_pilota_pounds + prazdna_hmotnost
#pridano check na MTOW
    if vzletova_hmotnost >=7500:
        label_15=Label(my_window,text="MTOW PREKROCEN !!!",bg="red",fg="blue", font="Times 12 bold")
        label_15.grid(row=11,column=1)
    else:
        label_16=Label(my_window,text="MTOW v limitech, start povolen!!",bg="green")
        label_16.grid(row=11,column=1)

    string_to_display = vaha_skokanu, "Liber"
    string_to_display_2 = str (round(vaha_paliva, 1)), "Liber"
    string_to_display_3 = str (round(vaha_pilota_pounds, 1)), "Liber"
    string_to_display_4 = str (round(vzletova_hmotnost, 1)), "Liber"
    label_5=Label (my_window)
    label_5["text"]=string_to_display
    label_5.grid(row=4,column=1)
    label_7=Label (my_window)
    label_7["text"]=string_to_display_2
    label_7.grid(row=5,column=1)
    label_12=Label (my_window)
    label_12["text"]=string_to_display_3
    label_12.grid(row=8,column=1)
    label_14=Label (my_window)
    label_14["text"]=string_to_display_4
    label_14.grid(row=9,column=1)

#zaokrouhleni answer = str(round(answer, 2))


my_window=Tk ()
my_window.title("weight & balance")
#my_window.geometry("300+100")

label_1=Label(my_window,text="Jmeno pilota:")
label_10=Label(my_window,text="vaha pilota v kg")
label_11=Label(my_window,text="vaha pilota  je")
label_2=Label(my_window,text="pocet skokanu:")
Label_3=Label(my_window,text="pocet litru JetA1")
Label_4=Label(my_window,text="Celkova vaha skokanu je")
Label_6=Label(my_window,text="Celkova vaha paliva je")
Label_8=Label(my_window,text="Prazdna hmotnost letadla je")
Label_9=Label(my_window,text="3500 Liber")
label_13=Label(my_window,text="Vzletova hmotnost je")
label_10.grid(row=3,column=0)
label_11.grid(row=8,column=0)
Label_8.grid(row=6,column=0)
Label_9.grid(row=6,column=1)
Label_4.grid(row=4,column=0)
label_1.grid(row=0,column=0)
label_2.grid(row=1,column=0)
Label_3.grid(row=2,column=0)
Label_6.grid(row=5,column=0)
label_13.grid(row=9,column=0)
entry_1=Entry(my_window)
entry_2=Entry(my_window)
entry_3=Entry(my_window)
entry_4=Entry(my_window)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)
entry_3.grid(row=2,column=1)
entry_4.grid(row=3,column=1)
button_1=Button(my_window,text="Compute W&B",command=weight_balance)
button_1.grid(row=12,column=1)
button_2=Button(my_window,text="Vymazat formular",command=clear_form)
button_2.grid(row=13,column=0)
my_window.mainloop ()
