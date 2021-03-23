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


'''def everymonthfirstday(year, month):
    month_day = 0
initial_year = 1582
distinguish = 0
january_first_day = 5
month_first_day = 0
initialmonth = 1'''
year = eval(input('請輸入年份'))
month = eval(input('請輸入月份'))
date = eval(input('請輸入日期'))
def distinguish_leapyear(year):
    distinguish = 0
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:#leapyear
        distinguish = 1  
    elif year % 4 == 0 and year % 100 == 0:#leapyear
        distinguish = 0
    elif year % 4 == 0:
        distinguish = 1
    else:
        distinguish = 0 #判斷平閏年# Bissextile Year=1 #Common Year=0 
    return distinguish
print(distinguish_leapyear(year))


 #if month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12:
        #month_day = 31
    #elif month==2 and distinguish == 0:
        #month_day = 28
    #elif month==2 and distinguish == 1:
        #month_day = 29
    #else:
        #month_day = 30
    #if year == initial_year:
        #break
    #elif distinguish == 1:
        #january_first_day = (january_first_day+2)%7
    #else:
        #january_first_day = (january_first_day+1)%7
    #initial_year = initial_year+1'''

#month_first_day = january_first_day   