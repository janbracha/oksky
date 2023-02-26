from tkinter import *
from tkinter import filedialog
import math
import os
import time
import webbrowser as wb
import sys
import pyautogui
import PIL
import pygetwindow
from PIL import Image
from win32gui import FindWindow, GetWindowRect

#zadani aktualniho casu
secondsSinceEpoch = time.time()
timeObj = time.localtime(secondsSinceEpoch)
current_timestamt=('%d-%d-%d-%d-%d-%d' % (timeObj.tm_mday, timeObj.tm_mon, timeObj.tm_year, timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))
#konec zadani aktualniho casu

def weather():
    weather_okno= Toplevel()
    weather_okno.title("Weather widget")
    weather_okno.iconbitmap("airplane.ico")
    weather_okno.geometry("+{}+{}".format(300, 100))
    weather_okno.geometry("400x150")
    def chmi():
        wb.open_new("http://www.chmi.cz")
    def meteogram():
        wb.open_new("http://portal.chmi.cz/files/portal/docs/meteo/ov/aladin/results/public/meteogramy/meteogram_page_portal/m.html#Most%20(LKMO)")
    def aladin():
        wb.open_new("http://portal.chmi.cz/files/portal/docs/meteo/ov/aladin/results/ala.html#T2m,prec,v10mmslp,nebul,nebuldet,RH2m,veind,Tmxmn,prec24?")
    def radar():
        wb.open_new("http://portal.chmi.cz/files/portal/docs/meteo/rad/data_jsradview.html")
    def synoptic():
        wb.open_new("http://portal.chmi.cz/aktualni-situace/aktualni-stav-pocasi/evropa/synopticka-situace")
    def gamet():
        wb.open_new("http://portal.chmi.cz/predpovedi/predpovedi-pocasi/letecke/gamet")
    def sigmet():
        wb.open_new("http://portal.chmi.cz/predpovedi/predpovedi-pocasi/letecke/sigmet")
    def windguru():
        wb.open_new("https://www.windguru.cz/343183")
    def sunset():
        wb.open_new("https://www.meteogram.cz/vychod-zapad-slunce/ceska-republika/most/")


    button_weather1=Button(weather_okno,text="CHMI portal", command=chmi, bg="SkyBlue4")
    button_weather1.grid(row=0,column=0)
    button_weather2=Button(weather_okno,text="Meteogram LKMO", command=meteogram, bg="SkyBlue4")
    button_weather2.grid(row=0,column=1)
    button_weather3=Button(weather_okno,text="Aladin", command=aladin, bg="SkyBlue4")
    button_weather3.grid(row=0,column=2)
    button_weather4=Button(weather_okno,text="Radar Maps", command=radar, bg="SkyBlue4")
    button_weather4.grid(row=2,column=0)
    button_weather5=Button(weather_okno,text="Synoptic Maps", command=synoptic, bg="SkyBlue4")
    button_weather5.grid(row=1,column=0)
    button_weather6=Button(weather_okno,text="Gamet", command=gamet, bg="SkyBlue4")
    button_weather6.grid(row=1,column=1)
    button_weather7=Button(weather_okno,text="Sigmet", command=sigmet, bg="SkyBlue4")
    button_weather7.grid(row=1,column=2)
    button_weather8=Button(weather_okno,text="Windguru LKMO", command=windguru, bg="SkyBlue4")
    button_weather8.grid(row=2,column=1)
    button_weather9=Button(weather_okno,text="Sunset LKMO", command=sunset, bg="SkyBlue4")
    button_weather9.grid(row=2,column=2)
    label_close_weather=Label(weather_okno,text="                                           ")
    label_close_weather.grid(row=20,column=0)
    button_close_weather=Button(weather_okno,text="Close Weather ", command=weather_okno.destroy, bg="SkyBlue4")
    button_close_weather.grid(row=21,column=0)
def pdf():
    treti_okno= Toplevel()
    treti_okno.title("Manuals section ")
    treti_okno.iconbitmap("airplane.ico")
    #treti_okno.positionRight = int(550)
    #treti_okno.positionDown = int(100)
    treti_okno.geometry("+{}+{}".format(100, 100))
    #positionRight = int(550)
    #positionDown = int(100)
    #treti_okno.geometry("265x300")

    def section1():
        wb.open_new(r'section1.pdf')
    def section2():
        wb.open_new(r'section2.pdf')
    def section3():
        wb.open_new(r'section3.pdf')
    def section4():
        wb.open_new(r'section4.pdf')
    def section5():
        wb.open_new(r'section5.pdf')
    def section6():
        wb.open_new(r'section6.pdf')
    def section7():
        wb.open_new(r'section7.pdf')
    def section8():
        wb.open_new(r'section8.pdf')
    def section9():
        wb.open_new(r'section9.pdf')
    button_section1=Button(treti_okno,text="           Section 1 General          ", command=section1, bg="SkyBlue4")
    button_section1.grid(row=0,column=0)
    button_section2=Button(treti_okno,text="         Section 2 Limitations      ", command=section2, bg="SkyBlue4")
    button_section2.grid(row=1,column=0)
    button_section3=Button(treti_okno,text="       Section 3 Emergencies      ", command=section3, bg="SkyBlue4")
    button_section3.grid(row=2,column=0)
    button_section4=Button(treti_okno,text="Section 4 Normal procedures ", command=section4, bg="SkyBlue4")
    button_section4.grid(row=3,column=0)
    button_section5=Button(treti_okno,text="Section 5 Normal procedures ", command=section5, bg="SkyBlue4")
    button_section5.grid(row=4,column=0)
    button_section6=Button(treti_okno,text="  Section 6 Weight & Balance ", command=section6, bg="SkyBlue4")
    button_section6.grid(row=5,column=0)
    button_section7=Button(treti_okno,text="           Section 7 Airplane         ", command=section7, bg="SkyBlue4")
    button_section7.grid(row=6,column=0)
    button_section8=Button(treti_okno,text="   Section 8 Airplane handling", command=section8, bg="SkyBlue4")
    button_section8.grid(row=7,column=0)
    button_section9=Button(treti_okno,text="Section 9 Supplements EASA ", command=section9, bg="SkyBlue4")
    button_section9.grid(row=8,column=0)
    label_blank1=Label(treti_okno,text="")
    label_blank1.grid(row=9,column=0)
    button_close_manuals=Button(treti_okno,text="Close Manuals", command=treti_okno.destroy, bg="SkyBlue4")
    button_close_manuals.grid(row=20,column=0)
