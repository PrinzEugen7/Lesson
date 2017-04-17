#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 
double f(double x)
{
    return x*x - 4;
}
 
double df(double x)
{
    return 2*x;
}
 
void newtonMethod(double a, double eps, double *result, double *num)
{
    int i=0;
    double ah;
 
    while(i<1000) {
        i++;
        ah = a - f(a)/df(a);
        // 収束条件を満たせばループ終了
        if(abs(ah - a)<eps) break;
        a = ah;
    }
    *result = a;
    *num = i; 
}
 
 
int main()
{
    double result;
    int num;
 
    // ニュートン法(初期値, 収束条件)
    newtonMethod(1.0, 1.0e-5, &result, &num);
 
    // 結果表示
    printf("解：%f(収束回数%d)回\n", result, num); // 解：2.000000(収束回数0)回
 
    return 0;
}
