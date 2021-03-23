month_day = 0
yyear = 1582
distinguish = 0
j_f_d = 5
m_f_d = 0
initialmonth = 1
allmonth = ["JAN", 'FEB', 'MAR', 'APR', 'MAY',
            'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
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
while 1:
    if yyear % 4 == 0 and yyear % 100 == 0 and yyear % 400 == 0:#leapyear
        if month == 2:
            month_day = 29
        distinguish = 1  # Bissextile Year=1 #Common Year=0
    elif yyear % 4 == 0 and yyear % 100 == 0:#leapyear
        if month == 2:
            month_day = 28
        distinguish = 0
    elif yyear % 4 == 0:
        if month == 2:
            month_day = 29
        distinguish = 1
    else:
        if month == 2:
            month_day = 28
        distinguish = 0
    if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        month_day = 31
    else:
        month_day = 30
    if year == yyear:
        break
    elif distinguish == 1:
        j_f_d = j_f_d+2
    else:
        j_f_d = j_f_d+1
    yyear = yyear+1

if month == 4:
    month_day = 30
if month == 6:
    month_day = 30
if month == 9:
    month_day = 30
if month == 11:
    month_day = 30

j_f_d %= 7
# print(distinguish)
# print(j_f_d)#禮拜幾#print=0 sunday
m_f_d = j_f_d

while 1:

    if initialmonth == 1:
        m_f_d = m_f_d
    elif initialmonth == 3 and distinguish == 1:
        m_f_d = (m_f_d+29) % 7
    elif initialmonth == 3 :
        m_f_d = (m_f_d+28) % 7
    elif initialmonth == (5 or 7 or 10 or 12):
        m_f_d = (m_f_d+30) % 7
    elif initialmonth == 2 or 4 or 6 or 8 or 9 or 11:
        m_f_d = (m_f_d+31) % 7
    if initialmonth == month:
        break
    else:
        initialmonth = initialmonth+1

if mode == 1:
    print("日\t一\t二\t三\t四\t五\t六")
    enter = j_f_d
    for j in range(0, 12):

        print("\n", allmonth[j], end='\n', sep="")
        print('\t'*(m_f_d), end="")

        for i in range(1, month_day+1):
            print(i, end='\t')
            enter = enter+1
            if enter % 7 == 0:
                print('')
if mode == 2:
    print("日\t一\t二\t三\t四\t五\t六")
    enter = m_f_d
    print('\t'*(m_f_d+1), end="")
    for i in range(1, month_day+1):
        print(i, end='\t')
        enter = enter+1
        if enter % 7 == 0:
            print('')
if mode == 3:
    print(year, '年', month, '月', date, '日', '星期', end='')
    day = (m_f_d+date-1) % 7
    print(allday[day-1])