def compute():

    pilot_1_weight_kg=E_r1_c0.get()
    pilot_2_weight_kg=E_r0_c6.get()
    pilot_1_weight_pounds = float(pilot_1_weight_kg) * 2.2
    pilot_2_weight_pounds = float(pilot_2_weight_kg) * 2.2
    cargo_1_weight_ponds=float(E_r6_c0.get())
    cargo_2_weight_ponds=float(E_r6_c2.get())
    cargo_3_weight_ponds=float(E_r6_c4.get())
    cargo_4_weight_ponds=float(E_r6_c6.get())
    cargo_5_weight_ponds=float(E_r7_c0.get())
    cargo_6_weight_ponds=float(E_r7_c2.get())
    cargo_7_weight_ponds=float(E_r7_c4.get())
    cargo_8_weight_ponds=float(E_r7_c6.get())
    cargo_9_weight_ponds=float(E_r8_c0.get())
    cargo_10_weight_ponds=float(E_r8_c2.get())
    cargo_11_weight_ponds=float(E_r8_c4.get())
    cargo_12_weight_ponds=float(E_r8_c6.get())
    cargo_13_weight_ponds=float(E_r9_c0.get())
    cargo_14_weight_ponds=float(E_r9_c2.get())
    cargo_15_weight_ponds=float(E_r9_c4.get())
    cargo_16_weight_ponds=float(E_r9_c6.get())
    fuel_quantity_front_liters=float(E_r2_c0.get())
    fuel_quantity_rear_liters=float(E_r3_c0.get())
    fuel_front_tank_weight_pounds=fuel_quantity_front_liters * 0.78 * 2.2
    fuel_rear_tank_weight_pounds=fuel_quantity_rear_liters * 0.78 * 2.2
    basic_empty_weight=float(E_r0_c2.get())
    approved_mtow=float(E_r1_c2.get())
    pilot_1_arm=float(E_r2_c6.get())
    pilot_2_arm=float(E_r3_c4.get())
    empty_plane_arm=float(E_r2_c4.get())
    fuel_front_tank_arm=float(E_r3_c6.get())
    fuel_rear_tank_arm=float(E_r4_c4.get())
    cargo_1_arm=float(E_r10_c0.get())
    cargo_2_arm=float(E_r10_c2.get())
    cargo_3_arm=float(E_r10_c4.get())
    cargo_4_arm=float(E_r10_c6.get())
    cargo_5_arm=float(E_r11_c0.get())
    cargo_6_arm=float(E_r11_c2.get())
    cargo_7_arm=float(E_r11_c4.get())
    cargo_8_arm=float(E_r11_c6.get())
    cargo_9_arm=float(E_r12_c0.get())
    cargo_10_arm=float(E_r12_c2.get())
    cargo_11_arm=float(E_r12_c4.get())
    cargo_12_arm=float(E_r12_c6.get())
    cargo_13_arm=float(E_r13_c0.get())
    cargo_14_arm=float(E_r13_c2.get())
    cargo_15_arm=float(E_r13_c4.get())
    cargo_16_arm=float(E_r13_c6.get())
    wind_derection=float(E_r3_c2.get())
    wind_velocity=float(E_r4_c0.get())
    runway_magnetic_direction=float(E_r2_c2.get())

    moment_pilot_1 = pilot_1_arm * pilot_1_weight_pounds
    moment_pilot_2 = pilot_2_arm * pilot_2_weight_pounds
    moment_fuel_front_tanks = fuel_front_tank_arm * fuel_front_tank_weight_pounds
    moment_fuel_rear_tanks = fuel_rear_tank_arm * fuel_rear_tank_weight_pounds
    moment_empty_plane = empty_plane_arm * basic_empty_weight
    moment_cargo_ponit_1 = cargo_1_arm * cargo_1_weight_ponds
    moment_cargo_ponit_2 = cargo_2_arm * cargo_2_weight_ponds
    moment_cargo_ponit_3 = cargo_3_arm * cargo_3_weight_ponds
    moment_cargo_ponit_4 = cargo_4_arm * cargo_4_weight_ponds
    moment_cargo_ponit_5 = cargo_5_arm * cargo_5_weight_ponds
    moment_cargo_ponit_6 = cargo_6_arm * cargo_6_weight_ponds
    moment_cargo_ponit_7 = cargo_7_arm * cargo_7_weight_ponds
    moment_cargo_ponit_8 = cargo_8_arm * cargo_8_weight_ponds
    moment_cargo_ponit_9 = cargo_9_arm * cargo_9_weight_ponds
    moment_cargo_ponit_10 = cargo_10_arm * cargo_10_weight_ponds
    moment_cargo_ponit_11 = cargo_11_arm * cargo_11_weight_ponds
    moment_cargo_ponit_12 = cargo_12_arm * cargo_12_weight_ponds
    moment_cargo_ponit_13 = cargo_13_arm * cargo_13_weight_ponds
    moment_cargo_ponit_14 = cargo_14_arm * cargo_14_weight_ponds
    moment_cargo_ponit_15 = cargo_15_arm * cargo_15_weight_ponds
    moment_cargo_ponit_16 = cargo_16_arm * cargo_16_weight_ponds
    total_moment = moment_pilot_1 + moment_pilot_2 + moment_fuel_rear_tanks + moment_fuel_front_tanks +moment_empty_plane + moment_cargo_ponit_1 + moment_cargo_ponit_2 + moment_cargo_ponit_3 + moment_cargo_ponit_4 + moment_cargo_ponit_5 + moment_cargo_ponit_6 + moment_cargo_ponit_7 + moment_cargo_ponit_8 + moment_cargo_ponit_9 + moment_cargo_ponit_10 + moment_cargo_ponit_11 + moment_cargo_ponit_12 + moment_cargo_ponit_13 + moment_cargo_ponit_14 + moment_cargo_ponit_15 + moment_cargo_ponit_16
    total_tow = pilot_1_weight_pounds + pilot_2_weight_pounds + fuel_front_tank_weight_pounds + fuel_rear_tank_weight_pounds + basic_empty_weight + cargo_1_weight_ponds + cargo_2_weight_ponds + cargo_3_weight_ponds + cargo_4_weight_ponds + cargo_5_weight_ponds + cargo_6_weight_ponds + cargo_7_weight_ponds + cargo_8_weight_ponds + cargo_9_weight_ponds + cargo_10_weight_ponds + cargo_11_weight_ponds + cargo_12_weight_ponds + cargo_13_weight_ponds + cargo_14_weight_ponds + cargo_15_weight_ponds +cargo_16_weight_ponds
    total_CG =total_moment / total_tow
    approved_mtow1= approved_mtow+1

    if total_tow >= approved_mtow1:
        label_warning=Label(hlavni_okno,text="MTOW over limits", bg="orange red")
        label_warning.grid(row=25,column=1)
        label_warning1=Label(hlavni_okno,text="Unable determinate CG limits", bg="orange red")
        label_warning1.grid(row=25,column=2)
    elif total_tow <= 4209:
        label_warning=Label(hlavni_okno,text="MTOW within limits", bg="lime green")
        label_warning.grid(row=25,column=1)
        label_approved1=Label(hlavni_okno,text="Approved CG for this payload")
        label_approved1.grid(row=22,column=6)
        label_approved2=Label(hlavni_okno,text="100.46 front - 125.6 after")
        label_approved2.grid(row=22,column=7)
        front=100.46
        after=125.6
        if front <= total_CG <=after:
            label_CG_warning=Label(hlavni_okno,text="CG within limits", bg="lime green")
            label_CG_warning.grid(row=25,column=2)
        else:
            label_CG_warning=Label(hlavni_okno,text="CG OUT of limits", bg="orange red")
            label_CG_warning.grid(row=25,column=2)
    elif total_tow <= 5639:
        label_warning=Label(hlavni_okno,text="MTOW within limits", bg="lime green")
        label_warning.grid(row=25,column=1)
        label_approved1=Label(hlavni_okno,text="Approved CG for this payload")
        label_approved1.grid(row=22,column=6)
        label_approved2=Label(hlavni_okno,text="103.18 front - 125.6 after")
        label_approved2.grid(row=22,column=7)
        front=103.18
        after=125.6
        if front <= total_CG <=after:
            label_CG_warning=Label(hlavni_okno,text="CG within limits", bg="lime green")
            label_CG_warning.grid(row=25,column=2)
        else:
            label_CG_warning=Label(hlavni_okno,text="CG OUT of limits", bg="orange red")
            label_CG_warning.grid(row=25,column=2)
    else:
        label_warning=Label(hlavni_okno,text="MTOW within limits", bg="lime green")
        label_warning.grid(row=25,column=1)
        label_approved1=Label(hlavni_okno,text="Approved CG for this payload")
        label_approved1.grid(row=22,column=6)
        label_approved2=Label(hlavni_okno,text="111.55 front - 125.6 after")
        label_approved2.grid(row=22,column=7)
        front=111.55
        after=125.6
        if front <= total_CG <=after:
            label_CG_warning=Label(hlavni_okno,text="CG within limits", bg="lime green")
            label_CG_warning.grid(row=25,column=2)
        else:
            label_CG_warning=Label(hlavni_okno,text="CG OUT of limits", bg="orange red")
            label_CG_warning.grid(row=25,column=2)

