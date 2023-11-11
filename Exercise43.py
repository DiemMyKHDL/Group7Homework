MenhGia= int(input('Enter the denomination of the bill: $'))
if MenhGia==1:
    print('The individual that appears on $', MenhGia,' in the United States is: George Washington', sep='')
elif MenhGia==2:
    print('The individual that appears on $', MenhGia, ' in the United States is: Thomas Jefferson', sep='')
elif MenhGia==5:
    print('The individual that appears on $', MenhGia, ' in the United States is: Abraham Lincoln', sep='')
elif MenhGia==10:
    print('The individual that appears on $', MenhGia, ' in the United States is: Alexander Hamilton', sep='')
elif MenhGia==20:
    print('The individual that appears on $', MenhGia, ' in the United States is: Andrew Jackson', sep='')
elif MenhGia==50:
    print('The individual that appears on $', MenhGia, ' in the United States is: Ulysses S. Grant', sep='')
elif MenhGia==100:
    print('The individual that appears on $', MenhGia, ' in the United States is: Benjamin Franklin', sep='')
else:
    print('No person appears on $', MenhGia, sep='')