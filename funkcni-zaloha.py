from tkinter import *
import math
import os
import time



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
letoun_rameno=109.71
prazdna_hmotnost = 3506
vaha_skokana_pounds=200
palivo_zadni_rameno=139.15


#zadani aktualniho casu
secondsSinceEpoch = time.time()
timeObj = time.localtime(secondsSinceEpoch)
current_timestamt=('%d-%d-%d-%d-%d-%d' % (timeObj.tm_mday, timeObj.tm_mon, timeObj.tm_year, timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))
#konec zadani aktualniho casu




def weight_balance():
    pocet_skokanu = entry_2.get()
    pocet_litru = entry_3.get()
#pridana zadni ndarz
    pocet_litru_zadni = entry_zadni_nadrz.get()
    vaha_paliva_zadni = float(pocet_litru_zadni) * 0.78
    vaha_paliva_zadni_pounds = vaha_paliva_zadni * 2.2
#konec zadni nadrze
    vaha_paliva = float(pocet_litru) * 0.78
    vaha_paliva_pounds = vaha_paliva * 2.2
    vaha_paliva_predni_zadni_pounds = vaha_paliva_pounds +vaha_paliva_zadni_pounds
    vaha_pilota = entry_4.get()
    vaha_pilota_pounds =float(vaha_pilota) * 2.2
    vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
    vzletova_hmotnost= vaha_paliva_pounds + vaha_skokanu + vaha_pilota_pounds + prazdna_hmotnost + vaha_paliva_zadni_pounds
#crosswind vypocet
    smer_vetru_vypocet = float(entry_smer_vetru_vzlet.get())
    sila_vetru_vypocet = float(entry_sila_vetru.get())
    smer_drahy_vypocet = float(entry_smer_drahy.get())
    crosswind_drif = smer_vetru_vypocet - smer_drahy_vypocet
    crosswind = math.sin(crosswind_drif) * sila_vetru_vypocet
    string_to_display_crosswind= str (round(crosswind, 1)), "kts"
    label_crosswind_vypocet=Label(my_window,text="Crosswind for take off is")
    label_crosswind_vypocet.grid(row=14,column=2)
    laebel_current_crosswind=Label(my_window)
    laebel_current_crosswind["text"]=string_to_display_crosswind
    laebel_current_crosswind.grid(row=14,column=3)

    if crosswind <=14:
        label_crosswind_demonstrated=Label(my_window,text="Crosswind within limits, take off approved",bg="green")
        label_crosswind_demonstrated.grid(row=15,column=2)
    else:
        label_crosswind_demonstrated=Label(my_window,text="Crosswind out of limits",bg="red")
        label_crosswind_demonstrated.grid(row=15,column=2)
