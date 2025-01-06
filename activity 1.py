MC=bool(input("Do you have a medical certificate for absents?"))
atendance=int(input("How many times did you attend?"))
if MC==True:
    print("You can enter the exam")
else:
    if  atendance>75:
        print("You can do the exam")
    else:
        print("You can't do the exam")