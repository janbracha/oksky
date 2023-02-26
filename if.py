print ('program if')
vzletova_hmotnost = float(input('Zadej stranu čtverce v centimetrech: '))


if float (vzletova_hmotnost) >=7500:
    print('vice nez 7500')
    #label_15=Label(my_window,text="MTOW PREKROCEN !!!",bg="red",fg="blue")
    #label_15.grid(row=15,column=1)
elif float (vzletova_hmotnost) <=4209:
    print('mene nez 4209')
    #label_16=Label(my_window,text="MTOW v limitech, start povolen!!",bg="green")
    #label_16.grid(row=15,column=1)
    #label_CG_Limit=Label(my_window,text="forward 100.46 iad aft 125.6 iad")
    #label_CG_Limit.grid(row=11,column=1)
elif float (vzletova_hmotnost) <=5639:
    print('mene nez 5639')
    #label_16=Label(my_window,text="MTOW v limitech, start povolen!!",bg="green")
    #label_16.grid(row=15,column=1)
    #label_CG_Limit=Label(my_window,text="forward 111.55 iad aft 125.6 iad")
    #label_CG_Limit.grid(row=11,column=1)
else :
    print('mene nez 7500')
    #label_16=Label(my_window,text="MTOW v limitech, start povolen!!",bg="green")
    #label_16.grid(row=15,column=1)
    #label_CG_Limit=Label(my_window,text="forward 100.46 iad aft 125.6 iad")
    #label_CG_Limit.grid(row=11,column=1)

#if strana > 0:
#    print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')#
#    print('Obsah čtverce se stranou', strana, 'je', strana ** 2, 'cm2')
#else:
    print('Strana musí být kladná, jinak z toho nebude čtverec!')

print('Děkujeme za použití geometrické kalkulačky.')
