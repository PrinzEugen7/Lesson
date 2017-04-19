include <stdio.h>
include <stdlib.h>
include <math.h>

double dxdt( double x)
{
    double c = 0.001;
    double r = 100;
    double e = 10;
    return (e-x)/r/c;
}

int main(void)
{
    int i, n;
    double x, t, h;
    double x0=0, t0=0, tn=1;
    x = x0;
    t = t0;
    h = (tn - t0) /n;
    for ( i=1; i <= n ; i++){
        x += dxdt(x) * h;
        t = t0 + i*h;
    }
    return 0;
}
