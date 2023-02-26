from tkinter import *

#definice promenych
skokan_1_rameno=66.5
skokan_2_rameno=93
skokan_3_rameno=93
skokan_4_rameno=106.25
skokan_5_rameno=106.25
skokan_6_rameno=119.5
skokan_7_rameno=119.5
skokan_8_rameno=132.75
skokan_9_rameno=132.75
skokan_10_rameno=146
skokan_11_rameno=146
skokan_12_rameno=159.25
skokan_13_rameno=159.25
skokan_14_rameno=172.5
skokan_15_rameno=172.5
skokan_16_rameno=185.75
skokan_17_rameno=185.75
pilot_rameno=66.5
palivo_rameno=110.2
vaha_skokana_pounds=200




def weight_balance():
    pocet_skokanu = entry_2.get()
    if float(pocet_skokanu) >= 18:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        label_16=Label(my_window,text="Maximalni pocet skokaku je 17")
        label_16.grid(row=13,column=0)
    elif float(pocet_skokanu) >= 1:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
    else:
        label_16=Label(my_window,text="zadany neplatny pocet skokanu")
        label_16.grid(row=13,column=0)

    prazdna_hmotnost = 3500
    pocet_litru = entry_3.get()
    vaha_paliva = float(pocet_litru) * 0.78
    vaha_paliva_pounds = vaha_paliva * 2.2
    vaha_pilota = entry_4.get()
    vaha_pilota_pounds =float(vaha_pilota) * 2.2
    vzletova_hmotnost= vaha_paliva_pounds + vaha_skokanu + vaha_pilota_pounds + prazdna_hmotnost
    moment_skokan1=skokan_1_rameno * vaha_skokana_pounds
    moment_skokan2=skokan_2_rameno * vaha_skokana_pounds
    moment_skokan3=skokan_3_rameno * vaha_skokana_pounds
    moment_skokan4=skokan_4_rameno * vaha_skokana_pounds
    moment_skokan5=skokan_5_rameno * vaha_skokana_pounds
    moment_skokan6=skokan_6_rameno * vaha_skokana_pounds
    moment_skokan7=skokan_7_rameno * vaha_skokana_pounds
    moment_skokan8=skokan_8_rameno * vaha_skokana_pounds
    moment_skokan9=skokan_9_rameno * vaha_skokana_pounds
    moment_skokan10=skokan_10_rameno * vaha_skokana_pounds
    moment_skokan11=skokan_11_rameno * vaha_skokana_pounds
    moment_skokan12=skokan_12_rameno * vaha_skokana_pounds
    moment_skokan13=skokan_13_rameno * vaha_skokana_pounds
    moment_skokan14=skokan_14_rameno * vaha_skokana_pounds
    moment_skokan15=skokan_15_rameno * vaha_skokana_pounds
    moment_skokan16=skokan_16_rameno * vaha_skokana_pounds
    moment_skokan17=skokan_17_rameno * vaha_skokana_pounds
    moment_pilot=pilot_rameno * vaha_pilota_pounds
    moment_palivo=palivo_rameno * vaha_paliva_pounds

    if vzletova_hmotnost >=7500:
        label_15=Label(my_window,text="MTOW PREKROCEN !!!",bg="red",fg="blue")
        label_15.grid(row=11,column=1)
    else:
        label_16=Label(my_window,text="MTOW v limitech, start povolen!!",bg="green")
        label_16.grid(row=11,column=1)

    string_to_display = vaha_skokanu, "Liber"
    string_to_display_2 = str (round(vaha_paliva_pounds, 1)), "Liber"
    string_to_display_3 = str (round(vaha_pilota_pounds, 1)), "Liber"
    string_to_display_4 = str (round(vzletova_hmotnost, 1)), "Liber"
    string_to_display_moment1= str (round(moment_skokan1, 1)), "lb.in"
    string_to_display_moment2= str (round(moment_skokan2, 1)), "lb.in"
    string_to_display_moment3= str (round(moment_skokan3, 1)), "lb.in"
    string_to_display_moment4= str (round(moment_skokan4, 1)), "lb.in"
    string_to_display_moment5= str (round(moment_skokan5, 1)), "lb.in"
    string_to_display_moment6= str (round(moment_skokan6, 1)), "lb.in"
    string_to_display_moment7= str (round(moment_skokan7, 1)), "lb.in"
    string_to_display_moment8= str (round(moment_skokan8, 1)), "lb.in"
    string_to_display_moment9= str (round(moment_skokan9, 1)), "lb.in"
    string_to_display_moment10= str (round(moment_skokan10, 1)), "lb.in"
    string_to_display_moment11= str (round(moment_skokan11, 1)), "lb.in"
    string_to_display_moment12= str (round(moment_skokan12, 1)), "lb.in"
    string_to_display_moment13= str (round(moment_skokan13, 1)), "lb.in"
    string_to_display_moment14= str (round(moment_skokan14, 1)), "lb.in"
    string_to_display_moment15= str (round(moment_skokan15, 1)), "lb.in"
    string_to_display_moment16= str (round(moment_skokan16, 1)), "lb.in"
    string_to_display_moment17= str (round(moment_skokan17, 1)), "lb.in"
    string_to_display_moment18= str (round(moment_pilot, 1)), "lb.in"
    string_to_display_moment19= str (round(moment_palivo, 1)), "lb.in"

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

    label_2_1_1=Label (my_window)
    label_2_1_1["text"]=string_to_display_moment1
    label_2_1_1.grid(row=0,column=3)

    label_2_1_2=Label (my_window)
    label_2_1_2["text"]=string_to_display_moment2
    label_2_1_2.grid(row=1,column=3)

    label_2_1_3=Label (my_window)
    label_2_1_3["text"]=string_to_display_moment3
    label_2_1_3.grid(row=2,column=3)

    label_2_1_4=Label (my_window)
    label_2_1_4["text"]=string_to_display_moment4
    label_2_1_4.grid(row=3,column=3)

    label_2_1_5=Label (my_window)
    label_2_1_5["text"]=string_to_display_moment5
    label_2_1_5.grid(row=4,column=3)

    label_2_1_6=Label (my_window)
    label_2_1_6["text"]=string_to_display_moment6
    label_2_1_6.grid(row=5,column=3)

    label_2_1_7=Label (my_window)
    label_2_1_7["text"]=string_to_display_moment7
    label_2_1_7.grid(row=6,column=3)

    label_2_1_8=Label (my_window)
    label_2_1_8["text"]=string_to_display_moment8
    label_2_1_8.grid(row=7,column=3)

    label_2_1_9=Label (my_window)
    label_2_1_9["text"]=string_to_display_moment9
    label_2_1_9.grid(row=8,column=3)

    label_2_1_10=Label (my_window)
    label_2_1_10["text"]=string_to_display_moment10
    label_2_1_10.grid(row=9,column=3)

    label_2_1_11=Label (my_window)
    label_2_1_11["text"]=string_to_display_moment11
    label_2_1_11.grid(row=10,column=3)

    label_2_1_12=Label (my_window)
    label_2_1_12["text"]=string_to_display_moment12
    label_2_1_12.grid(row=11,column=3)

    label_2_1_13=Label (my_window)
    label_2_1_13["text"]=string_to_display_moment13
    label_2_1_13.grid(row=12,column=3)

    label_2_1_14=Label (my_window)
    label_2_1_14["text"]=string_to_display_moment14
    label_2_1_14.grid(row=13,column=3)

    label_2_1_15=Label (my_window)
    label_2_1_15["text"]=string_to_display_moment15
    label_2_1_15.grid(row=14,column=3)

    label_2_1_16=Label (my_window)
    label_2_1_16["text"]=string_to_display_moment16
    label_2_1_16.grid(row=15,column=3)

    label_2_1_17=Label (my_window)
    label_2_1_17["text"]=string_to_display_moment17
    label_2_1_17.grid(row=16,column=3)

    label_2_1_18=Label (my_window)
    label_2_1_18["text"]=string_to_display_moment18
    label_2_1_18.grid(row=17,column=3)

    label_2_1_19=Label (my_window)
    label_2_1_19["text"]=string_to_display_moment19
    label_2_1_19.grid(row=18,column=3)




