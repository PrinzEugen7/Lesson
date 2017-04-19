#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double dxdt( double x)
{
    double c = 0.001;
    double r = 100;
    double e = 10;
    return (e-x)/r/c;
}

// オイラー法(初期条件x0,  区間[t0, tn])
double eulerMethod(double x0, double t0, double tn, int n)
{
    int i;
    double x, t, h;
    x = x0;
    t = t0;
    h = (tn - t0) /n;
    
    // 漸化式を計算
    for ( i=1; i <= n ; i++){
        x += dxdt(x) * h;
        t = t0 + i*h;
        printf("%f\n", x);
    }
    return x;
}

int main(void)
{
    eulerMethod(0, 0, 1, 100);
    return 0;
}
