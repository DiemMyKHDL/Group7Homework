Decibels= int(input('Enter a number of decibels: '))
if Decibels == 130:
    print('Jackhammer')
elif 106<Decibels<130:
    print('The noise level is between gaslawnmower and jackhammer')
elif Decibels == 106:
    print('Gaslawnmower')
elif 70<Decibels<106:
    print('The noise level is between gaslawnmower and alarm clock')
elif Decibels == 70:
    print('Alarm clock')
elif 40<Decibels<70:
    print('The noise level is between quiet room and alarm clock')
elif Decibels == 40:
    print('Quiet room')
elif Decibels < 40:
    print('The noise level is too low to be heard')
else:
    print('The noise level is too loud to be heard')