####preasure altitude section
    elevation_entry= E_r1_c6.get()
    elevation= int(elevation_entry)
    qnh= float(E_r1_c4.get())
    ofset=1013 - qnh
    preasure_alt=elevation + ( 30 * ofset)

    label_preasure_alt=Label(hlavni_okno,text="Preasure altitude is")
    label_preasure_alt.grid(row=23,column=0)
    string_preasure_alt= str (round (preasure_alt, 2)), "feets"
    label_string_preasure_alt=Label(hlavni_okno)
    label_string_preasure_alt["text"]=string_preasure_alt
    label_string_preasure_alt.grid(row=23,column=1)
##### end of preasure altitude section
    def closest_3(pres_alt_range, OAT):
        return pres_alt_range[min(range(len(pres_alt_range)), key = lambda i: abs(pres_alt_range[i]-preasure_alt))]
    pres_alt_range = [0, 2000, 4000, 6000, 8000, 10000]
    closest_preasure_alt= (closest_3(pres_alt_range, preasure_alt))
    print (closest_preasure_alt)

#closest selection section
    def closest_2(payload_range, total_tow):
            return payload_range[min(range(len(payload_range)), key = lambda i: abs (payload_range[i]-total_tow))]
    payload_range = [7500, 6500, 5500, 4500]
    closest_payload= (closest_2(payload_range, total_tow))
    if closest_payload == 7500:
        payload_cursor=0
    elif closest_payload == 6500:
        payload_cursor=1
    elif closest_payload == 5500:
        payload_cursor=2
    else:
        closest_payload == 4500
        payload_cursor=3

    OAT_entry = E_r4_c2.get()
    OAT = int(OAT_entry)
    def closest_1(temp_range, OAT):
        return temp_range[min(range(len(temp_range)), key = lambda i: abs(temp_range[i]-OAT))]
    temp_range = [5, 15, 25, 35, 45]
    closest_temperature= (closest_1(temp_range, OAT))
    if closest_temperature == 5:
        temperature_cursor=0
    elif closest_temperature == 15:
        temperature_cursor=1
    elif closest_temperature == 25:
        temperature_cursor=2
    elif closest_temperature == 35:
        temperature_cursor=3
    else:
        closest_temperature == 4500
        temperature_cursor=4

    list_1 = [[1606, 1695, 1785, 1956, 2208],
            [1341, 1414, 1487, 1626, 1822],
            [1028, 1083, 1140, 1242, 1384],
            [769, 810, 852, 926, 1028]]

    list_2 = [[1752, 1854, 1974, 2205, 2495],
              [1461, 1545, 1644, 1826, 2048],
              [1119, 1183, 1259, 1391, 1550],
              [837, 884, 940, 1035, 1148]]

    list_3 = [[1922, 2036, 2237, 2507, 2844],
              [1600, 1694, 1856, 2064, 2317],
              [1224, 1296, 1416, 1566, 1746],
              [915, 968, 1072, 1162, 1288]]

    list_4 = [[2111, 2294, 2559, 2882, 3293],
              [1754, 1903, 2111, 2351, 2653],
              [1341, 1452, 1604, 1778, 1985],
              [1012, 1083, 1191, 1314, 1458]]

    list_5 = [[2481, 2751, 3085, 3497, 4055],
              [2056, 2268, 2523, 2825, 3209],
              [1567, 1723, 1877, 2119, 2374],
              [1188, 1279, 1410, 1558, 1757]]

    list_6 = [[2977, 3325, 3753, 4310, 5096],
              [2450, 2629, 2920, 3268, 3693],
              [1859, 2051, 2274, 2538, 2858],
              [1379, 1515, 1673, 1854, 2069]]



    if closest_preasure_alt == 0:
        list = list_1
    elif closest_preasure_alt == 2000:
        list = list_2
    elif closest_preasure_alt == 4000:
        list = list_3
    elif closest_preasure_alt == 6000:
        list = list_4
    elif closest_preasure_alt == 8000:
        list = list_5
    else:
        list = list_6

    take_off_distance = (list [(payload_cursor)][(temperature_cursor)])
    label_required_runway_result=Label(hlavni_okno)
    take_off_distance_label_var = str (round(take_off_distance, 1)), "feets"
    label_required_runway=Label(hlavni_okno,text="Required runway lenght is")
    label_required_runway.grid(row=23,column=2)
    label_required_runway_result["text"]=take_off_distance_label_var
    label_required_runway_result.grid(row=23,column=3)
    TODA_entry = E_r5_c2.get()
    TODA = int(TODA_entry)

    if TODA <= take_off_distance:
        label_TODA_warning=Label(hlavni_okno,text="TODA is too short",bg="orange red")
        label_TODA_warning.grid(row=25,column=3)
    else:
        label_TODA_warning=Label(hlavni_okno,text="TODA within limits",bg="lime green")
        label_TODA_warning.grid(row=25,column=3)




#end of closet selection


#crosswind calculation

    crosswind_drift = wind_derection - runway_magnetic_direction
    crosswind_current = math.sin(crosswind_drift) * wind_velocity

    label_result_r22_c4=Label(hlavni_okno,text="Current crosswind is:")
    label_result_r22_c4.grid(row=22,column=4)
    str_crosswind = str (round(crosswind_current, 1)), "kts"
    label_result_r22_c5=Label(hlavni_okno)
    label_result_r22_c5["text"]=str_crosswind
    label_result_r22_c5.grid(row=22,column=5)



    if crosswind_current <=14:
        label_result_r25_c0=Label(hlavni_okno,text="Crosswind within limits",bg="lime green")
        label_result_r25_c0.grid(row=25,column=0)
    else:
        label_result_r25_c0=Label(hlavni_okno,text="Crosswind out of limits",bg="orange red")
        label_result_r25_c0.grid(row=25,column=0)