#konec crosswind vypocet
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
    moment_palivo_zadni = palivo_zadni_rameno * vaha_paliva_zadni_pounds
    moment_letoun= prazdna_hmotnost * letoun_rameno
    string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
    string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
    string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
    string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
    string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
    string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
    string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
    string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
    string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
    string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
    string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
    string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
    string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
    string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
    string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
    string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
    string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
    string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
    string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
    string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
    string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"
    if float(pocet_skokanu) >= 18:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        label_16=Label(my_window,text="Maximum number skydivers is 17")
        label_16.grid(row=13,column=0)

    elif float(pocet_skokanu) == 1:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment=(moment_palivo_zadni) + (moment_pilot) + (moment_letoun) + (moment_palivo) + (moment_skokan1)
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is is:")
        label_2_2.grid(row=1,column=4)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)
    elif float(pocet_skokanu) == 2:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1 + moment_skokan2
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)


        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)
    elif float(pocet_skokanu) == 3:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment=  moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1 + moment_skokan2 + moment_skokan3
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)
    elif float(pocet_skokanu) == 4:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)
    elif float(pocet_skokanu) == 5:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4+moment_skokan5
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)

        label_2_1_8=Label (my_window)
        label_2_1_8["text"]=string_to_display_moment8
        label_2_1_8.grid(row=7,column=5)
        label_2_8=Label(my_window,text="Skydiver 5 moment is:")
        label_2_8.grid(row=7,column=4)
    elif float(pocet_skokanu) == 6:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4+moment_skokan5+moment_skokan6
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)

        label_2_1_8=Label (my_window)
        label_2_1_8["text"]=string_to_display_moment8
        label_2_1_8.grid(row=7,column=5)
        label_2_8=Label(my_window,text="Skydiver 5 moment is:")
        label_2_8.grid(row=7,column=4)

        label_2_1_9=Label (my_window)
        label_2_1_9["text"]=string_to_display_moment9
        label_2_1_9.grid(row=8,column=5)
        label_2_9=Label(my_window,text="Skydiver 6 moment is:")
        label_2_9.grid(row=8,column=4)
    elif float(pocet_skokanu) == 7:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4+moment_skokan5+moment_skokan6+moment_skokan7
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)

        label_2_1_8=Label (my_window)
        label_2_1_8["text"]=string_to_display_moment8
        label_2_1_8.grid(row=7,column=5)
        label_2_8=Label(my_window,text="Skydiver 5 moment is:")
        label_2_8.grid(row=7,column=4)

        label_2_1_9=Label (my_window)
        label_2_1_9["text"]=string_to_display_moment9
        label_2_1_9.grid(row=8,column=5)
        label_2_9=Label(my_window,text="Skydiver 6 moment is:")
        label_2_9.grid(row=8,column=4)

        label_2_1_10=Label (my_window)
        label_2_1_10["text"]=string_to_display_moment10
        label_2_1_10.grid(row=9,column=5)
        label_2_10=Label(my_window,text="Skydiver 7 moment is:")
        label_2_10.grid(row=9,column=4)
    elif float(pocet_skokanu) == 8:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4+moment_skokan5+moment_skokan6+moment_skokan7+moment_skokan8
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)

        label_2_1_8=Label (my_window)
        label_2_1_8["text"]=string_to_display_moment8
        label_2_1_8.grid(row=7,column=5)
        label_2_8=Label(my_window,text="Skydiver 5 moment is:")
        label_2_8.grid(row=7,column=4)

        label_2_1_9=Label (my_window)
        label_2_1_9["text"]=string_to_display_moment9
        label_2_1_9.grid(row=8,column=5)
        label_2_9=Label(my_window,text="Skydiver 6 moment is:")
        label_2_9.grid(row=8,column=4)

        label_2_1_10=Label (my_window)
        label_2_1_10["text"]=string_to_display_moment10
        label_2_1_10.grid(row=9,column=5)
        label_2_10=Label(my_window,text="Skydiver 7 moment is:")
        label_2_10.grid(row=9,column=4)

        label_2_1_11=Label (my_window)
        label_2_1_11["text"]=string_to_display_moment11
        label_2_1_11.grid(row=10,column=5)
        label_2_11=Label(my_window,text="Skydiver 8 moment is:")
        label_2_11.grid(row=10,column=4)
    elif float(pocet_skokanu) == 9:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4+moment_skokan5+moment_skokan6+moment_skokan7+moment_skokan8+moment_skokan9
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)

        label_2_1_8=Label (my_window)
        label_2_1_8["text"]=string_to_display_moment8
        label_2_1_8.grid(row=7,column=5)
        label_2_8=Label(my_window,text="Skydiver 5 moment is:")
        label_2_8.grid(row=7,column=4)

        label_2_1_9=Label (my_window)
        label_2_1_9["text"]=string_to_display_moment9
        label_2_1_9.grid(row=8,column=5)
        label_2_9=Label(my_window,text="Skydiver 6 moment is:")
        label_2_9.grid(row=8,column=4)

        label_2_1_10=Label (my_window)
        label_2_1_10["text"]=string_to_display_moment10
        label_2_1_10.grid(row=9,column=5)
        label_2_10=Label(my_window,text="Skydiver 7 moment is:")
        label_2_10.grid(row=9,column=4)

        label_2_1_11=Label (my_window)
        label_2_1_11["text"]=string_to_display_moment11
        label_2_1_11.grid(row=10,column=5)
        label_2_11=Label(my_window,text="Skydiver 8 moment is:")
        label_2_11.grid(row=10,column=4)

        label_2_1_12=Label (my_window)
        label_2_1_12["text"]=string_to_display_moment12
        label_2_1_12.grid(row=11,column=5)
        label_2_12=Label(my_window,text="Skydiver 9 moment is:")
        label_2_12.grid(row=11,column=4)
    elif float(pocet_skokanu) == 10:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4+moment_skokan5+moment_skokan6+moment_skokan7+moment_skokan8+moment_skokan9+moment_skokan10
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)

        label_2_1_8=Label (my_window)
        label_2_1_8["text"]=string_to_display_moment8
        label_2_1_8.grid(row=7,column=5)
        label_2_8=Label(my_window,text="Skydiver 5 moment is:")
        label_2_8.grid(row=7,column=4)

        label_2_1_9=Label (my_window)
        label_2_1_9["text"]=string_to_display_moment9
        label_2_1_9.grid(row=8,column=5)
        label_2_9=Label(my_window,text="Skydiver 6 moment is:")
        label_2_9.grid(row=8,column=4)

        label_2_1_10=Label (my_window)
        label_2_1_10["text"]=string_to_display_moment10
        label_2_1_10.grid(row=9,column=5)
        label_2_10=Label(my_window,text="Skydiver 7 moment is:")
        label_2_10.grid(row=9,column=4)

        label_2_1_11=Label (my_window)
        label_2_1_11["text"]=string_to_display_moment11
        label_2_1_11.grid(row=10,column=5)
        label_2_11=Label(my_window,text="Skydiver 8 moment is:")
        label_2_11.grid(row=10,column=4)

        label_2_1_12=Label (my_window)
        label_2_1_12["text"]=string_to_display_moment12
        label_2_1_12.grid(row=11,column=5)
        label_2_12=Label(my_window,text="Skydiver 9 moment is:")
        label_2_12.grid(row=11,column=4)

        label_2_1_13=Label (my_window)
        label_2_1_13["text"]=string_to_display_moment13
        label_2_1_13.grid(row=12,column=5)
        label_2_13=Label(my_window,text="Skydiver 10 moment is:")
        label_2_13.grid(row=12,column=4)
    elif float(pocet_skokanu) == 11:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4+moment_skokan5+moment_skokan6+moment_skokan7+moment_skokan8+moment_skokan9+moment_skokan10+moment_skokan11
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)

        label_2_1_8=Label (my_window)
        label_2_1_8["text"]=string_to_display_moment8
        label_2_1_8.grid(row=7,column=5)
        label_2_8=Label(my_window,text="Skydiver 5 moment is:")
        label_2_8.grid(row=7,column=4)

        label_2_1_9=Label (my_window)
        label_2_1_9["text"]=string_to_display_moment9
        label_2_1_9.grid(row=8,column=5)
        label_2_9=Label(my_window,text="Skydiver 6 moment is:")
        label_2_9.grid(row=8,column=4)

        label_2_1_10=Label (my_window)
        label_2_1_10["text"]=string_to_display_moment10
        label_2_1_10.grid(row=9,column=5)
        label_2_10=Label(my_window,text="Skydiver 7 moment is:")
        label_2_10.grid(row=9,column=4)

        label_2_1_11=Label (my_window)
        label_2_1_11["text"]=string_to_display_moment11
        label_2_1_11.grid(row=10,column=5)
        label_2_11=Label(my_window,text="Skydiver 8 moment is:")
        label_2_11.grid(row=10,column=4)

        label_2_1_12=Label (my_window)
        label_2_1_12["text"]=string_to_display_moment12
        label_2_1_12.grid(row=11,column=5)
        label_2_12=Label(my_window,text="Skydiver 9 moment is:")
        label_2_12.grid(row=11,column=4)

        label_2_1_13=Label (my_window)
        label_2_1_13["text"]=string_to_display_moment13
        label_2_1_13.grid(row=12,column=5)
        label_2_13=Label(my_window,text="Skydiver 10 moment is:")
        label_2_13.grid(row=12,column=4)

        label_2_1_14=Label (my_window)
        label_2_1_14["text"]=string_to_display_moment14
        label_2_1_14.grid(row=13,column=5)
        label_2_14=Label(my_window,text="Skydiver 11 moment is:")
        label_2_14.grid(row=13,column=4)
    elif float(pocet_skokanu) == 12:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4+moment_skokan5+moment_skokan6+moment_skokan7+moment_skokan8+moment_skokan9+moment_skokan10+moment_skokan11+moment_skokan12
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)

        label_2_1_8=Label (my_window)
        label_2_1_8["text"]=string_to_display_moment8
        label_2_1_8.grid(row=7,column=5)
        label_2_8=Label(my_window,text="Skydiver 5 moment is:")
        label_2_8.grid(row=7,column=4)

        label_2_1_9=Label (my_window)
        label_2_1_9["text"]=string_to_display_moment9
        label_2_1_9.grid(row=8,column=5)
        label_2_9=Label(my_window,text="Skydiver 6 moment is:")
        label_2_9.grid(row=8,column=4)

        label_2_1_10=Label (my_window)
        label_2_1_10["text"]=string_to_display_moment10
        label_2_1_10.grid(row=9,column=5)
        label_2_10=Label(my_window,text="Skydiver 7 moment is:")
        label_2_10.grid(row=9,column=4)

        label_2_1_11=Label (my_window)
        label_2_1_11["text"]=string_to_display_moment11
        label_2_1_11.grid(row=10,column=5)
        label_2_11=Label(my_window,text="Skydiver 8 moment is:")
        label_2_11.grid(row=10,column=4)

        label_2_1_12=Label (my_window)
        label_2_1_12["text"]=string_to_display_moment12
        label_2_1_12.grid(row=11,column=5)
        label_2_12=Label(my_window,text="Skydiver 9 moment is:")
        label_2_12.grid(row=11,column=4)

        label_2_1_13=Label (my_window)
        label_2_1_13["text"]=string_to_display_moment13
        label_2_1_13.grid(row=12,column=5)
        label_2_13=Label(my_window,text="Skydiver 10 moment is:")
        label_2_13.grid(row=12,column=4)

        label_2_1_14=Label (my_window)
        label_2_1_14["text"]=string_to_display_moment14
        label_2_1_14.grid(row=13,column=5)
        label_2_14=Label(my_window,text="Skydiver 11 moment is:")
        label_2_14.grid(row=13,column=4)

        label_2_1_15=Label (my_window)
        label_2_1_15["text"]=string_to_display_moment15
        label_2_1_15.grid(row=14,column=5)
        label_2_15=Label(my_window,text="Skydiver 12 moment is:")
        label_2_15.grid(row=14,column=4)
    elif float(pocet_skokanu) == 13:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4+moment_skokan5+moment_skokan6+moment_skokan7+moment_skokan8+moment_skokan9+moment_skokan10+moment_skokan11+moment_skokan12+moment_skokan13
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)

        label_2_1_8=Label (my_window)
        label_2_1_8["text"]=string_to_display_moment8
        label_2_1_8.grid(row=7,column=5)
        label_2_8=Label(my_window,text="Skydiver 5 moment is:")
        label_2_8.grid(row=7,column=4)

        label_2_1_9=Label (my_window)
        label_2_1_9["text"]=string_to_display_moment9
        label_2_1_9.grid(row=8,column=5)
        label_2_9=Label(my_window,text="Skydiver 6 moment is:")
        label_2_9.grid(row=8,column=4)

        label_2_1_10=Label (my_window)
        label_2_1_10["text"]=string_to_display_moment10
        label_2_1_10.grid(row=9,column=5)
        label_2_10=Label(my_window,text="Skydiver 7 moment is:")
        label_2_10.grid(row=9,column=4)

        label_2_1_11=Label (my_window)
        label_2_1_11["text"]=string_to_display_moment11
        label_2_1_11.grid(row=10,column=5)
        label_2_11=Label(my_window,text="Skydiver 8 moment is:")
        label_2_11.grid(row=10,column=4)

        label_2_1_12=Label (my_window)
        label_2_1_12["text"]=string_to_display_moment12
        label_2_1_12.grid(row=11,column=5)
        label_2_12=Label(my_window,text="Skydiver 9 moment is:")
        label_2_12.grid(row=11,column=4)

        label_2_1_13=Label (my_window)
        label_2_1_13["text"]=string_to_display_moment13
        label_2_1_13.grid(row=12,column=5)
        label_2_13=Label(my_window,text="Skydiver 10 moment is:")
        label_2_13.grid(row=12,column=4)

        label_2_1_14=Label (my_window)
        label_2_1_14["text"]=string_to_display_moment14
        label_2_1_14.grid(row=13,column=5)
        label_2_14=Label(my_window,text="Skydiver 11 moment is:")
        label_2_14.grid(row=13,column=4)

        label_2_1_15=Label (my_window)
        label_2_1_15["text"]=string_to_display_moment15
        label_2_1_15.grid(row=14,column=5)
        label_2_15=Label(my_window,text="Skydiver 12 moment is:")
        label_2_15.grid(row=14,column=4)

        label_2_1_16=Label (my_window)
        label_2_1_16["text"]=string_to_display_moment16
        label_2_1_16.grid(row=15,column=5)
        label_2_16=Label(my_window,text="Skydiver 13 moment is:")
        label_2_16.grid(row=15,column=4)
    elif float(pocet_skokanu) == 14:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4+moment_skokan5+moment_skokan6+moment_skokan7+moment_skokan8+moment_skokan9+moment_skokan10+moment_skokan11+moment_skokan12+moment_skokan13+moment_skokan14
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)

        label_2_1_8=Label (my_window)
        label_2_1_8["text"]=string_to_display_moment8
        label_2_1_8.grid(row=7,column=5)
        label_2_8=Label(my_window,text="Skydiver 5 moment is:")
        label_2_8.grid(row=7,column=4)

        label_2_1_9=Label (my_window)
        label_2_1_9["text"]=string_to_display_moment9
        label_2_1_9.grid(row=8,column=5)
        label_2_9=Label(my_window,text="Skydiver 6 moment is:")
        label_2_9.grid(row=8,column=4)

        label_2_1_10=Label (my_window)
        label_2_1_10["text"]=string_to_display_moment10
        label_2_1_10.grid(row=9,column=5)
        label_2_10=Label(my_window,text="Skydiver 7 moment is:")
        label_2_10.grid(row=9,column=4)

        label_2_1_11=Label (my_window)
        label_2_1_11["text"]=string_to_display_moment11
        label_2_1_11.grid(row=10,column=5)
        label_2_11=Label(my_window,text="Skydiver 8 moment is:")
        label_2_11.grid(row=10,column=4)

        label_2_1_12=Label (my_window)
        label_2_1_12["text"]=string_to_display_moment12
        label_2_1_12.grid(row=11,column=5)
        label_2_12=Label(my_window,text="Skydiver 9 moment is:")
        label_2_12.grid(row=11,column=4)

        label_2_1_13=Label (my_window)
        label_2_1_13["text"]=string_to_display_moment13
        label_2_1_13.grid(row=12,column=5)
        label_2_13=Label(my_window,text="Skydiver 10 moment is:")
        label_2_13.grid(row=12,column=4)

        label_2_1_14=Label (my_window)
        label_2_1_14["text"]=string_to_display_moment14
        label_2_1_14.grid(row=13,column=5)
        label_2_14=Label(my_window,text="Skydiver 11 moment is:")
        label_2_14.grid(row=13,column=4)

        label_2_1_15=Label (my_window)
        label_2_1_15["text"]=string_to_display_moment15
        label_2_1_15.grid(row=14,column=5)
        label_2_15=Label(my_window,text="Skydiver 12 moment is:")
        label_2_15.grid(row=14,column=4)

        label_2_1_16=Label (my_window)
        label_2_1_16["text"]=string_to_display_moment16
        label_2_1_16.grid(row=15,column=5)
        label_2_16=Label(my_window,text="Skydiver 13 moment is:")
        label_2_16.grid(row=15,column=4)

        label_2_1_17=Label (my_window)
        label_2_1_17["text"]=string_to_display_moment17
        label_2_1_17.grid(row=16,column=5)
        label_2_17=Label(my_window,text="Skydiver 14 moment is:")
        label_2_17.grid(row=16,column=4)
    elif float(pocet_skokanu) == 15:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4+moment_skokan5+moment_skokan6+moment_skokan7+moment_skokan8+moment_skokan9+moment_skokan10+moment_skokan11+moment_skokan12+moment_skokan13+moment_skokan14+moment_skokan15
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)

        label_2_1_8=Label (my_window)
        label_2_1_8["text"]=string_to_display_moment8
        label_2_1_8.grid(row=7,column=5)
        label_2_8=Label(my_window,text="Skydiver 5 moment is:")
        label_2_8.grid(row=7,column=4)

        label_2_1_9=Label (my_window)
        label_2_1_9["text"]=string_to_display_moment9
        label_2_1_9.grid(row=8,column=5)
        label_2_9=Label(my_window,text="Skydiver 6 moment is:")
        label_2_9.grid(row=8,column=4)

        label_2_1_10=Label (my_window)
        label_2_1_10["text"]=string_to_display_moment10
        label_2_1_10.grid(row=9,column=5)
        label_2_10=Label(my_window,text="Skydiver 7 moment is:")
        label_2_10.grid(row=9,column=4)

        label_2_1_11=Label (my_window)
        label_2_1_11["text"]=string_to_display_moment11
        label_2_1_11.grid(row=10,column=5)
        label_2_11=Label(my_window,text="Skydiver 8 moment is:")
        label_2_11.grid(row=10,column=4)

        label_2_1_12=Label (my_window)
        label_2_1_12["text"]=string_to_display_moment12
        label_2_1_12.grid(row=11,column=5)
        label_2_12=Label(my_window,text="Skydiver 9 moment is:")
        label_2_12.grid(row=11,column=4)

        label_2_1_13=Label (my_window)
        label_2_1_13["text"]=string_to_display_moment13
        label_2_1_13.grid(row=12,column=5)
        label_2_13=Label(my_window,text="Skydiver 10 moment is:")
        label_2_13.grid(row=12,column=4)

        label_2_1_14=Label (my_window)
        label_2_1_14["text"]=string_to_display_moment14
        label_2_1_14.grid(row=13,column=5)
        label_2_14=Label(my_window,text="Skydiver 11 moment is:")
        label_2_14.grid(row=13,column=4)

        label_2_1_15=Label (my_window)
        label_2_1_15["text"]=string_to_display_moment15
        label_2_1_15.grid(row=14,column=5)
        label_2_15=Label(my_window,text="Skydiver 12 moment is:")
        label_2_15.grid(row=14,column=4)

        label_2_1_16=Label (my_window)
        label_2_1_16["text"]=string_to_display_moment16
        label_2_1_16.grid(row=15,column=5)
        label_2_16=Label(my_window,text="Skydiver 13 moment is:")
        label_2_16.grid(row=15,column=4)

        label_2_1_17=Label (my_window)
        label_2_1_17["text"]=string_to_display_moment17
        label_2_1_17.grid(row=16,column=5)
        label_2_17=Label(my_window,text="Skydiver 14 moment is:")
        label_2_17.grid(row=16,column=4)

        label_2_1_18=Label (my_window)
        label_2_1_18["text"]=string_to_display_moment18
        label_2_1_18.grid(row=17,column=5)
        label_2_18=Label(my_window,text="Skydiver 15 moment is:")
        label_2_18.grid(row=17,column=4)
    elif float(pocet_skokanu) == 16:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4+moment_skokan5+moment_skokan6+moment_skokan7+moment_skokan8+moment_skokan9+moment_skokan10+moment_skokan11+moment_skokan12+moment_skokan13+moment_skokan14+moment_skokan15+moment_skokan16
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)

        label_2_1_8=Label (my_window)
        label_2_1_8["text"]=string_to_display_moment8
        label_2_1_8.grid(row=7,column=5)
        label_2_8=Label(my_window,text="Skydiver 5 moment is:")
        label_2_8.grid(row=7,column=4)

        label_2_1_9=Label (my_window)
        label_2_1_9["text"]=string_to_display_moment9
        label_2_1_9.grid(row=8,column=5)
        label_2_9=Label(my_window,text="Skydiver 6 moment is:")
        label_2_9.grid(row=8,column=4)

        label_2_1_10=Label (my_window)
        label_2_1_10["text"]=string_to_display_moment10
        label_2_1_10.grid(row=9,column=5)
        label_2_10=Label(my_window,text="Skydiver 7 moment is:")
        label_2_10.grid(row=9,column=4)

        label_2_1_11=Label (my_window)
        label_2_1_11["text"]=string_to_display_moment11
        label_2_1_11.grid(row=10,column=5)
        label_2_11=Label(my_window,text="Skydiver 8 moment is:")
        label_2_11.grid(row=10,column=4)

        label_2_1_12=Label (my_window)
        label_2_1_12["text"]=string_to_display_moment12
        label_2_1_12.grid(row=11,column=5)
        label_2_12=Label(my_window,text="Skydiver 9 moment is:")
        label_2_12.grid(row=11,column=4)

        label_2_1_13=Label (my_window)
        label_2_1_13["text"]=string_to_display_moment13
        label_2_1_13.grid(row=12,column=5)
        label_2_13=Label(my_window,text="Skydiver 10 moment is:")
        label_2_13.grid(row=12,column=4)

        label_2_1_14=Label (my_window)
        label_2_1_14["text"]=string_to_display_moment14
        label_2_1_14.grid(row=13,column=5)
        label_2_14=Label(my_window,text="Skydiver 11 moment is:")
        label_2_14.grid(row=13,column=4)

        label_2_1_15=Label (my_window)
        label_2_1_15["text"]=string_to_display_moment15
        label_2_1_15.grid(row=14,column=5)
        label_2_15=Label(my_window,text="Skydiver 12 moment is:")
        label_2_15.grid(row=14,column=4)

        label_2_1_16=Label (my_window)
        label_2_1_16["text"]=string_to_display_moment16
        label_2_1_16.grid(row=15,column=5)
        label_2_16=Label(my_window,text="Skydiver 13 moment is:")
        label_2_16.grid(row=15,column=4)

        label_2_1_17=Label (my_window)
        label_2_1_17["text"]=string_to_display_moment17
        label_2_1_17.grid(row=16,column=5)
        label_2_17=Label(my_window,text="Skydiver 14 moment is:")
        label_2_17.grid(row=16,column=4)

        label_2_1_18=Label (my_window)
        label_2_1_18["text"]=string_to_display_moment18
        label_2_1_18.grid(row=17,column=5)
        label_2_18=Label(my_window,text="Skydiver 15 moment is:")
        label_2_18.grid(row=17,column=4)

        label_2_1_19=Label (my_window)
        label_2_1_19["text"]=string_to_display_moment19
        label_2_1_19.grid(row=18,column=5)
        label_2_19=Label(my_window,text="Skydiver 16 moment is:")
        label_2_19.grid(row=18,column=4)
    elif float(pocet_skokanu) == 17:
        vaha_skokanu =  float(pocet_skokanu) * vaha_skokana_pounds
        string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
        string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
        string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
        string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
        string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
        string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
        string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
        string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
        string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
        string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
        string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
        string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
        string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
        string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
        string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
        string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
        string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
        string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
        string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
        string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
        string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"

        celkovy_moment= moment_palivo_zadni + moment_pilot + moment_letoun + moment_palivo + moment_skokan1+moment_skokan2+moment_skokan3+moment_skokan4+moment_skokan5+moment_skokan6+moment_skokan7+moment_skokan8+moment_skokan9+moment_skokan10+moment_skokan11+moment_skokan12+moment_skokan13+moment_skokan14+moment_skokan15+moment_skokan16+moment_skokan17
        string_to_display_celkovy_moment = str (round(celkovy_moment, 1)), "lb.in"
        label_celkovy_moment_vysledek=Label(my_window)
        label_celkovy_moment_vysledek["text"]=string_to_display_celkovy_moment
        label_celkovy_moment_vysledek.grid(row=10,column=1)

        CG= celkovy_moment / vzletova_hmotnost
        string_to_display_CG= str (round(CG, 1)), "InAfDatum"
        laebel_CG=Label(my_window)
        laebel_CG["text"]=string_to_display_CG
        laebel_CG.grid(row=7,column=1)

        label_2_1_1=Label (my_window)
        label_2_1_1["text"]=string_to_display_moment1
        label_2_1_1.grid(row=0,column=5)
        label_2_1=Label(my_window,text="Pilot moment is :")
        label_2_1.grid(row=0,column=4)

        label_2_1_2=Label (my_window)
        label_2_1_2["text"]=string_to_display_moment2
        label_2_1_2.grid(row=1,column=5)
        label_2_1_21=Label(my_window)
        label_2_1_21["text"]=string_to_display_moment21
        label_2_1_21.grid(row=20,column=5)
        label_2_21=Label(my_window,text="Fuel moment rear tank is:")
        label_2_21.grid(row=20,column=4)
        label_2_2=Label(my_window,text="Fuel moment front tank is :")
        label_2_2.grid(row=1,column=4)

        label_2_1_3=Label (my_window)
        label_2_1_3["text"]=string_to_display_moment3
        label_2_1_3.grid(row=2,column=5)
        label_2_3=Label(my_window,text="Airplane moment is:")
        label_2_3.grid(row=2,column=4)

        label_2_1_4=Label (my_window)
        label_2_1_4["text"]=string_to_display_moment4
        label_2_1_4.grid(row=3,column=5)
        label_2_4=Label(my_window,text="Skydiver 1 moment is:")
        label_2_4.grid(row=3,column=4)

        label_2_1_5=Label (my_window)
        label_2_1_5["text"]=string_to_display_moment5
        label_2_1_5.grid(row=4,column=5)
        label_2_5=Label(my_window,text="Skydiver 2 moment is:")
        label_2_5.grid(row=4,column=4)

        label_2_1_6=Label (my_window)
        label_2_1_6["text"]=string_to_display_moment6
        label_2_1_6.grid(row=5,column=5)
        label_2_6=Label(my_window,text="Skydiver 3 moment is:")
        label_2_6.grid(row=5,column=4)

        label_2_1_7=Label (my_window)
        label_2_1_7["text"]=string_to_display_moment7
        label_2_1_7.grid(row=6,column=5)
        label_2_7=Label(my_window,text="Skydiver 4 moment is:")
        label_2_7.grid(row=6,column=4)

        label_2_1_8=Label (my_window)
        label_2_1_8["text"]=string_to_display_moment8
        label_2_1_8.grid(row=7,column=5)
        label_2_8=Label(my_window,text="Skydiver 5 moment is:")
        label_2_8.grid(row=7,column=4)

        label_2_1_9=Label (my_window)
        label_2_1_9["text"]=string_to_display_moment9
        label_2_1_9.grid(row=8,column=5)
        label_2_9=Label(my_window,text="Skydiver 6 moment is:")
        label_2_9.grid(row=8,column=4)

        label_2_1_10=Label (my_window)
        label_2_1_10["text"]=string_to_display_moment10
        label_2_1_10.grid(row=9,column=5)
        label_2_10=Label(my_window,text="Skydiver 7 moment is:")
        label_2_10.grid(row=9,column=4)

        label_2_1_11=Label (my_window)
        label_2_1_11["text"]=string_to_display_moment11
        label_2_1_11.grid(row=10,column=5)
        label_2_11=Label(my_window,text="Skydiver 8 moment is:")
        label_2_11.grid(row=10,column=4)

        label_2_1_12=Label (my_window)
        label_2_1_12["text"]=string_to_display_moment12
        label_2_1_12.grid(row=11,column=5)
        label_2_12=Label(my_window,text="Skydiver 9 moment is:")
        label_2_12.grid(row=11,column=4)

        label_2_1_13=Label (my_window)
        label_2_1_13["text"]=string_to_display_moment13
        label_2_1_13.grid(row=12,column=5)
        label_2_13=Label(my_window,text="Skydiver 10 moment is:")
        label_2_13.grid(row=12,column=4)

        label_2_1_14=Label (my_window)
        label_2_1_14["text"]=string_to_display_moment14
        label_2_1_14.grid(row=13,column=5)
        label_2_14=Label(my_window,text="Skydiver 11 moment is:")
        label_2_14.grid(row=13,column=4)

        label_2_1_15=Label (my_window)
        label_2_1_15["text"]=string_to_display_moment15
        label_2_1_15.grid(row=14,column=5)
        label_2_15=Label(my_window,text="Skydiver 12 moment is:")
        label_2_15.grid(row=14,column=4)

        label_2_1_16=Label (my_window)
        label_2_1_16["text"]=string_to_display_moment16
        label_2_1_16.grid(row=15,column=5)
        label_2_16=Label(my_window,text="Skydiver 13 moment is:")
        label_2_16.grid(row=15,column=4)

        label_2_1_17=Label (my_window)
        label_2_1_17["text"]=string_to_display_moment17
        label_2_1_17.grid(row=16,column=5)
        label_2_17=Label(my_window,text="Skydiver 14 moment is:")
        label_2_17.grid(row=16,column=4)

        label_2_1_18=Label (my_window)
        label_2_1_18["text"]=string_to_display_moment18
        label_2_1_18.grid(row=17,column=5)
        label_2_18=Label(my_window,text="Skydiver 15 moment is:")
        label_2_18.grid(row=17,column=4)

        label_2_1_19=Label (my_window)
        label_2_1_19["text"]=string_to_display_moment19
        label_2_1_19.grid(row=18,column=5)
        label_2_19=Label(my_window,text="Skydiver 16 moment is:")
        label_2_19.grid(row=18,column=4)

        label_2_1_20=Label (my_window)
        label_2_1_20["text"]=string_to_display_moment20
        label_2_1_20.grid(row=19,column=5)
        label_2_20=Label(my_window,text="Skydiver 17 moment is:")
        label_2_20.grid(row=19,column=4)
    else:
        label_16=Label(my_window,text="zadany neplatny pocet skokanu")
        label_16.grid(row=13,column=0)






    if vzletova_hmotnost >=7500:
        label_15=Label(my_window,text="MTOW over limit !!!",bg="red")
        label_15.grid(row=15,column=1)
        label_CG_result=Label(my_window,text="CG unable detrminate, MTOW over limit",bg="red")
        label_CG_result.grid(row=15,column=0)
    elif float (vzletova_hmotnost) <=4209:
        label_16=Label(my_window,text="MTOW within limits, take off approved",bg="green")
        label_16.grid(row=15,column=1)
        label_CG_Limit=Label(my_window,text="Forward 100.46 InAfDatum After 125.6 InAfDatum")
        label_CG_Limit.grid(row=14,column=1)
        if CG <=100.46:
            label_CG_result=Label(my_window,text="CG out of limits !!!",bg="red")
            label_CG_result.grid(row=15,column=0)
        else:
            label_CG_result=Label(my_window,text="CG within limits, take off approved",bg="green")
            label_CG_result.grid(row=15,column=0)

    elif float (vzletova_hmotnost) <=5639:
        label_16=Label(my_window,text="MTOW within limits, take off approved",bg="green")
        label_16.grid(row=15,column=1)
        label_CG_Limit=Label(my_window,text="Forward 103.18 InAfDatum After 125.6 InAfDatum")
        label_CG_Limit.grid(row=14,column=1)
        if CG <=103.18:
            label_CG_result=Label(my_window,text="CG out of limits !!!",bg="red")
            label_CG_result.grid(row=15,column=0)
        else:
            label_CG_result=Label(my_window,text="CG within limits, take off approved",bg="green")
            label_CG_result.grid(row=15,column=0)

    else:
        label_16=Label(my_window,text="MTOW within limits, take off approved",bg="green")
        label_16.grid(row=15,column=1)
        label_CG_Limit=Label(my_window,text="Forward 111.55 InAfDatum After 125.6 InAfDatum")
        label_CG_Limit.grid(row=14,column=1)
        if CG <=111.55:
            label_CG_result=Label(my_window,text="CG out of limits !!!",bg="red")
            label_CG_result.grid(row=15,column=0)
        else:
            label_CG_result=Label(my_window,text="CG within limits, take off approved",bg="green")
            label_CG_result.grid(row=15,column=0)




