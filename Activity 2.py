unit=int(input("Enter the number of units you used "))
if unit<50:
    amt=unit*2.6
    tax=25
elif unit<100:
    amt=130+((unit-50)*3.25)
    tax=35
elif unit<200:
    amt=130+126.5+((unit-100)*5.26 )
    tax=45
else:
    amt=130+126.5+526+((unit-200)*8.45)
    tax=75
print("Your electricity bill is ",amt+tax)