#end of crosswind calculation




    label_result_r22_c0=Label(hlavni_okno,text="Total CG is:")
    label_result_r22_c0.grid(row=22,column=0)
    str_total_CG= str (round(total_CG, 1)), "InAfDatum"
    label_result_r22_c1=Label(hlavni_okno)
    label_result_r22_c1["text"]=str_total_CG
    label_result_r22_c1.grid(row=22,column=1)

    label_result_r22_c2=Label(hlavni_okno,text="Take off weight is:")
    label_result_r22_c2.grid(row=22,column=2)
    str_total_tow= str (round(total_tow, 1)), "Pounds"
    label_result_r22_c3=Label(hlavni_okno)
    label_result_r22_c3["text"]=str_total_tow
    label_result_r22_c3.grid(row=22,column=3)





    label_result_r15_c0=Label(hlavni_okno,text="Pilot 1 moment is:")
    label_result_r15_c0.grid(row=15,column=0)
    str_pilot_1_mnt= str (round(moment_pilot_1, 1)), "in.lbs"
    label_result_r15_c1=Label(hlavni_okno)
    label_result_r15_c1["text"]=str_pilot_1_mnt
    label_result_r15_c1.grid(row=15,column=1)

    label_result_r15_c2=Label(hlavni_okno,text="Pilot 2 moment is:")
    label_result_r15_c2.grid(row=15,column=2)
    str_pilot_2_mnt= str (round(moment_pilot_2, 1)), "in.lbs"
    label_result_r15_c3=Label(hlavni_okno)
    label_result_r15_c3["text"]=str_pilot_2_mnt
    label_result_r15_c3.grid(row=15,column=3)

    label_result_r15_c4=Label(hlavni_okno,text="Fuel front tank moment is:")
    label_result_r15_c4.grid(row=15,column=4)
    str_fuel_front= str (round(moment_fuel_front_tanks, 1)), "in.lbs"
    label_result_r15_c5=Label(hlavni_okno)
    label_result_r15_c5["text"]=str_fuel_front
    label_result_r15_c5.grid(row=15,column=5)

    label_result_r15_c6=Label(hlavni_okno,text="Fuel rear tank moment is:")
    label_result_r15_c6.grid(row=15,column=6)
    str_fuel_rear= str (round(moment_fuel_rear_tanks, 1)), "in.lbs"
    label_result_r15_c7=Label(hlavni_okno)
    label_result_r15_c7["text"]=str_fuel_rear
    label_result_r15_c7.grid(row=15,column=7)

    label_result_r16_c0=Label(hlavni_okno,text="Empty plane moment is:")
    label_result_r16_c0.grid(row=16,column=0)
    str_empty_plane= str (round(moment_empty_plane, 1)), "in.lbs"
    label_result_r16_c1=Label(hlavni_okno)
    label_result_r16_c1["text"]=str_empty_plane
    label_result_r16_c1.grid(row=16,column=1)

    label_result_r16_c2=Label(hlavni_okno,text="Cargo point 1 moment is:")
    label_result_r16_c2.grid(row=16,column=2)
    str_cargo_1= str (round(moment_cargo_ponit_1, 1)), "in.lbs"
    label_result_r16_c3=Label(hlavni_okno)
    label_result_r16_c3["text"]=str_cargo_1
    label_result_r16_c3.grid(row=16,column=3)

    label_result_r16_c4=Label(hlavni_okno,text="Cargo point 2 moment is:")
    label_result_r16_c4.grid(row=16,column=4)
    str_cargo_2= str (round(moment_cargo_ponit_2, 1)), "in.lbs"
    label_result_r16_c5=Label(hlavni_okno)
    label_result_r16_c5["text"]=str_cargo_2
    label_result_r16_c5.grid(row=16,column=5)

    label_result_r16_c6=Label(hlavni_okno,text="Cargo point 3 moment is:")
    label_result_r16_c6.grid(row=16,column=6)
    str_cargo_3= str (round(moment_cargo_ponit_3, 1)), "in.lbs"
    label_result_r16_c7=Label(hlavni_okno)
    label_result_r16_c7["text"]=str_cargo_3
    label_result_r16_c7.grid(row=16,column=7)

    label_result_r17_c0=Label(hlavni_okno,text="Cargo point 4 moment is:")
    label_result_r17_c0.grid(row=17,column=0)
    str_cargo_4= str (round(moment_cargo_ponit_4, 1)), "in.lbs"
    label_result_r17_c1=Label(hlavni_okno)
    label_result_r17_c1["text"]=str_cargo_4
    label_result_r17_c1.grid(row=17,column=1)

    label_result_r17_c2=Label(hlavni_okno,text="Cargo point 5 moment is:")
    label_result_r17_c2.grid(row=17,column=2)
    str_cargo_5= str (round(moment_cargo_ponit_5, 1)), "in.lbs"
    label_result_r17_c3=Label(hlavni_okno)
    label_result_r17_c3["text"]=str_cargo_5
    label_result_r17_c3.grid(row=17,column=3)

    label_result_r17_c4=Label(hlavni_okno,text="Cargo point 6 moment is:")
    label_result_r17_c4.grid(row=17,column=4)
    str_cargo_6= str (round(moment_cargo_ponit_6, 1)), "in.lbs"
    label_result_r17_c5=Label(hlavni_okno)
    label_result_r17_c5["text"]=str_cargo_6
    label_result_r17_c5.grid(row=17,column=5)

    label_result_r17_c6=Label(hlavni_okno,text="Cargo point 7 moment is:")
    label_result_r17_c6.grid(row=17,column=6)
    str_cargo_7= str (round(moment_cargo_ponit_7, 1)), "in.lbs"
    label_result_r17_c7=Label(hlavni_okno)
    label_result_r17_c7["text"]=str_cargo_7
    label_result_r17_c7.grid(row=17,column=7)

    label_result_r18_c0=Label(hlavni_okno,text="Cargo point 8 moment is:")
    label_result_r18_c0.grid(row=18,column=0)
    str_cargo_8= str (round(moment_cargo_ponit_8, 1)), "in.lbs"
    label_result_r18_c1=Label(hlavni_okno)
    label_result_r18_c1["text"]=str_cargo_8
    label_result_r18_c1.grid(row=18,column=1)

    label_result_r18_c2=Label(hlavni_okno,text="Cargo point 9 moment is:")
    label_result_r18_c2.grid(row=18,column=2)
    str_cargo_9= str (round(moment_cargo_ponit_9, 1)), "in.lbs"
    label_result_r18_c3=Label(hlavni_okno)
    label_result_r18_c3["text"]=str_cargo_9
    label_result_r18_c3.grid(row=18,column=3)

    label_result_r18_c4=Label(hlavni_okno,text="Cargo point 10 moment is:")
    label_result_r18_c4.grid(row=18,column=4)
    str_cargo_10= str (round(moment_cargo_ponit_10, 1)), "in.lbs"
    label_result_r18_c5=Label(hlavni_okno)
    label_result_r18_c5["text"]=str_cargo_10
    label_result_r18_c5.grid(row=18,column=5)

    label_result_r18_c6=Label(hlavni_okno,text="Cargo point 11 moment is:")
    label_result_r18_c6.grid(row=18,column=6)
    str_cargo_11= str (round(moment_cargo_ponit_11, 1)), "in.lbs"
    label_result_r18_c7=Label(hlavni_okno)
    label_result_r18_c7["text"]=str_cargo_11
    label_result_r18_c7.grid(row=18,column=7)

    label_result_r19_c0=Label(hlavni_okno,text="Cargo point 12 moment is:")
    label_result_r19_c0.grid(row=19,column=0)
    str_cargo_12= str (round(moment_cargo_ponit_12, 1)), "in.lbs"
    label_result_r19_c1=Label(hlavni_okno)
    label_result_r19_c1["text"]=str_cargo_12
    label_result_r19_c1.grid(row=19,column=1)

    label_result_r19_c2=Label(hlavni_okno,text="Cargo point 13 moment is:")
    label_result_r19_c2.grid(row=19,column=2)
    str_cargo_13= str (round(moment_cargo_ponit_13, 1)), "in.lbs"
    label_result_r19_c3=Label(hlavni_okno)
    label_result_r19_c3["text"]=str_cargo_13
    label_result_r19_c3.grid(row=19,column=3)

    label_result_r19_c4=Label(hlavni_okno,text="Cargo point 14 moment is:")
    label_result_r19_c4.grid(row=19,column=4)
    str_cargo_14= str (round(moment_cargo_ponit_14, 1)), "in.lbs"
    label_result_r19_c5=Label(hlavni_okno)
    label_result_r19_c5["text"]=str_cargo_14
    label_result_r19_c5.grid(row=19,column=5)

    label_result_r19_c6=Label(hlavni_okno,text="Cargo point 15 moment is:")
    label_result_r19_c6.grid(row=19,column=6)
    str_cargo_15= str (round(moment_cargo_ponit_15, 1)), "in.lbs"
    label_result_r19_c7=Label(hlavni_okno)
    label_result_r19_c7["text"]=str_cargo_15
    label_result_r19_c7.grid(row=19,column=7)

    label_result_r20_c0=Label(hlavni_okno,text="Cargo point 16 moment is:")
    label_result_r20_c0.grid(row=20,column=0)
    str_cargo_16= str (round(moment_cargo_ponit_16, 1)), "in.lbs"
    label_result_r20_c1=Label(hlavni_okno)
    label_result_r20_c1["text"]=str_cargo_16
    label_result_r20_c1.grid(row=20,column=1)

    label_result_r20_c2=Label(hlavni_okno,text="Total moment moment is:")
    label_result_r20_c2.grid(row=20,column=2)
    str_total_moment= str (round(total_moment, 1)), "in.lbs"
    label_result_r20_c3=Label(hlavni_okno)
    label_result_r20_c3["text"]=str_total_moment
    label_result_r20_c3.grid(row=20,column=3)

    label_separator_9=Label(hlavni_okno,text="")
    label_separator_9.grid(row=21,column=0)
    label_separator_10=Label(hlavni_okno,text="")
    label_separator_10.grid(row=21,column=1)
    label_separator_11=Label(hlavni_okno,text="")
    label_separator_11.grid(row=21,column=2)
    label_separator_12=Label(hlavni_okno,text="")
    label_separator_12.grid(row=21,column=3)
    label_separator_13=Label(hlavni_okno,text="")
    label_separator_13.grid(row=21,column=4)
    label_separator_14=Label(hlavni_okno,text="")
    label_separator_14.grid(row=21,column=5)
    label_separator_15=Label(hlavni_okno,text="")
    label_separator_15.grid(row=21,column=6)
    label_separator_16=Label(hlavni_okno,text="")
    label_separator_16.grid(row=21,column=7)