#Blok promenych pro STRING do GRID LABELU
    string_to_display = vaha_skokanu, "Pounds"
    string_to_display_2 = str (round(vaha_paliva_predni_zadni_pounds, 1)), "Pounds"
    string_to_display_3 = str (round(vaha_pilota_pounds, 1)), "Pounds"
    string_to_display_4 = str (round(vzletova_hmotnost, 1)), "Pounds"
    string_to_display_moment1= str (round(moment_pilot, 1)), "lb.in"
    string_to_display_moment2= str (round(moment_palivo, 1)), "lb.in"
    string_to_display_moment21= str (round(moment_palivo_zadni, 1)), "lb.in"
    string_to_display_moment3= str (round(moment_letoun, 1)), "lb.in"
    string_to_display_moment4= str (round(moment_skokan1, 1)), "lb.in"
    string_to_display_moment5= str (round(moment_skokan2, 1)), "lb.in"
    string_to_display_moment6= str (round(moment_skokan3, 1)), "lb.in"
    string_to_display_moment7= str (round(moment_skokan4, 1)), "lb.in"
    string_to_display_moment8= str (round(moment_skokan5, 1)), "lb.in"
    string_to_display_moment9= str (round(moment_skokan6, 1)), "lb.in"
    string_to_display_moment10= str (round(moment_skokan7, 1)), "lb.in"
    string_to_display_moment11= str (round(moment_skokan8, 1)), "lb.in"
    string_to_display_moment12= str (round(moment_skokan9, 1)), "lb.in"
    string_to_display_moment13= str (round(moment_skokan10, 1)), "lb.in"
    string_to_display_moment14= str (round(moment_skokan11, 1)), "lb.in"
    string_to_display_moment15= str (round(moment_skokan12, 1)), "lb.in"
    string_to_display_moment16= str (round(moment_skokan13, 1)), "lb.in"
    string_to_display_moment17= str (round(moment_skokan14, 1)), "lb.in"
    string_to_display_moment18= str (round(moment_skokan15, 1)), "lb.in"
    string_to_display_moment19= str (round(moment_skokan16, 1)), "lb.in"
    string_to_display_moment20 = str (round(moment_skokan17, 1)), "lb.in"
