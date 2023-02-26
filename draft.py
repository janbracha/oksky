from tkinter import *
import math
import os
import time
from PIL import ImageGrab



#zadani aktualniho casu
secondsSinceEpoch = time.time()
timeObj = time.localtime(secondsSinceEpoch)
current_timestamt=('%d-%d-%d-%d-%d-%d' % (timeObj.tm_mday, timeObj.tm_mon, timeObj.tm_year, timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))
#konec zadani aktualniho casu

def vypocet():

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
    #print()
    total_moment = moment_pilot_1 + moment_pilot_2 + moment_fuel_rear_tanks + moment_fuel_front_tanks +moment_empty_plane + moment_cargo_ponit_1 + moment_cargo_ponit_2 + moment_cargo_ponit_3 + moment_cargo_ponit_4 + moment_cargo_ponit_5 + moment_cargo_ponit_6 + moment_cargo_ponit_7 + moment_cargo_ponit_8 + moment_cargo_ponit_9 + moment_cargo_ponit_10 + moment_cargo_ponit_11 + moment_cargo_ponit_12 + moment_cargo_ponit_13 + moment_cargo_ponit_14 + moment_cargo_ponit_15 + moment_cargo_ponit_16
    total_tow = pilot_1_weight_pounds + pilot_2_weight_pounds + fuel_front_tank_weight_pounds + fuel_rear_tank_weight_pounds + basic_empty_weight + cargo_1_weight_ponds + cargo_2_weight_ponds + cargo_3_weight_ponds + cargo_4_weight_ponds + cargo_5_weight_ponds + cargo_6_weight_ponds + cargo_7_weight_ponds + cargo_8_weight_ponds + cargo_9_weight_ponds + cargo_10_weight_ponds + cargo_11_weight_ponds + cargo_12_weight_ponds + cargo_13_weight_ponds + cargo_14_weight_ponds + cargo_15_weight_ponds +cargo_16_weight_ponds
    total_CG =total_moment / total_tow



#crosswind calculation

    crosswind_drift = wind_derection - runway_magnetic_direction
    crosswind_current = math.sin(crosswind_drift) * wind_velocity

    label_result_r22_c4=Label(hlavni_okno,text="current crosswind is:")
    label_result_r22_c4.grid(row=22,column=4)
    str_crosswind = str (round(crosswind_current, 1)), "kts"
    label_result_r22_c5=Label(hlavni_okno)
    label_result_r22_c5["text"]=str_crosswind
    label_result_r22_c5.grid(row=22,column=5)

    if crosswind_current <=14:
        label_result_r25_c0=Label(hlavni_okno,text="Crosswind within limits, take off approved",bg="green")
        label_result_r25_c0.grid(row=25,column=0)
    else:
        label_result_r25_c0=Label(hlavni_okno,text="Crosswind out of limits",bg="red")
        label_result_r25_c0.grid(row=25,column=0)

#end of crosswind calculation