def unit_calculator():
    druhe_okno= Toplevel()
    druhe_okno.title("Unit convertor tool ")
    druhe_okno.iconbitmap("airplane.ico")
    #positionRight = int(300)
    #positionDown = int(100)
    druhe_okno.geometry("+{}+{}".format(730, 100))

    label_galons_liters=Label(druhe_okno,text="galons to liters")
    label_galons_liters.grid(row=0,column=0)
    galons_to_liters_entry=Entry(druhe_okno)
    galons_to_liters_entry.insert(END, "10")
    galons_to_liters_entry.grid(row=0,column=1)
    def galons():
        galons_entry=galons_to_liters_entry.get()
        galons_converted=int(galons_entry)*3.78
        result_display = str (round(galons_converted, 3))
        label_converted=Label(druhe_okno,)
        label_converted["text"]=result_display, "Liters"
        label_converted.grid(row=0,column=2)
    button_4=Button(druhe_okno,text="Convert", command=galons,bg="SkyBlue4")
    button_4.grid(row=0,column=3)

    label_liters_galons=Label(druhe_okno,text="liters to galons")
    label_liters_galons.grid(row=1,column=0)
    label_liters_galons_entry=Entry(druhe_okno)
    label_liters_galons_entry.insert(END, "10")
    label_liters_galons_entry.grid(row=1,column=1)
    def liters():
        liters_entry=label_liters_galons_entry.get()
        galons_converted=int(liters_entry)/3.78
        result_display1 = str (round(galons_converted, 3))
        label_converted_1=Label(druhe_okno,)
        label_converted_1["text"]=result_display1, "Galons"
        label_converted_1.grid(row=1,column=2)
    button_5=Button(druhe_okno,text="Convert", command=liters,bg="SkyBlue4")
    button_5.grid(row=1,column=3)

    label_meters_feets=Label(druhe_okno,text="meters to feets")
    label_meters_feets.grid(row=2,column=0)
    label_meters_entry=Entry(druhe_okno)
    label_meters_entry.insert(END, "10")
    label_meters_entry.grid(row=2,column=1)
    def meters():
        meters_entry=label_meters_entry.get()
        meters_converted=int(meters_entry)*3.28
        result_display2 = str (round(meters_converted, 3))
        label_converted_2=Label(druhe_okno,)
        label_converted_2["text"]=result_display2, "Feets"
        label_converted_2.grid(row=2,column=2)
    button_6=Button(druhe_okno,text="Convert", command=meters,bg="SkyBlue4")
    button_6.grid(row=2,column=3)
#######################
    label_feets_meters=Label(druhe_okno,text="feets to meters")
    label_feets_meters.grid(row=3,column=0)
    label_feets_meters_entry=Entry(druhe_okno)
    label_feets_meters_entry.insert(END, "10")
    label_feets_meters_entry.grid(row=3,column=1)
    def feets():
        feets_entry=label_feets_meters_entry.get()
        feets_converted=int(feets_entry)/3.28
        result_display3 = str (round(feets_converted, 3))
        label_converted_3=Label(druhe_okno,)
        label_converted_3["text"]=result_display3, "Meters"
        label_converted_3.grid(row=3,column=2)
    button_7=Button(druhe_okno,text="Convert", command=feets,bg="SkyBlue4")
    button_7.grid(row=3,column=3)


###########################

    label_kilo_pound=Label(druhe_okno,text="Kilograms to pounds")
    label_kilo_pound.grid(row=4,column=0)
    label_kilo_pound_entry=Entry(druhe_okno)
    label_kilo_pound_entry.insert(END, "10")
    label_kilo_pound_entry.grid(row=4,column=1)
    def kilo():
        kilos_entry=label_kilo_pound_entry.get()
        kilos_converted=int(kilos_entry)*2.2
        result_display4 = str (round(kilos_converted, 3))
        label_converted_4=Label(druhe_okno,)
        label_converted_4["text"]=result_display4, "Pounds"
        label_converted_4.grid(row=4,column=2)
    button_8=Button(druhe_okno,text="Convert", command=kilo,bg="SkyBlue4")
    button_8.grid(row=4,column=3)
########################
    label_pound_kilo=Label(druhe_okno,text="Pounds to kilograms")
    label_pound_kilo.grid(row=5,column=0)
    label_pound_kilo_entry=Entry(druhe_okno)
    label_pound_kilo_entry.insert(END, "10")
    label_pound_kilo_entry.grid(row=5,column=1)
    def pound():
        pounds_entry=label_pound_kilo_entry.get()
        pounds_converted=int(pounds_entry)/2.2
        result_display5 = str (round(pounds_converted, 3))
        label_converted_5=Label(druhe_okno,)
        label_converted_5["text"]=result_display5, "Kilograms"
        label_converted_5.grid(row=5,column=2)
    button_9=Button(druhe_okno,text="Convert", command=pound,bg="SkyBlue4")
    button_9.grid(row=5,column=3)

###########################

    label_mts_kts=Label(druhe_okno,text="meters/s to kts")
    label_mts_kts.grid(row=6,column=0)
    label_mts_kts_entry=Entry(druhe_okno)
    label_mts_kts_entry.insert(END, "10")
    label_mts_kts_entry.grid(row=6,column=1)
    def mtskts():
        mts_entry=label_mts_kts_entry.get()
        mtskts_converted=int(mts_entry)*1.94
        result_display6 = str (round(mtskts_converted, 3))
        label_converted_6=Label(druhe_okno,)
        label_converted_6["text"]=result_display6, "kts"
        label_converted_6.grid(row=6,column=2)
    button_10=Button(druhe_okno,text="Convert", command=mtskts,bg="SkyBlue4")
    button_10.grid(row=6,column=3)

###############
    label_kts_mts=Label(druhe_okno,text="kts to meters/s")
    label_kts_mts.grid(row=7,column=0)
    label_kts_mts_entry=Entry(druhe_okno)
    label_kts_mts_entry.insert(END, "10")
    label_kts_mts_entry.grid(row=7,column=1)
    def ktsmts():
        kts_entry=label_kts_mts_entry.get()
        ktsmts_converted=int(kts_entry)*0.51
        result_display7 = str (round(ktsmts_converted, 3))
        label_converted_7=Label(druhe_okno,)
        label_converted_7["text"]=result_display7, "meters/s"
        label_converted_7.grid(row=7,column=2)
    button_11=Button(druhe_okno,text="Convert", command=ktsmts,bg="SkyBlue4")
    button_11.grid(row=7,column=3)

