month=['January','Febuarary','March','April','May','June','July','August','September','October','November','December']
month_name=input(('Enter the month name: '))
date=int(input('Enter day: '))
if (month_name=='January') and date==1:
    print("New year's day")
elif (month_name=='July') and date==1:
    print('Canada day')
elif (month_name=='December') and date==25:
    print('Christmas day')
else:
    print('Do not correspond to a fixed-day holiday')