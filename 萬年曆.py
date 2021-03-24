month_day = 0
initial_year = 1582
distinguish = 0
january_first_day = 5
month_first_day = 0
initialmonth = 1
allmonth = ["JAN", 'FEB', 'MAR', 'APR', 'MAY','JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
allday=['一','二','三','四','五','六','日']
print('輸入1進入年曆模式')
print('輸入2進入月曆模式')
print('輸入3進入日曆模式')
mode = eval(input("請輸入查詢模式"))
if mode == 1:
    year = eval(input('請輸入年份'))
    month = 1
    date = 1
    print('進入年曆模式')
elif mode == 2:
    year = eval(input('請輸入年份'))
    month = eval(input('請輸入月份'))
    date = 1
    print('進入月曆模式')
elif mode == 3:
    year = eval(input('請輸入年份'))
    month = eval(input('請輸入月份'))
    date = eval(input('請輸入日期'))
    print('進入日曆模式')
while 1:#找到distinguish值和
    if initial_year % 4 == 0 and initial_year % 100 == 0 and initial_year % 400 == 0:#leapyear
        distinguish = 1  
    elif initial_year % 4 == 0 and initial_year % 100 == 0:#leapyear
        distinguish = 0
    elif initial_year % 4 == 0:
        distinguish = 1
    else:
        distinguish = 0 #判斷平閏年# Bissextile Year=1 #Common Year=0 
    if month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12:
        month_day = 31
    elif month==2:
        if  distinguish == 0:
            month_day = 28
        else:
            month_day = 29
    else:
        month_day = 30
    if year == initial_year:
        break
    elif distinguish == 1:
        january_first_day = (january_first_day+2)%7
    else:
        january_first_day = (january_first_day+1)%7
    initial_year = initial_year+1

month_first_day = january_first_day

while 1:

    if initialmonth == 1:
        month_first_day = month_first_day
    elif initialmonth == 3 and distinguish == 1:
        month_first_day = (month_first_day+29) % 7
    elif initialmonth == 3 :
        month_first_day = (month_first_day+28) % 7
    elif initialmonth == 5 or initialmonth == 7 or initialmonth ==10 or initialmonth ==12:
        month_first_day = (month_first_day+30) % 7
    elif initialmonth == 2 or initialmonth == 4 or initialmonth == 6 or initialmonth == 8 or initialmonth ==9 or initialmonth ==11:
        month_first_day = (month_first_day+31) % 7
    if initialmonth == month:
        break
    else:
        initialmonth = initialmonth+1
if mode == 1:
    print("日\t一\t二\t三\t四\t五\t六")
    enter = january_first_day
    for j in range(0, 12):

        print("\n", allmonth[j], end='\n', sep="")
        print('\t'*(month_first_day), end="")

        for i in range(1, month_day+1):
            print(i, end='\t')
            enter = enter+1
            if enter % 7 == 0:
                print('')
if mode == 2:
    print("日\t一\t二\t三\t四\t五\t六")
    enter = month_first_day
    print('\t'*(month_first_day), end="")
    for i in range(1, month_day+1):
        print(i, end='\t')
        enter = enter+1
        if enter % 7 == 0:
            print('')
if mode == 3:
    print(year, '年', month, '月', date, '日', '星期', end='')
    day = (month_first_day+date-1) % 7
    print(allday[day-1])