#MTOW check and CG check
    if total_tow >=approved_mtow:
        label_result_r25_c1=Label(hlavni_okno,text="MTOW over limit", bg="red")
        label_result_r25_c1.grid(row=25,column=1)
        label_result_r21_c0=Label(hlavni_okno,text="CG unable detrminate, MTOW over limit",bg="red")
        label_result_r21_c0.grid(row=21,column=0)
    elif total_tow <=4209:
        label_result_r25_c1=Label(hlavni_okno,text="MTOW within limits", bg="green")
        label_result_r25_c1.grid(row=25,column=1)
        label_result_r21_c0=Label(hlavni_okno,text="CG for this payload is ")
        label_result_r21_c0.grid(row=21,column=0)
        label_result_r21_c1=Label(hlavni_okno,text="Forward 100.46 InAfDatum After 125.6 InAfDatum")
        label_result_r21_c1.grid(row=21,column=2)
        if total_CG <=100.46:
            label_result_r25_c1=Label(hlavni_okno,text="CG out of limtis", bg="red")
            label_result_r25_c1.grid(row=25,column=2)
        else:
            label_result_r25_c1=Label(hlavni_okno,text="CG within limits", bg="green")
            label_result_r25_c1.grid(row=25,column=2)
    elif total_tow <=5639:
        label_result_r25_c1=Label(hlavni_okno,text="MTOW within limits", bg="green")
        label_result_r25_c1.grid(row=25,column=1)
        label_result_r21_c0=Label(hlavni_okno,text="CG for this payload is ")
        label_result_r21_c0.grid(row=21,column=0)
        label_result_r21_c1=Label(hlavni_okno,text="Forward 103.18 InAfDatum After 125.6 InAfDatum")
        label_result_r21_c1.grid(row=21,column=2)
        if total_CG <=103.18:
            label_result_r25_c1=Label(hlavni_okno,text="CG out of limtis", bg="red")
            label_result_r25_c1.grid(row=25,column=2)
        else:
            label_result_r25_c1=Label(hlavni_okno,text="CG within limits", bg="green")
            label_result_r25_c1.grid(row=25,column=2)
    else:
        label_result_r25_c1=Label(hlavni_okno,text="MTOW within limits", bg="green")
        label_result_r25_c1.grid(row=25,column=1)
        label_result_r21_c0=Label(hlavni_okno,text="CG for this payload is ")
        label_result_r21_c0.grid(row=21,column=0)
        label_result_r21_c1=Label(hlavni_okno,text="Forward 111.55 InAfDatum After 125.6 InAfDatum")
        label_result_r21_c1.grid(row=21,column=2)

        if total_CG <=111.55:
            label_result_r25_c1=Label(hlavni_okno,text="CG out of limtis", bg="red")
            label_result_r25_c1.grid(row=25,column=2)
        else:
            label_result_r25_c1=Label(hlavni_okno,text="CG within limits", bg="green")
            label_result_r25_c1.grid(row=25,column=2)
#end of MTOW & CG check function
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
#konec #funkce nearest payload
#funkce nearest OAT
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

#konec funkce nearest OAT

#funkce vyber z pole hodnot pro take off SL
    list = [[1606, 1695, 1785, 1956, 2208],
            [1341, 1414, 1487, 1626, 1822],
            [1028, 1083, 1140, 1242, 1384],
            [769, 810, 852, 926, 1028]]

    label_result_r21_c3=Label(hlavni_okno,text="reguired Runway lenght is")
    label_result_r21_c3.grid(row=21,column=3)
    take_off_distance = (list [(payload_cursor)][(temperature_cursor)])
    label_result_r21_c4=Label(hlavni_okno)
    take_off_distance_label_var = str (round(take_off_distance, 1)), "feets"
    label_result_r21_c4["text"]=take_off_distance_label_var
    label_result_r21_c4.grid(row=21,column=4)

    TODA_entry = E_r5_c2.get()
    TODA = int(TODA_entry)

    if TODA <= take_off_distance:
        label_TODA_warning=Label(hlavni_okno,text="Runway/ TODA is too short !!!",bg="red")
        label_TODA_warning.grid(row=25,column=3)
    else:
        label_TODA_warning=Label(hlavni_okno,text="TODA within limits, take off Approved",bg="green")
        label_TODA_warning.grid(row=25,column=3)




#po dodelani prehodit pod sekci momen

    label_result_r22_c0=Label(hlavni_okno,text="total CG is:")
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



