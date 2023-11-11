a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
import math
if (a==b) and (a==c) and (b==c):
    print('The type of triangle: equilateral')
elif (a==b) or (a==c) or (b==c):
    print('The type of triangle: isoscelet')
else:
    print('The type of triangle: scalene')