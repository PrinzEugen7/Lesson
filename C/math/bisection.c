#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// 計算する関数
double f(double x)
{
    return x*x*x-3*x*x+9*x-8;
}

// 2分法
void bisection(double a, double b, double eps, double *solution, int *N)
{
    int i = 0;
    double s;

    // 解が収束条件を満たせば終了
    while (!(abs(a-b)<eps)){
        i++;
        s = (a+b)/2.0;
        if(f(s) * f(a)<0) b=s;
        else a = s;
        if(i==1000) break; // 1000回繰り返したら強制終了
    };
    *N = i; 
    *solution = s; 
}



int main()
{
    double solution;
    int N;
    // 2分法
    bisection(0.0, 2.0, 1.0e-5, &solution, &N);

    printf("解:%f (繰り返し回数：%d )",solution,N); // 解:1.165901 (繰り返し回数：18 )

    return 0;
}
