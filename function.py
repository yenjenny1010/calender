
'''import calendar 
c = calendar.TextCalendar(calendar.SUNDAY) 
c.prmonth(1582, 10)
'''
'''
import numpy as np
calender=np.zeros((5,7))
monthday=[0,31,28,31]
month_first_day=1
enter = month_first_day

while 1:
    for l in range(1,3):#一到二月
        monthtotalday=monthday[l]
        for i in range(0,month_first_day):
            k=0
            calender[k,i]=0
        for i in range(1,monthtotalday+1):
            calender[k,enter % 7]=i
            enter=enter+1
            print("k",k,"enter",enter%7,i)
            if (enter) % 7 == 0:
                k+=1
        print (calender)
    break

            


'''
'''for i in range(1, month_day+1):
        print(i, end='\t')
        enter = enter+1
        if enter % 7 == 0:
            print('')'''
'''
month = eval(input('請輸入月份'))
distinguish=1
while 1:
    monthtotalday=[0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if distinguish == 1:
        monthtotalday[2]=29
    initialmonth = 1
    
    while 1 :
        if initialmonth == 1:
            month_first_day = month_first_day
        else:
            month_first_day = (month_first_day+monthtotalday[initialmonth]) % 7
        '''
'''elif initialmonth == 3 :
            month_first_day = (month_first_day+28) % 7
        elif initialmonth == 5 or initialmonth == 7 or initialmonth ==10 or initialmonth ==12:
            month_first_day = (month_first_day+30) % 7
        elif initialmonth == 2 or initialmonth == 4 or initialmonth == 6 or initialmonth == 8 or initialmonth ==9 or initialmonth ==11:
            month_first_day = (month_first_day+31) % 7'''
'''
        if initialmonth == month:
            break
        else:
            initialmonth = initialmonth+1
    break
'''