#konec sekce na prehozeni





    label_result_r15_c0=Label(hlavni_okno,text="pilot 1 moment is:")
    label_result_r15_c0.grid(row=15,column=0)
    str_pilot_1_mnt= str (round(moment_pilot_1, 1)), "in.lbs"
    label_result_r15_c1=Label(hlavni_okno)
    label_result_r15_c1["text"]=str_pilot_1_mnt
    label_result_r15_c1.grid(row=15,column=1)

    label_result_r15_c2=Label(hlavni_okno,text="pilot 2 moment is:")
    label_result_r15_c2.grid(row=15,column=2)
    str_pilot_2_mnt= str (round(moment_pilot_2, 1)), "in.lbs"
    label_result_r15_c3=Label(hlavni_okno)
    label_result_r15_c3["text"]=str_pilot_2_mnt
    label_result_r15_c3.grid(row=15,column=3)

    label_result_r15_c4=Label(hlavni_okno,text="fuel front tank moment is:")
    label_result_r15_c4.grid(row=15,column=4)
    str_fuel_front= str (round(moment_fuel_front_tanks, 1)), "in.lbs"
    label_result_r15_c5=Label(hlavni_okno)
    label_result_r15_c5["text"]=str_fuel_front
    label_result_r15_c5.grid(row=15,column=5)

    label_result_r15_c6=Label(hlavni_okno,text="fuel rear tank moment is:")
    label_result_r15_c6.grid(row=15,column=6)
    str_fuel_rear= str (round(moment_fuel_rear_tanks, 1)), "in.lbs"
    label_result_r15_c7=Label(hlavni_okno)
    label_result_r15_c7["text"]=str_fuel_rear
    label_result_r15_c7.grid(row=15,column=7)

    label_result_r16_c0=Label(hlavni_okno,text="empty plane moment is:")
    label_result_r16_c0.grid(row=16,column=0)
    str_empty_plane= str (round(moment_empty_plane, 1)), "in.lbs"
    label_result_r16_c1=Label(hlavni_okno)
    label_result_r16_c1["text"]=str_empty_plane
    label_result_r16_c1.grid(row=16,column=1)

    label_result_r16_c2=Label(hlavni_okno,text="cargo point 1 moment is:")
    label_result_r16_c2.grid(row=16,column=2)
    str_cargo_1= str (round(moment_cargo_ponit_1, 1)), "in.lbs"
    label_result_r16_c3=Label(hlavni_okno)
    label_result_r16_c3["text"]=str_cargo_1
    label_result_r16_c3.grid(row=16,column=3)

    label_result_r16_c4=Label(hlavni_okno,text="cargo point 2 moment is:")
    label_result_r16_c4.grid(row=16,column=4)
    str_cargo_2= str (round(moment_cargo_ponit_2, 1)), "in.lbs"
    label_result_r16_c5=Label(hlavni_okno)
    label_result_r16_c5["text"]=str_cargo_2
    label_result_r16_c5.grid(row=16,column=5)

    label_result_r16_c6=Label(hlavni_okno,text="cargo point 3 moment is:")
    label_result_r16_c6.grid(row=16,column=6)
    str_cargo_3= str (round(moment_cargo_ponit_3, 1)), "in.lbs"
    label_result_r16_c7=Label(hlavni_okno)
    label_result_r16_c7["text"]=str_cargo_3
    label_result_r16_c7.grid(row=16,column=7)

    label_result_r17_c0=Label(hlavni_okno,text="cargo point 4 moment is:")
    label_result_r17_c0.grid(row=17,column=0)
    str_cargo_4= str (round(moment_cargo_ponit_4, 1)), "in.lbs"
    label_result_r17_c1=Label(hlavni_okno)
    label_result_r17_c1["text"]=str_cargo_4
    label_result_r17_c1.grid(row=17,column=1)

    label_result_r17_c2=Label(hlavni_okno,text="cargo point 5 moment is:")
    label_result_r17_c2.grid(row=17,column=2)
    str_cargo_5= str (round(moment_cargo_ponit_5, 1)), "in.lbs"
    label_result_r17_c3=Label(hlavni_okno)
    label_result_r17_c3["text"]=str_cargo_5
    label_result_r17_c3.grid(row=17,column=3)

    label_result_r17_c4=Label(hlavni_okno,text="cargo point 6 moment is:")
    label_result_r17_c4.grid(row=17,column=4)
    str_cargo_6= str (round(moment_cargo_ponit_6, 1)), "in.lbs"
    label_result_r17_c5=Label(hlavni_okno)
    label_result_r17_c5["text"]=str_cargo_6
    label_result_r17_c5.grid(row=17,column=5)

    label_result_r17_c6=Label(hlavni_okno,text="cargo point 7 moment is:")
    label_result_r17_c6.grid(row=17,column=6)
    str_cargo_7= str (round(moment_cargo_ponit_7, 1)), "in.lbs"
    label_result_r17_c7=Label(hlavni_okno)
    label_result_r17_c7["text"]=str_cargo_7
    label_result_r17_c7.grid(row=17,column=7)

    label_result_r18_c0=Label(hlavni_okno,text="cargo point 8 moment is:")
    label_result_r18_c0.grid(row=18,column=0)
    str_cargo_8= str (round(moment_cargo_ponit_8, 1)), "in.lbs"
    label_result_r18_c1=Label(hlavni_okno)
    label_result_r18_c1["text"]=str_cargo_8
    label_result_r18_c1.grid(row=18,column=1)

    label_result_r18_c2=Label(hlavni_okno,text="cargo point 9 moment is:")
    label_result_r18_c2.grid(row=18,column=2)
    str_cargo_9= str (round(moment_cargo_ponit_9, 1)), "in.lbs"
    label_result_r18_c3=Label(hlavni_okno)
    label_result_r18_c3["text"]=str_cargo_9
    label_result_r18_c3.grid(row=18,column=3)

    label_result_r18_c4=Label(hlavni_okno,text="cargo point 10 moment is:")
    label_result_r18_c4.grid(row=18,column=4)
    str_cargo_10= str (round(moment_cargo_ponit_10, 1)), "in.lbs"
    label_result_r18_c5=Label(hlavni_okno)
    label_result_r18_c5["text"]=str_cargo_10
    label_result_r18_c5.grid(row=18,column=5)

    label_result_r18_c6=Label(hlavni_okno,text="cargo point 11 moment is:")
    label_result_r18_c6.grid(row=18,column=6)
    str_cargo_11= str (round(moment_cargo_ponit_11, 1)), "in.lbs"
    label_result_r18_c7=Label(hlavni_okno)
    label_result_r18_c7["text"]=str_cargo_11
    label_result_r18_c7.grid(row=18,column=7)

    label_result_r19_c0=Label(hlavni_okno,text="cargo point 12 moment is:")
    label_result_r19_c0.grid(row=19,column=0)
    str_cargo_12= str (round(moment_cargo_ponit_12, 1)), "in.lbs"
    label_result_r19_c1=Label(hlavni_okno)
    label_result_r19_c1["text"]=str_cargo_12
    label_result_r19_c1.grid(row=19,column=1)

    label_result_r19_c2=Label(hlavni_okno,text="cargo point 13 moment is:")
    label_result_r19_c2.grid(row=19,column=2)
    str_cargo_13= str (round(moment_cargo_ponit_13, 1)), "in.lbs"
    label_result_r19_c3=Label(hlavni_okno)
    label_result_r19_c3["text"]=str_cargo_13
    label_result_r19_c3.grid(row=19,column=3)

    label_result_r19_c4=Label(hlavni_okno,text="cargo point 14 moment is:")
    label_result_r19_c4.grid(row=19,column=4)
    str_cargo_14= str (round(moment_cargo_ponit_14, 1)), "in.lbs"
    label_result_r19_c5=Label(hlavni_okno)
    label_result_r19_c5["text"]=str_cargo_14
    label_result_r19_c5.grid(row=19,column=5)

    label_result_r19_c6=Label(hlavni_okno,text="cargo point 15 moment is:")
    label_result_r19_c6.grid(row=19,column=6)
    str_cargo_15= str (round(moment_cargo_ponit_15, 1)), "in.lbs"
    label_result_r19_c7=Label(hlavni_okno)
    label_result_r19_c7["text"]=str_cargo_15
    label_result_r19_c7.grid(row=19,column=7)

    label_result_r20_c0=Label(hlavni_okno,text="cargo point 16 moment is:")
    label_result_r20_c0.grid(row=20,column=0)
    str_cargo_16= str (round(moment_cargo_ponit_16, 1)), "in.lbs"
    label_result_r20_c1=Label(hlavni_okno)
    label_result_r20_c1["text"]=str_cargo_16
    label_result_r20_c1.grid(row=20,column=1)

    label_result_r20_c2=Label(hlavni_okno,text="total moment moment is:")
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