##################
    label_litersJet_to_kilos=Label(druhe_okno,text="Liters JetA1 to kilos")
    label_litersJet_to_kilos.grid(row=8,column=0)
    label_litersJet_to_kilos_entry=Entry(druhe_okno)
    label_litersJet_to_kilos_entry.insert(END, "10")
    label_litersJet_to_kilos_entry.grid(row=8,column=1)
    def jettokilo():
        JetA1_liter_entry=label_litersJet_to_kilos_entry.get()
        JetA1_liter_converted=int(JetA1_liter_entry)*0.78
        result_display8 = str (round(JetA1_liter_converted, 3))
        label_converted_8=Label(druhe_okno,)
        label_converted_8["text"]=result_display8, "kilograms"
        label_converted_8.grid(row=8,column=2)
    button_12=Button(druhe_okno,text="Convert", command=jettokilo,bg="SkyBlue4")
    button_12.grid(row=8,column=3)

############

    label_litersJet_to_pounds=Label(druhe_okno,text="Liters JetA1 to pounds")
    label_litersJet_to_pounds.grid(row=9,column=0)
    label_litersJet_to_pounds_entry=Entry(druhe_okno)
    label_litersJet_to_pounds_entry.insert(END, "10")
    label_litersJet_to_pounds_entry.grid(row=9,column=1)
    def jettopound():
        JetA1_liter_entry1=label_litersJet_to_pounds_entry.get()
        JetA1_liter_converted1=int(JetA1_liter_entry1)*0.78*2.2
        result_display9 = str (round(JetA1_liter_converted1, 3))
        label_converted_9=Label(druhe_okno,)
        label_converted_9["text"]=result_display9, "pounds"
        label_converted_9.grid(row=9,column=2)
    button_13=Button(druhe_okno,text="Convert", command=jettopound,bg="SkyBlue4")
    button_13.grid(row=9,column=3)

############
    label_Kilo_to_nautical=Label(druhe_okno,text="Kilometers to Miles")
    label_Kilo_to_nautical.grid(row=10,column=0)
    label_Kilo_to_nautical_entry=Entry(druhe_okno)
    label_Kilo_to_nautical_entry.insert(END, "10")
    label_Kilo_to_nautical_entry.grid(row=10,column=1)
    def kmstomph():
        kmstomph_entry=label_Kilo_to_nautical_entry.get()
        kmstomph_converted=int(kmstomph_entry)/1.852
        result_display10 = str (round(kmstomph_converted, 3))
        label_converted_10=Label(druhe_okno,)
        label_converted_10["text"]=result_display10, "Miles"
        label_converted_10.grid(row=10,column=2)
    button_14=Button(druhe_okno,text="Convert", command=kmstomph,bg="SkyBlue4")
    button_14.grid(row=10,column=3)

###########################
    label_nautical_to_kilometers=Label(druhe_okno,text="Miles to Kilometers")
    label_nautical_to_kilometers.grid(row=11,column=0)
    label_nautical_to_kilometers_entry=Entry(druhe_okno)
    label_nautical_to_kilometers_entry.insert(END, "10")
    label_nautical_to_kilometers_entry.grid(row=11,column=1)
    def mphtokts():
        mphtokms_entry=label_nautical_to_kilometers_entry.get()
        mphtokms_converted=int(mphtokms_entry)*1.852
        result_display11 = str (round(mphtokms_converted, 3))
        label_converted_11=Label(druhe_okno,)
        label_converted_11["text"]=result_display11, "Kilometers"
        label_converted_11.grid(row=11,column=2)
    button_15=Button(druhe_okno,text="Convert", command=mphtokts,bg="SkyBlue4")
    button_15.grid(row=11,column=3)

###################

    label_Fahrenheit_to_celsius=Label(druhe_okno,text="Fahrenheit to Celsius")
    label_Fahrenheit_to_celsius.grid(row=12,column=0)
    label_Fahrenheit_to_celsius_entry=Entry(druhe_okno)
    label_Fahrenheit_to_celsius_entry.insert(END, "10")
    label_Fahrenheit_to_celsius_entry.grid(row=12,column=1)
    def f_to_c():
        ftoc_entry=label_Fahrenheit_to_celsius_entry.get()
        ftoc_converted=int(ftoc_entry)-32
        ftoc_converted1= ftoc_converted*5
        ftoc_converted2= ftoc_converted1/9
        result_display12 = str (round(ftoc_converted2, 3))
        label_converted_12=Label(druhe_okno,)
        label_converted_12["text"]=result_display12, "Celsius"
        label_converted_12.grid(row=12,column=2)
    button_16=Button(druhe_okno,text="Convert", command=f_to_c,bg="SkyBlue4")
    button_16.grid(row=12,column=3)

########################

    label_celsius_to_Fahrenheit=Label(druhe_okno,text="Celsius to Fahrenheit")
    label_celsius_to_Fahrenheit.grid(row=13,column=0)
    label_celsius_to_Fahrenheit_entry=Entry(druhe_okno)
    label_celsius_to_Fahrenheit_entry.insert(END, "10")
    label_celsius_to_Fahrenheit_entry.grid(row=13,column=1)
    def c_to_f():
        ctof_entry=label_celsius_to_Fahrenheit_entry.get()
        ctof_converted=int(ctof_entry)*9
        ctof_converted1= ctof_converted/5
        ctof_converted2= ctof_converted1+32
        result_display13 = str (round(ctof_converted2, 3))
        label_converted_13=Label(druhe_okno,)
        label_converted_13["text"]=result_display13, "Fahrenheit"
        label_converted_13.grid(row=13,column=2)
    button_17=Button(druhe_okno,text="Convert", command=c_to_f,bg="SkyBlue4")
    button_17.grid(row=13,column=3)




    label_close_unit=Label(druhe_okno,text="                                           ")
    label_close_unit.grid(row=20,column=0)
    button_close_unit=Button(druhe_okno,text="Close Convertor ", command=druhe_okno.destroy, bg="SkyBlue4")
    button_close_unit.grid(row=21,column=0)
def reset_formular ():
    os.execl(sys.executable, sys.executable, *sys.argv)


def takeScreenshot ():
    titles = pygetwindow.getAllTitles()
    window_handle = FindWindow(None, "OK-SKW Weight & balance open CARGO version")
    x1, y1, x2, y2   = GetWindowRect(window_handle)
    x1corrected = x1 + 8
    x2corrected = x2 - 8
    y1corrected = y1
    y2corrected = y2 -8
    im = pyautogui.screenshot()
    im = im.crop((x1corrected, y1corrected, x2corrected, y2corrected))
    file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    im.save(file_path)







hlavni_okno=Tk ()
hlavni_okno.title("OK-SKW Weight & balance open CARGO version")
hlavni_okno.iconbitmap("airplane.ico")
positionRight = int(0)
positionDown = int(0)
hlavni_okno.geometry("+{}+{}".format(positionRight, positionDown))

#entry section

label_r0_c0=Label(hlavni_okno,text="Pilot Name:")
label_r0_c0.grid(row=0,column=0)
E_r0_c0=Entry(hlavni_okno)
E_r0_c0.insert(END, "Vladimir Vopat")
E_r0_c0.grid(row=0,column=1)

label_r1_c0=Label(hlavni_okno,text="Pilot weight Kg")
label_r1_c0.grid(row=1,column=0)
E_r1_c0=Entry(hlavni_okno)
E_r1_c0.insert(END, "85")
E_r1_c0.grid(row=1,column=1)

label_r2_c0=Label(hlavni_okno,text="Fuel quantity / Liters Jet A1 front tank is")
label_r2_c0.grid(row=2,column=0)
E_r2_c0=Entry(hlavni_okno)
E_r2_c0.insert(END, "300")
E_r2_c0.grid(row=2,column=1)

label_r3_c0=Label(hlavni_okno,text="Fuel quantity / Liters Jet A1 rear tank")
label_r3_c0.grid(row=3,column=0)
E_r3_c0=Entry(hlavni_okno)
E_r3_c0.insert(END, "300")
E_r3_c0.grid(row=3,column=1)

label_r4_c0=Label(hlavni_okno,text="Wind velocity kts")
label_r4_c0.grid(row=4,column=0)
E_r4_c0=Entry(hlavni_okno)
E_r4_c0.insert(END, "1")
E_r4_c0.grid(row=4,column=1)

