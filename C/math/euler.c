include <stdio .h>
include <stdlib .h>
include <math.h>

double dxdt( double x)
{
    double c=;
    double r=;
    double e=;
    return (e-x)/r/c;
}

int main(void)
{
    int i, n;
    double x, t, h, v0 , t0 , tn;

    x = x0;
    t = t0;
    h = (tn - t0) /n;
    for ( i=1; i <= n ; i++){
        x += dxdt(x) * h;
        t = t0 + i*h;
    }
    return 0;
}
