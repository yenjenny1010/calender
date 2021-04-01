#include <stdio.h>
#include <iostream>
using namespace std;
int initial_year = 1582;
int january_first_day = 5;
double month_first_day = 0;
double month_day = 0;
double distinguish;
int month = 5;
int year = 2021;
string allmonth[12] = {"JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"};
string allday[7] = {"一", "二", "三", "四", "五", "六", "日"};
int function_january_first_day()
{
    while (1)
    {
        if (initial_year % 4 == 0 && initial_year % 100 == 0 && initial_year % 400 == 0)
        { //leapyear
            distinguish = 1;
        }
        else if (initial_year % 4 == 0 && initial_year % 100 == 0)
        { //leapyear
            distinguish = 0;
        }
        else if (initial_year % 4 == 0)
        {
            distinguish = 1;
        }
        else
            distinguish = 0; //判斷平閏年# Bissextile Year=1 //Common Year=0

        if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12)
        {
            month_day = 31;
        }
        else if (month == 2)
        {
            if (distinguish == 0)
                month_day = 28;
            else
                month_day = 29;
        }
        else
            month_day = 30;
        if (year == initial_year)
            break;
        else if (distinguish == 1)
            january_first_day = (january_first_day + 2) % 7;
        else
            january_first_day = (january_first_day + 1) % 7;
        initial_year = initial_year + 1;
        return january_first_day;
    }
}
    int function_month_first_day(month) 
    {
        while (1)
        {
            initialmonth = 1;
            while (1)
            {
                if (initialmonth == 1)
                {
                    month_first_day = january_first_day
                }
                else if (initialmonth == 3 and distinguish == 1)
                    month_first_day = (month_first_day + 29) % 7;
                else if (initialmonth == 3)
                {
                    month_first_day = (month_first_day + 28) % 7;
                }
                else if (initialmonth == 5 || initialmonth == 7 || initialmonth == 10 || initialmonth == 12)
                    month_first_day = (month_first_day + 30) % 7;
                else
                    month_first_day = (month_first_day + 31) % 7;
                if initialmonth== month 
                    break;
                else
                    initialmonth = initialmonth + 1;
            }
            break;
        }
        return month_first_day  ;
        }
/*
print("輸入1進入年曆模式\n輸入2進入月曆模式\n輸入3進入日曆模式")
mode = eval(input("請輸入查詢模式"))
if mode == 1:
    year = eval(input("請輸入年份"))
    month = 1
    date = 1
    print("進入年曆模式")
elif mode == 2:
    year = eval(input("請輸入年份"))
    month = eval(input("請輸入月份"))
    date = 1
    print("進入月曆模式")
elif mode == 3:
    year = eval(input("請輸入年份"))
    month = eval(input("請輸入月份"))
    date = eval(input("請輸入日期"))
    print("進入日曆模式")

january_first_day=function_january_first_day(year)
month_first_day=function_month_first_day (year,month)
if mode == 1:
    enter = january_first_day
    print("\t"*5,"======",year,"======")
    for j in range(1, 13):
        print("\n","------------------------",allmonth[j],"------------------------", end="\n", sep="")
        print("SUN\tMON\tTUS\tWED\tTHU\tFRI\tSAT")
        print("\t"*(function_month_first_day(year,j)), end="")
        enter = function_month_first_day(year,j)
        for i in range(1, month_day+1):
            print(i, end="\t")
            enter = enter+1
            if enter % 7 == 0:
                print("")
if mode == 2:
    print("\n","------------------------",allmonth[month],"------------------------", end="\n", sep="")
    print("SUN\tMON\tTUS\tWED\tTHU\tFRI\tSAT")
    enter = month_first_day
    print("\t"*(month_first_day), end="")
    for i in range(1, month_day+1):
        print(i, end="\t")
        enter = enter+1
        if enter % 7 == 0:
            print("")
if mode == 3:
    print(year, "年", month, "月", date, "日", "星期", end="")
    day = (month_first_day+date-1) % 7
    print(allday[day-1])
    */