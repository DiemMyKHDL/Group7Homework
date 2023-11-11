HumanAge= int(input('Enter the number of human years: '))
if HumanAge<0:
    print('error')
elif HumanAge<=2:
    DY=HumanAge*10.5
else:
    DY=2*10.5+(HumanAge-2)*4
print('Dog years:',DY)