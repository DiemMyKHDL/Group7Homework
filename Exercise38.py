month_name=input('Enter the month name: ')
month=['January','Febuarary','March','April','May','June','July','August','September','October','November','December']
if month_name in ('January','March','May','July','August','October','December'):
    print('The number of day: 31 days')
elif month_name=='Febuarary':
    print('The number of days: 28 or 29 days')
elif month_name in ('April','June','September','November'):
    print('The number of days: 30 days')
else:
    print('Error month name')