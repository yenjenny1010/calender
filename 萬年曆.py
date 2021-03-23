print('輸入1進入年曆模式')
print('輸入2進入月曆模式')
print('輸入3進入日曆模式')
mode=eval(input("請輸入查詢模式"))
if mode==1:
    year=eval(input('請輸入年份'))
    month=1
    date=1
    print('進入年曆模式')
elif mode==2:
    year=eval(input('請輸入年份'))
    month=eval(input('請輸入月份'))
    date=1
    print('進入月曆模式')
elif mode==3:
    year=eval(input('請輸入年份'))
    month=eval(input('請輸入月份'))
    date=eval(input('請輸入日期'))
    print('進入日曆模式')

month_day=0
yyear=1582
distinguish=0
j_f_d=5
m_f_d=0
mmonth=1
allmonth=["JAN",'FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

while 1:
    
    if yyear%4==0 and yyear%100==0 and yyear%400==0:
        if month==2:
            month_day=29
        elif month==1 or 3 or 5 or 7 or 8 or 10 or 12:
            month_day=31
        else :
            month_day=30
       
        distinguish=1               #Bissextile Year=1 #Common Year=0
    elif yyear%4==0 and yyear%100==0 :
        if month==2:
            month_day=28
        elif month==1 or 3 or 5 or 7 or 8 or 10 or 12:
            month_day=31
        else :
            month_day=30
        distinguish=0
    elif yyear%4==0:
         if month==2:
            month_day=29
        elif month==1 or 3 or 5 or 7 or 8 or 10 or 12:
            month_day=31
        else :
            month_day=30
        distinguish=1
    else:
        if month==2:
            month_day=28
        elif month==1 or 3 or 5 or 7 or 8 or 10 or 12:
            month_day=31
        else :
            month_day=30
        distinguish=0
    if year==yyear:
        break
    elif distinguish==1:
        j_f_d=j_f_d+2
    else:
        j_f_d=j_f_d+1
    yyear=yyear+1
if month==4 :
    month_day=30
if month==6:
    month_day=30
if month==9 :
    month_day=30
if month==11:
    month_day=30
   
j_f_d%=7
#print(distinguish)
#print(j_f_d)#禮拜幾#print=0 sunday
m_f_d=j_f_d
while 1:
    if mmonth==1:
        m_f_d=m_f_d
    elif mmonth==3 and distinguish==1:
        m_f_d=(m_f_d+29)%7
    elif mmonth==3 :
        m_f_d=(m_f_d+28)%7    
    elif mmonth==5 :
        m_f_d=(m_f_d+30)%7   
    elif mmonth==7 :
        m_f_d=(m_f_d+30)%7   
    elif mmonth==10 :
        m_f_d=(m_f_d+30)%7  
    elif mmonth==12 :
        m_f_d=(m_f_d+30)%7
    elif mmonth==2 or 4 or 6 or 8 or 9 or 11:
        m_f_d=(m_f_d+31)%7
    if mmonth==month:
        break
    else:
        mmonth=mmonth+1

#print(m_f_d)#取得某年某月的第一天是星期幾

if mode==1:
    print("日\t一\t二\t三\t四\t五\t六")
    enter=j_f_d
    for j in range(0,12):
        
        print("\n",allmonth[j],end='\n',sep="")
        print((m_f_d))
        print('\t'*(m_f_d),end="")
        
        for i in range(1,month_day+1):
            print(i,end='\t')
            enter=enter+1
            if enter%7==0:
                print('')

if mode==2:
    print ("日\t一\t二\t三\t四\t五\t六")
    enter=m_f_d
    print('\t'*(m_f_d+1),end="")
    for i in range(1,month_day+1):
        print(i,end='\t')
        enter=enter+1
        if enter%7==0:
            print('')
            
if mode==3:
    print(year,'年',month,'月',date,'日','星期',end='')
    day=(m_f_d+date-1)%7
    if day==1:
        print('一')
    if day==2:
        print('二')
    if day==3:
        print('三')
    if day==4:
        print('四')
    if day==5:
        print('五')
    if day==6:
        print('六')
    if day==0:
        print('日')





































        
