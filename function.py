month_day = 0
distinguish = 0
month_first_day = 0
mmonth = 1
allmonth = ["JAN", 'FEB', 'MAR', 'APR', 'MAY',
            'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

'''month_day = 0
initial_year = 1582
distinguish = 0
january_first_day = 5
month_first_day = 0
initialmonth = 1'''

year = eval(input('請輸入年份'))
month = eval(input('請輸入月份'))
#date = eval(input('請輸入日期'))


def function_month_first_day (year,month):
    global initial_year , january_first_day , month_first_day , month_day , distinguish 
    initial_year=1582
    january_first_day = 5
    month_first_day = 0
    month_day = 0
    while 1:
        distinguish = 0
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
        month_first_day=january_first_day
    
    
    while 1:
        initialmonth = 1
        while 1 :
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
        break
            
       
    return month_first_day  




'''def function_month_first_day(month):
    while 1:
        initialmonth = 1
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
    return month_first_day'''