def clear_form():
    entry_1.delete(first=0,last=100)
    entry_2.delete(first=0,last=100)
    entry_3.delete(first=0,last=100)
    entry_4.delete(first=0,last=100)
    label_5=Label (my_window,text="                               ")
    label_5.grid(row=4,column=1)
    label_7=Label (my_window,text="                               ")
    label_7.grid(row=5,column=1)
    label_12=Label (my_window,text="                              ")
    label_12.grid(row=8,column=1)
    label_14=Label (my_window,text="                              ")
    label_14.grid(row=9,column=1)
    label_15=Label (my_window,text="                                                           ",bg="#F0F0F0",fg="#F0F0F0")
    label_15.grid(row=11,column=1)
    label_16=Label(my_window,text="")
    label_16.grid(row=13,column=0)
    label_16.destroy()



my_window=Tk ()
my_window.title("weight & balance")


#canvas=Canvas(my_window,width=400,height=250)
#image=ImageTk.PhotoImage(Image.open("pac750PNG.png"))
#canvas.create_image(0,0,anchor=NW,image=image)
#canvas.grid(row=0,column=0)



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
button_2.grid(row=12,column=0)

label_2_1=Label(my_window,text="Moment skokan 1 je :")
label_2_1.grid(row=0,column=2)
label_2_2=Label(my_window,text="Moment skokan 2 je :")
label_2_2.grid(row=1,column=2)
label_2_1=Label(my_window,text="Moment skokan 3 je :")
label_2_1.grid(row=2,column=2)
label_2_1=Label(my_window,text="Moment skokan 4 je :")
label_2_1.grid(row=3,column=2)
label_2_1=Label(my_window,text="Moment skokan 5 je :")
label_2_1.grid(row=4,column=2)
label_2_1=Label(my_window,text="Moment skokan 6 je :")
label_2_1.grid(row=5,column=2)
label_2_1=Label(my_window,text="Moment skokan 7 je :")
label_2_1.grid(row=6,column=2)
label_2_1=Label(my_window,text="Moment skokan 8 je :")
label_2_1.grid(row=7,column=2)
label_2_1=Label(my_window,text="Moment skokan 9 je :")
label_2_1.grid(row=8,column=2)
label_2_1=Label(my_window,text="Moment skokan 10 je :")
label_2_1.grid(row=9,column=2)
label_2_1=Label(my_window,text="Moment skokan 11 je :")
label_2_1.grid(row=10,column=2)
label_2_1=Label(my_window,text="Moment skokan 12 je :")
label_2_1.grid(row=11,column=2)
label_2_1=Label(my_window,text="Moment skokan 13 je :")
label_2_1.grid(row=12,column=2)
label_2_1=Label(my_window,text="Moment skokan 14 je :")
label_2_1.grid(row=13,column=2)
label_2_1=Label(my_window,text="Moment skokan 15 je :")
label_2_1.grid(row=14,column=2)
label_2_1=Label(my_window,text="Moment skokan 16 je :")
label_2_1.grid(row=15,column=2)
label_2_1=Label(my_window,text="Moment skokan 17 je :")
label_2_1.grid(row=16,column=2)
label_2_1=Label(my_window,text="Moment pilota je :")
label_2_1.grid(row=17,column=2)
label_2_1=Label(my_window,text="Moment paliva je :")
label_2_1.grid(row=18,column=2)


my_window.mainloop ()