#Konce bloku promenych Sring do GRID LABELU


    label_5=Label (my_window)
    label_5["text"]=string_to_display
    label_5.grid(row=4,column=1)
    #return label_5
    label_7=Label (my_window)
    label_7["text"]=string_to_display_2
    label_7.grid(row=5,column=1)
    label_12=Label (my_window)
    label_12["text"]=string_to_display_3
    label_12.grid(row=8,column=1)
    label_14=Label (my_window)
    label_14["text"]=string_to_display_4
    label_14.grid(row=9,column=1)

    button_2=Button(my_window,text="Vymazat formular",command=clear_form)
    button_2.grid(row=16,column=0)




def clear_form():

    os.execl(sys.executable, sys.executable, *sys.argv)




my_window=Tk ()
my_window.title("OK-SKW Weight & balance "       "                        Copyright © 2019 Jan Bracha Skysurf s.r.o          distributed as The GNU General Public License")
my_window.iconbitmap("airplane.ico")

positionRight = int(0)
positionDown = int(0)
my_window.geometry("+{}+{}".format(positionRight, positionDown))



photo = PhotoImage(file = "pac750PNG.png")
label_fotka=Label(my_window, image = photo)
label_fotka.grid(row=21,column=1)





label_1=Label(my_window,text="Pilot Name:")
label_10=Label(my_window,text="Pilot weight Kg")
label_11=Label(my_window,text="Pilot weight  is")
label_2=Label(my_window,text="Number of skydivers:")
Label_3=Label(my_window,text="Fuel quantity / Liters Jet A1 front tank is")
Label_4=Label(my_window,text="Complete skydivers weight")
Label_6=Label(my_window,text="Complete fuel weight")
Label_8=Label(my_window,text="Basic empty plane weight")
Label_9=Label(my_window,text="3506 Pounds")
label_13=Label(my_window,text="Take off weight")
label_celkovy_moment=Label(my_window,text="Complete moment is ")
label_celkovy_moment.grid(row=10,column=0)
label_povolena_CG=Label(my_window,text="Approved CG for current paylod is ")
label_povolena_CG.grid(row=14,column=0)
label_celkovy_CG=Label(my_window,text="Airplane CG is")
label_celkovy_CG.grid(row=7,column=0)
label_zadni_nadrz=Label(my_window,text="Fuel quantity / Liters Jet A1 rear tank")
label_zadni_nadrz.grid(row=0,column=2)
label_smer_drahy=Label(my_window,text="Runway direction magnetic")
label_smer_drahy.grid(row=1,column=2)
label_smer_vetru=Label(my_window,text="Wind direction")
label_smer_vetru.grid(row=2,column=2)
label_sila_vetru=Label(my_window,text="Wind velocity kts")
label_sila_vetru.grid(row=3,column=2)
label_current_time=Label(my_window,text="Current date & time ")
label_current_time.grid(row=4,column=2)
#label_venkovni_teplota=Label(my_window,text="Venkovni Teplota")
#label_venkovni_teplota.grid(row=4,column=2)
#label_faktorizace=Label(my_window,text="faktorizace %")
#label_faktorizace.grid(row=5,column=2)
#label_TODA=Label(my_window,text="Take off distance available ")
#label_TODA.grid(row=6,column=2)
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
#pokus
entry_1=Entry(my_window)
entry_1.insert(END, "Vladimir Vopat")
entry_2=Entry(my_window)
entry_2.insert(END, "15")
entry_3=Entry(my_window)
entry_3.insert(END, "170")
entry_4=Entry(my_window)
entry_4.insert(END, "90")
entry_zadni_nadrz=Entry(my_window)
entry_zadni_nadrz.insert(END, "0")
entry_zadni_nadrz.grid(row=0,column=3)
entry_smer_drahy=Entry(my_window)
entry_smer_drahy.insert(END, "200")
entry_smer_drahy.grid(row=1,column=3)
entry_smer_vetru_vzlet=Entry(my_window)
entry_smer_vetru_vzlet.insert(END, "20")
entry_smer_vetru_vzlet.grid(row=2,column=3)
entry_current_time=Entry(my_window)
entry_current_time.insert(END, current_timestamt)
entry_current_time.grid(row=4,column=3)
#entry_venkovni_teplota=Entry(my_window)
#entry_venkovni_teplota.insert(END, "20")
entry_sila_vetru=Entry(my_window)
entry_sila_vetru.grid(row=3,column=3)
entry_sila_vetru.insert(END, "0")
#entry_venkovni_teplota.grid(row=4,column=3)
#entry_faktorizace=Entry(my_window)
#entry_faktorizace.insert(END, "0")
#entry_faktorizace.grid(row=5,column=3)
#entry_TODA=Entry(my_window)
#entry_TODA.insert(END, "3707")
#entry_TODA.grid(row=6,column=3)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)
entry_3.grid(row=2,column=1)
entry_4.grid(row=3,column=1)
button_1=Button(my_window,text="Compute W&B",command=weight_balance)
button_1.grid(row=16,column=1)
#button_2=Button(my_window,text="Vymazat formular",command=clear_form)
#button_2.grid(row=16,column=0)



my_window.mainloop ()
