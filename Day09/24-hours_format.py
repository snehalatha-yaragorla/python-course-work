hours = int(input("enter hours: "))
minutes = int(input("enter minutes: "))
if hours>12 and hours<24:
    hours1=hours-12
    if minutes>60:
        m=minutes//60
        m1=minutes%60
        time=hours1+m
        if time > 12:
            time=time-12
        print("time is: ",time,"Hour ",m1,"Minutes"," PM")
elif hours<12:
    m=minutes//60
    m1=minutes%60
    hours=hours+m
    if hours>12:
        hours1=hours-12
        Print("time is: ",hours,"Hour ",m1,"Minutes"," AM")
elif hours==12:
    hours=hours-12
    m=minutes//60
    m1=minutes%60
    hours=hours+m
    print("time is: ",hours,"Hour ",m1,"Minutes","AM")
else:
    print("enter correct time")
