
'''import calendar 
c = calendar.TextCalendar(calendar.SUNDAY) 
c.prmonth(1582, 10)
'''

import numpy as np
calender=np.zeros((5,7))
monthday=[0,31,28,31]
month_first_day=1
enter = month_first_day

while 1:
    for l in range(1,2):#一到二月
        monthtotalday=monthday[l]
        for i in range(0,month_first_day):
            k=0
            calender[k,i]=0
        for i in range(1,monthtotalday+1):
            calender[k,enter % 7]=i
            enter=enter+1
            if (enter) % 7 == 0:
                k+=1
        print(calender)
    break
enter=1
print('\t'*(month_first_day),end="")
for i in range(5):
    print("")
    print(enter,".")
    for j in range(7):#j是行列所以7
        if enter%7==0:
            print("",sep="")
        if calender[i,j]==0:
            print(" ",end="")
        else:
            print("%5s" % int(calender[i,j]),end="")
        enter+=1
print(enter)
