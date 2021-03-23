month_day = 0
initialyear = 1582
distinguish = 0
j_f_d = 5
m_f_d = 0
mmonth = 1
year = eval(input("請輸入年"))
month = eval(input("請輸入月"))
allmonth = ["JAN", 'FEB', 'MAR', 'APR', 'MAY',
            'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']


def everymonthfirstday(year, month):
    month_day = 0
    yyear = 1582
    distinguish = 0  # 判斷LEAF YEAR
    j_f_d = 5  # 一月的第一天
    m_f_d = 0  # 每個月的第一天
    mmonth = 1  # 預設值
    while 1:
        if initial_month % 4 == 0 and initial_month % 100 == 0 and initial_month % 400 == 0:  # leapyear
            distinguish = 1
        elif initial_month % 4 == 0 and initial_month % 100 == 0:  # leapyear
            distinguish = 0
        elif initial_month % 4 == 0:
            distinguish = 1
        else:
            distinguish = 0  # 判斷平閏年# Bissextile Year=1 #Common Year=0
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            month_day = 31
        elif month == 2 and distinguish == 0:
            month_day = 28
        elif month == 2 and distinguish == 1:
            month_day = 29
        else:
            month_day = 30
        if year == initial_month:
            break
        elif distinguish == 1:
            january_first_day = (january_first_day+2) % 7
        else:
            january_first_day = (january_first_day+1) % 7
        initial_month = initial_month+1


month_first_day = january_first_day

while 1:

    if initialmonth == 1:
        month_first_day = month_first_day
    elif initialmonth == 3 and distinguish == 1:
        month_first_day = (month_first_day+29) % 7
    elif initialmonth == 3:
        month_first_day = (month_first_day+28) % 7
    elif initialmonth == (5 or 7 or 10 or 12):
        month_first_day = (month_first_day+30) % 7
    elif initialmonth == 2 or 4 or 6 or 8 or 9 or 11:
        month_first_day = (month_first_day+31) % 7
    if initialmonth == month:
        break
    else:
        initialmonth = initialmonth+1