label_r5_c0=Label(hlavni_okno,text="Current date & time ")
label_r5_c0.grid(row=5,column=0)
E_r5_c0=Entry(hlavni_okno)
E_r5_c0.insert(END, current_timestamt)
E_r5_c0.grid(row=5,column=1)

label_r6_c0=Label(hlavni_okno,text="Cargo point 1 weight pounds")
label_r6_c0.grid(row=6,column=0)
E_r6_c0=Entry(hlavni_okno)
E_r6_c0.insert(END, "150")
E_r6_c0.grid(row=6,column=1)

label_r7_c0=Label(hlavni_okno,text="Cargo point 5 weight pounds")
label_r7_c0.grid(row=7,column=0)
E_r7_c0=Entry(hlavni_okno)
E_r7_c0.insert(END, "150")
E_r7_c0.grid(row=7,column=1)

label_r8_c0=Label(hlavni_okno,text="Cargo point 9 weight pounds")
label_r8_c0.grid(row=8,column=0)
E_r8_c0=Entry(hlavni_okno)
E_r8_c0.insert(END, "150")
E_r8_c0.grid(row=8,column=1)

label_r9_c0=Label(hlavni_okno,text="Cargo point 13 weight pounds")
label_r9_c0.grid(row=9,column=0)
E_r9_c0=Entry(hlavni_okno)
E_r9_c0.insert(END, "150")
E_r9_c0.grid(row=9,column=1)

label_r10_c0=Label(hlavni_okno,text="Cargo point 1 arm InAfDatum")
label_r10_c0.grid(row=10,column=0)
E_r10_c0=Entry(hlavni_okno)
E_r10_c0.insert(END, 93)
E_r10_c0.grid(row=10,column=1)

label_r11_c0=Label(hlavni_okno,text="Cargo point 5 arm InAfDatum")
label_r11_c0.grid(row=11,column=0)
E_r11_c0=Entry(hlavni_okno)
E_r11_c0.insert(END, 119.5)
E_r11_c0.grid(row=11,column=1)

label_r12_c0=Label(hlavni_okno,text="Cargo point 9 arm InAfDatum")
label_r12_c0.grid(row=12,column=0)
E_r12_c0=Entry(hlavni_okno)
E_r12_c0.insert(END, 146)
E_r12_c0.grid(row=12,column=1)

label_r13_c0=Label(hlavni_okno,text="Cargo point 13 arm InAfDatum")
label_r13_c0.grid(row=13,column=0)
E_r13_c0=Entry(hlavni_okno)
E_r13_c0.insert(END, 172.5)
E_r13_c0.grid(row=13,column=1)

###### COLUMN 2 section

label_r0_c2=Label(hlavni_okno,text="Basic empty plane weight")
label_r0_c2.grid(row=0,column=2)
E_r0_c2=Entry(hlavni_okno)
E_r0_c2.insert(END, "3506")
E_r0_c2.grid(row=0,column=3)

label_r1_c2=Label(hlavni_okno,text="Approved MTOW")
label_r1_c2.grid(row=1,column=2)
E_r1_c2=Entry(hlavni_okno)
E_r1_c2.insert(END, "7500")
E_r1_c2.grid(row=1,column=3)

label_r2_c2=Label(hlavni_okno,text="Runway direction magnetic")
label_r2_c2.grid(row=2,column=2)
E_r2_c2=Entry(hlavni_okno)
E_r2_c2.insert(END, "150")
E_r2_c2.grid(row=2,column=3)

label_r3_c2=Label(hlavni_okno,text="Wind direction")
label_r3_c2.grid(row=3,column=2)
E_r3_c2=Entry(hlavni_okno)
E_r3_c2.insert(END, "20")
E_r3_c2.grid(row=3,column=3)

label_r4_c2=Label(hlavni_okno,text="OAT Celsius")
label_r4_c2.grid(row=4,column=2)
E_r4_c2=Entry(hlavni_okno)
E_r4_c2.insert(END, "20")
E_r4_c2.grid(row=4,column=3)

label_r5_c2=Label(hlavni_okno,text="Take off distance available feets")
label_r5_c2.grid(row=5,column=2)
E_r5_c2=Entry(hlavni_okno)
E_r5_c2.insert(END, "3707")
E_r5_c2.grid(row=5,column=3)

label_r6_c2=Label(hlavni_okno,text="Cargo point 2 weight pounds")
label_r6_c2.grid(row=6,column=2)
E_r6_c2=Entry(hlavni_okno)
E_r6_c2.insert(END, "150")
E_r6_c2.grid(row=6,column=3)

label_r7_c2=Label(hlavni_okno,text="Cargo point 6 weight pounds")
label_r7_c2.grid(row=7,column=2)
E_r7_c2=Entry(hlavni_okno)
E_r7_c2.insert(END, "150")
E_r7_c2.grid(row=7,column=3)

label_r8_c2=Label(hlavni_okno,text="Cargo point 10 weight pounds")
label_r8_c2.grid(row=8,column=2)
E_r8_c2=Entry(hlavni_okno)
E_r8_c2.insert(END, "150")
E_r8_c2.grid(row=8,column=3)

label_r9_c2=Label(hlavni_okno,text="Cargo point 14 weight pounds")
label_r9_c2.grid(row=9,column=2)
E_r9_c2=Entry(hlavni_okno)
E_r9_c2.insert(END, "150")
E_r9_c2.grid(row=9,column=3)

label_r10_c2=Label(hlavni_okno,text="Cargo point 2 arm InAfDatum")
label_r10_c2.grid(row=10,column=2)
E_r10_c2=Entry(hlavni_okno)
E_r10_c2.insert(END, 93)
E_r10_c2.grid(row=10,column=3)

label_r11_c2=Label(hlavni_okno,text="Cargo point 6 arm InAfDatum")
label_r11_c2.grid(row=11,column=2)
E_r11_c2=Entry(hlavni_okno)
E_r11_c2.insert(END, 119.5)
E_r11_c2.grid(row=11,column=3)

label_r12_c2=Label(hlavni_okno,text="Cargo point 10 arm InAfDatum")
label_r12_c2.grid(row=12,column=2)
E_r12_c2=Entry(hlavni_okno)
E_r12_c2.insert(END, 146)
E_r12_c2.grid(row=12,column=3)

label_r13_c2=Label(hlavni_okno,text="Cargo point 14 arm InAfDatum")
label_r13_c2.grid(row=13,column=2)
E_r13_c2=Entry(hlavni_okno)
E_r13_c2.insert(END, 172.5)
E_r13_c2.grid(row=13,column=3)

#Column 4 SECTION

label_r0_c4=Label(hlavni_okno,text="Pilot 2 name ")
label_r0_c4.grid(row=0,column=4)
E_r0_c4=Entry(hlavni_okno)
E_r0_c4.insert(END, "Jan Bracha")
E_r0_c4.grid(row=0,column=5)

label_r1_c4=Label(hlavni_okno,text="QNH")
label_r1_c4.grid(row=1,column=4)
E_r1_c4=Entry(hlavni_okno)
E_r1_c4.insert(END, "1012.25")
E_r1_c4.grid(row=1,column=5)

label_r2_c4=Label(hlavni_okno,text="Basic empty plane arm InAfDatum")
label_r2_c4.grid(row=2,column=4)
E_r2_c4=Entry(hlavni_okno)
E_r2_c4.insert(END, "109.71")
E_r2_c4.grid(row=2,column=5)

label_r3_c4=Label(hlavni_okno,text="Pilot 2 arm InAfDatum")
label_r3_c4.grid(row=3,column=4)
E_r3_c4=Entry(hlavni_okno)
E_r3_c4.insert(END, "66.5")
E_r3_c4.grid(row=3,column=5)

