#include <stdio.h>
#include <iostream>
using namespace std;
int initial_year = 1582;
int january_first_day = 5;
int month_first_day = 0;
int month_day = 0;
int distinguish;
int month;
int year;
int initialmonth = 1;
int mode;
int date;

string allmonth[12] = {"JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"};
string allday[7] = {"一", "二", "三", "四", "五", "六", "日"};
int function_january_first_day(int year)
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
int function_month_first_day()
{
    while (1)
    {
        initialmonth = 1;
        while (1)
        {
            if (initialmonth == 1)
            {
                month_first_day = january_first_day;
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
            if (initialmonth == month)
                break;
            else
                initialmonth = initialmonth + 1;
        }
        break;
    }
    return month_first_day;
}
int main()
{
    cout << "輸入1進入年曆模式\n輸入2進入月曆模式\n輸入3進入日曆模式" << endl;
    cout << "請輸入查詢模式" << endl;
    cin >> mode;
    if (mode == 1)
    {
        cout << "請輸入年份" << endl;
        cin >> year;
        month = 1;
        date = 1;
        cout << "進入年曆模式";
    }
    else if (mode == 2)
    {
        cout << "請輸入年份" << endl;
        cin >> year;
        cout << "請輸入月份" << endl;
        cin >> month;
        date = 1;
        cout << "進入月曆模式";
    }
    else if (mode == 3)
    {
        cout << "請輸入年份" << endl;
        cin >> year;
        cout << "請輸入月份" << endl;
        cin >> month;
        cout << "請輸入年份" << endl;
        cin >> date;
        cout << "進入月曆模式";
    }

    january_first_day = function_january_first_day(year);
    month_first_day = function_month_first_day();
    if (mode == 1)
    {
        int enter = january_first_day;
        cout << "\t" * 5 << "======" << year << "======" << endl;
        for (int j = 1; j < 13; j++)
        {
            cout << "\n"
                 << "------------------------" << allmonth[j] << "------------------------" << endl;
            cout << "SUN\tMON\tTUS\tWED\tTHU\tFRI\tSAT" << endl;
            cout << "\t" * (function_month_first_day()) << endl;
            enter = function_month_first_day();
            for (int i = 1; i < month_day + 1; i++)
            {
                cout << i << "\t";
                enter = enter + 1;
                if (enter % 7 == 0)
                    cout << "" << endl;
            }
        }
    }
    if (mode == 2)
    {
        cout << "\n"
             << "------------------------" << allmonth[month] << "------------------------"
             << "\n"
             << endl;
        cout << "SUN\tMON\tTUS\tWED\tTHU\tFRI\tSAT" << endl;
        int enter = month_first_day;
        cout << "\t" * (month_first_day) << "" << endl;
        for (int i = 1; i < month_day + 1; i++)
        {
            cout << i << "\t" << endl;
            enter = enter + 1;
            if (enter % 7 == 0)
            {
                cout <<"\n" << endl;
            }
        }
    }
    if (mode == 3)
    {
        cout << year << "年" << month << "月" << date << "日"
             << "星期" << endl;
        int day = (month_first_day + date - 1) % 7;
        cout << allday[day - 1];
    }
}