def weight_balance ():
    os.execl(sys.executable, sys.executable, *sys.argv)

hlavni_okno=Tk ()
hlavni_okno.title("OK-SKW Weight & balance open CARGO version "       "                        Copyright © 2019 Jan Bracha Skysurf s.r.o          distributed as The GNU General Public License")
hlavni_okno.iconbitmap("airplane.ico")
positionRight = int(0)
positionDown = int(0)
hlavni_okno.geometry("+{}+{}".format(positionRight, positionDown))

#entry section

label_r0_c0=Label(hlavni_okno,text="Pilot Name:")
label_r0_c0.grid(row=0,column=0)
E_r0_c0=Entry(hlavni_okno)
E_r0_c0.insert(END, "Honza")
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
E_r6_c0.insert(END, "200")
E_r6_c0.grid(row=6,column=1)

label_r7_c0=Label(hlavni_okno,text="Cargo point 5 weight pounds")
label_r7_c0.grid(row=7,column=0)
E_r7_c0=Entry(hlavni_okno)
E_r7_c0.insert(END, "200")
E_r7_c0.grid(row=7,column=1)

label_r8_c0=Label(hlavni_okno,text="Cargo point 9 weight pounds")
label_r8_c0.grid(row=8,column=0)
E_r8_c0=Entry(hlavni_okno)
E_r8_c0.insert(END, "200")
E_r8_c0.grid(row=8,column=1)

