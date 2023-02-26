import math


#crosswind_drift = wind_derection - runway_magnetic_direction
#crosswind_sinus = math.sin(crosswind_drift)
#crosswind_current = math.sin(crosswind_drift) * wind_velocity



smer_drahy = int (input('zadej smer drahy '))
smer_vetru = int (input('zadej smer vetru '))
sila_vetru = int (input('zadej silu vetru '))
zbytek_uhlu_drahy = 360 -smer_drahy
zbytek_uhlu_vetru= 360 - smer_vetru

print ('smer drahy je :', smer_drahy)
print ('smer vetru je :', smer_vetru)
print ('sila vetru je :', sila_vetru)
print ('zbytek uhlu drahy do 360 je :', zbytek_uhlu_drahy)
print ('zbytek uhlu vetru do 360 je :', zbytek_uhlu_vetru)
if zbytek_uhlu_drahy >= zbytek_uhlu_vetru:
    delta = zbytek_uhlu_drahy - zbytek_uhlu_vetru
else:
    delta = zbytek_uhlu_vetru - zbytek_uhlu_drahy
if delta <=180:
    rozdil_uhlu = delta
else:
    rozdil_uhlu = 360 - delta

#crosswind_drift = wind_derection - runway_magnetic_direction
crosswind_current = math.sin(rozdil_uhlu) * sila_vetru
sinus_uhlu= math.sin(rozdil_uhlu)
print (delta)
print ('sinus uhlu je :', sinus_uhlu)
print ('delta uhlu je : ', rozdil_uhlu)
print ('bocni vitr je :', crosswind_current)


#if crosswind <=14:
#    label_crosswind_demonstrated=Label(my_window,text="Crosswind within limits, take off approved",bg="green")
#    label_crosswind_demonstrated.grid(row=15,column=2)
#else:
#    label_crosswind_demonstrated=Label(my_window,text="Crosswind out of limits",bg="red")
#    label_crosswind_demonstrated.grid(row=15,column=2)
