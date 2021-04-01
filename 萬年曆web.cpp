#include <stdio.h>
using namespace std;
int main(void)
{
    int a, i, j, n, k, t, w, x, y, z;
    static int d[13][78];
    int m[14] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    char wst[] = " Sun Mon Yue Wed Thu Fri Sat   ";
    printf("Please enter the year: ");
    scanf("%d", &y);

    if(y%4==0 && y%100!=0 || y%400==0)  /*閏年的二月為29天*/
        m[2] = 29;
    w = (y+(y-1)/4-(y-1)/100+(y-1)/400)%7; /*計算y年元旦為星期w*/
    for(i=1; i<=12; i++)
    {
        a = 1;
        for(j=1; j<=6; j++)
        {
            for(k=0; k<=6; k++)
            {
                while(k<w) k=k+1;
                d[i][j*10+k] = a;  /*計算i月的第j個星期的星期w的日期為a*/
                a=a+1;
                w = k+1;
                if(w==7) w=0;
                if(a>m[i]) break;
            }
            if(a>m[i]) break;
        }
    }
    printf("input x(1,2,3,4,5,6): ");
    scanf("%d", &x);
    for(k=1; k<=16*x-3; k++)
        printf(" ");
    printf("=====%d=====\n", y);   /*列印年號*/
    for(n=1; n<=12/x; n++)
    {
        t = x*(n-1)+1;
        printf("\n    ");
        for(z=1; z<=x; z++)
        {
            for(k=1; k<=15; k++)
                printf(" ");
            printf("%2d", t+z-1);   /*列印月號*/
            for(k=1; k<=14; k++)
                printf(" ");
        }
        printf("\n      ");
        for(z=1; z<=x; z++)      /*按一橫排x個月格式列印*/
            printf("%s", wst);   /*列印星期標題*/
        for(j=1; j<=6; j++)
        {
            printf("\n  ");
            for(i=t; i<=t+x-1; i++)
            {
                printf("   ");
                for(k=0; k<=6; k++)
                    if(d[i][j*10+k]==0) /*空缺日期位置列印空格*/
                        printf("    ");
                    else
                        printf("%4d", d[i][j*10+k]);/*列印日期*/
            }
        }
    }

    return 0;
}