label_r9_c0=Label(hlavni_okno,text="Cargo point 13 weight pounds")
label_r9_c0.grid(row=9,column=0)
E_r9_c0=Entry(hlavni_okno)
E_r9_c0.insert(END, "200")
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
E_r2_c2.insert(END, "200")
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
E_r6_c2.insert(END, "1")
E_r6_c2.grid(row=6,column=3)

label_r7_c2=Label(hlavni_okno,text="Cargo point 6 weight pounds")
label_r7_c2.grid(row=7,column=2)
E_r7_c2=Entry(hlavni_okno)
E_r7_c2.insert(END, "1")
E_r7_c2.grid(row=7,column=3)

label_r8_c2=Label(hlavni_okno,text="Cargo point 10 weight pounds")
label_r8_c2.grid(row=8,column=2)
E_r8_c2=Entry(hlavni_okno)
E_r8_c2.insert(END, "1")
E_r8_c2.grid(row=8,column=3)

label_r9_c2=Label(hlavni_okno,text="Cargo point 14 weight pounds")
label_r9_c2.grid(row=9,column=2)
E_r9_c2=Entry(hlavni_okno)
E_r9_c2.insert(END, "1")
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
E_r0_c4.insert(END, "Vlada")
E_r0_c4.grid(row=0,column=5)

label_r1_c4=Label(hlavni_okno,text="QNH")
label_r1_c4.grid(row=1,column=4)
E_r1_c4=Entry(hlavni_okno)
E_r1_c4.insert(END, "1012,25")
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
E_r6_c4.insert(END, "200")
E_r6_c4.grid(row=6,column=5)

label_r7_c4=Label(hlavni_okno,text="Cargo point 7 weight pounds")
label_r7_c4.grid(row=7,column=4)
E_r7_c4=Entry(hlavni_okno)
E_r7_c4.insert(END, "200")
E_r7_c4.grid(row=7,column=5)

label_r8_c4=Label(hlavni_okno,text="Cargo point 11 weight pounds")
label_r8_c4.grid(row=8,column=4)
E_r8_c4=Entry(hlavni_okno)
E_r8_c4.insert(END, "200")
E_r8_c4.grid(row=8,column=5)

label_r9_c4=Label(hlavni_okno,text="Cargo point 15 weight pounds")
label_r9_c4.grid(row=9,column=4)
E_r9_c4=Entry(hlavni_okno)
E_r9_c4.insert(END, "200")
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
E_r6_c6.insert(END, "200")
E_r6_c6.grid(row=6,column=7)

label_r7_c6=Label(hlavni_okno,text="Cargo point 8 weight pounds")
label_r7_c6.grid(row=7,column=6)
E_r7_c6=Entry(hlavni_okno)
E_r7_c6.insert(END, "200")
E_r7_c6.grid(row=7,column=7)

label_r8_c6=Label(hlavni_okno,text="Cargo point 12 weight pounds")
label_r8_c6.grid(row=8,column=6)
E_r8_c6=Entry(hlavni_okno)
E_r8_c6.insert(END, "200")
E_r8_c6.grid(row=8,column=7)

label_r9_c6=Label(hlavni_okno,text="Cargo point 16 weight pounds")
label_r9_c6.grid(row=9,column=6)
E_r9_c6=Entry(hlavni_okno)
E_r9_c6.insert(END, "200")
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





button_1=Button(hlavni_okno,text="reset",command=weight_balance)
button_1.grid(row=30,column=1)
button_2=Button(hlavni_okno,text="Compute cargo W&B", command=vypocet)
button_2.grid(row=30,column=2)

hlavni_okno.mainloop ()