label_r4_c4=Label(hlavni_okno,text="Fuel rear tanks InAfDatum")
label_r4_c4.grid(row=4,column=4)
E_r4_c4=Entry(hlavni_okno)
E_r4_c4.insert(END, 139.15)
E_r4_c4.grid(row=4,column=5)

label_r6_c4=Label(hlavni_okno,text="Cargo point 3 weight pounds")
label_r6_c4.grid(row=6,column=4)
E_r6_c4=Entry(hlavni_okno)
E_r6_c4.insert(END, "150")
E_r6_c4.grid(row=6,column=5)

label_r7_c4=Label(hlavni_okno,text="Cargo point 7 weight pounds")
label_r7_c4.grid(row=7,column=4)
E_r7_c4=Entry(hlavni_okno)
E_r7_c4.insert(END, "150")
E_r7_c4.grid(row=7,column=5)

label_r8_c4=Label(hlavni_okno,text="Cargo point 11 weight pounds")
label_r8_c4.grid(row=8,column=4)
E_r8_c4=Entry(hlavni_okno)
E_r8_c4.insert(END, "150")
E_r8_c4.grid(row=8,column=5)

label_r9_c4=Label(hlavni_okno,text="Cargo point 15 weight pounds")
label_r9_c4.grid(row=9,column=4)
E_r9_c4=Entry(hlavni_okno)
E_r9_c4.insert(END, "150")
E_r9_c4.grid(row=9,column=5)

label_r10_c4=Label(hlavni_okno,text="Cargo point 3 arm InAfDatum")
label_r10_c4.grid(row=10,column=4)
E_r10_c4=Entry(hlavni_okno)
E_r10_c4.insert(END, 106.25)
E_r10_c4.grid(row=10,column=5)

label_r11_c4=Label(hlavni_okno,text="Cargo point 7 arm InAfDatum")
label_r11_c4.grid(row=11,column=4)
E_r11_c4=Entry(hlavni_okno)
E_r11_c4.insert(END, 132.75)
E_r11_c4.grid(row=11,column=5)

label_r12_c4=Label(hlavni_okno,text="Cargo point 11 arm InAfDatum")
label_r12_c4.grid(row=12,column=4)
E_r12_c4=Entry(hlavni_okno)
E_r12_c4.insert(END, 159.25)
E_r12_c4.grid(row=12,column=5)

label_r13_c4=Label(hlavni_okno,text="Cargo point 15 arm InAfDatum")
label_r13_c4.grid(row=13,column=4)
E_r13_c4=Entry(hlavni_okno)
E_r13_c4.insert(END, 185.75)
E_r13_c4.grid(row=13,column=5)


# cloumn 6 section
label_r0_c6=Label(hlavni_okno,text="Pilot 2 weight kg ")
label_r0_c6.grid(row=0,column=6)
E_r0_c6=Entry(hlavni_okno)
E_r0_c6.insert(END, "85")
E_r0_c6.grid(row=0,column=7)

label_r1_c6=Label(hlavni_okno,text="Airfield elevation")
label_r1_c6.grid(row=1,column=6)
E_r1_c6=Entry(hlavni_okno)
E_r1_c6.insert(END, "1100")
E_r1_c6.grid(row=1,column=7)


label_r2_c6=Label(hlavni_okno,text="Pilot 1 arm InAfDatum ")
label_r2_c6.grid(row=2,column=6)
E_r2_c6=Entry(hlavni_okno)
E_r2_c6.insert(END, 66.5)
E_r2_c6.grid(row=2,column=7)

label_r3_c6=Label(hlavni_okno,text="Fuel fron tanks InAfDatum ")
label_r3_c6.grid(row=3,column=6)
E_r3_c6=Entry(hlavni_okno)
E_r3_c6.insert(END, 110.2)
E_r3_c6.grid(row=3,column=7)

label_r6_c6=Label(hlavni_okno,text="Cargo point 4 weight pounds")
label_r6_c6.grid(row=6,column=6)
E_r6_c6=Entry(hlavni_okno)
E_r6_c6.insert(END, "150")
E_r6_c6.grid(row=6,column=7)

label_r7_c6=Label(hlavni_okno,text="Cargo point 8 weight pounds")
label_r7_c6.grid(row=7,column=6)
E_r7_c6=Entry(hlavni_okno)
E_r7_c6.insert(END, "150")
E_r7_c6.grid(row=7,column=7)

label_r8_c6=Label(hlavni_okno,text="Cargo point 12 weight pounds")
label_r8_c6.grid(row=8,column=6)
E_r8_c6=Entry(hlavni_okno)
E_r8_c6.insert(END, "150")
E_r8_c6.grid(row=8,column=7)

label_r9_c6=Label(hlavni_okno,text="Cargo point 16 weight pounds")
label_r9_c6.grid(row=9,column=6)
E_r9_c6=Entry(hlavni_okno)
E_r9_c6.insert(END, "150")
E_r9_c6.grid(row=9,column=7)

label_r10_c6=Label(hlavni_okno,text="Cargo point 4 arm InAfDatum")
label_r10_c6.grid(row=10,column=6)
E_r10_c6=Entry(hlavni_okno)
E_r10_c6.insert(END, 106.25)
E_r10_c6.grid(row=10,column=7)

label_r11_c6=Label(hlavni_okno,text="Cargo point 8 arm InAfDatum")
label_r11_c6.grid(row=11,column=6)
E_r11_c6=Entry(hlavni_okno)
E_r11_c6.insert(END, 132.75)
E_r11_c6.grid(row=11,column=7)

label_r12_c6=Label(hlavni_okno,text="Cargo point 12 arm InAfDatum")
label_r12_c6.grid(row=12,column=6)
E_r12_c6=Entry(hlavni_okno)
E_r12_c6.insert(END, 159.25)
E_r12_c6.grid(row=12,column=7)

label_r13_c6=Label(hlavni_okno,text="Cargo point 16 arm InAfDatum")
label_r13_c6.grid(row=13,column=6)
E_r13_c6=Entry(hlavni_okno)
E_r13_c6.insert(END, 185.75)
E_r13_c6.grid(row=13,column=7)



#definition GUI separation

label_separator_1=Label(hlavni_okno,text="")
label_separator_1.grid(row=14,column=0)
label_separator_2=Label(hlavni_okno,text="")
label_separator_2.grid(row=14,column=1)
label_separator_3=Label(hlavni_okno,text="")
label_separator_3.grid(row=14,column=2)
label_separator_4=Label(hlavni_okno,text="")
label_separator_4.grid(row=14,column=3)
label_separator_5=Label(hlavni_okno,text="")
label_separator_5.grid(row=14,column=4)
label_separator_6=Label(hlavni_okno,text="")
label_separator_6.grid(row=14,column=5)
label_separator_7=Label(hlavni_okno,text="")
label_separator_7.grid(row=14,column=6)
label_separator_8=Label(hlavni_okno,text="")
label_separator_8.grid(row=14,column=7)

# end of GUI separator definition

button_1=Button(hlavni_okno,text="Reset formular",command=reset_formular, bg="SkyBlue4")
button_1.grid(row=30,column=1)
button_2=Button(hlavni_okno,text="Compute cargo W&B", command=compute, bg="SkyBlue4")
button_2.grid(row=30,column=2)
button_3=Button(hlavni_okno,text="Unit convertor", command=unit_calculator, bg="SkyBlue4")
button_3.grid(row=30,column=3)
button_pdf=Button(hlavni_okno,text="PAC 750 manuals", command=pdf, bg="SkyBlue4")
button_pdf.grid(row=30,column=4)
button_weather=Button(hlavni_okno,text="Check weather", command=weather, bg="SkyBlue4")
button_weather.grid(row=30,column=5)
button_printscreen=Button(hlavni_okno,text="Export save", command=takeScreenshot, bg="SkyBlue4")
button_printscreen.grid(row=30,column=6)



hlavni_okno.mainloop ()
