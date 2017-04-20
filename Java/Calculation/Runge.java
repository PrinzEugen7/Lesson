import java.util.*;
import java.lang.*;
import java.io.*;

class Runge
{
    double dxdt(double x)
    {
        double c = 0.001;
        double r = 100;
        double e = 10;
        return (e-x)/r/c;
    }

 
    double calc(double x0, double t0, double tn, int n)
    {
        int i;
        double x, t, h, d1, d2, d3, d4;
        x = x0;
        t = t0;
        h = (tn - t0) /n;
    
        // 漸化式を計算
        for ( i=1; i <= n ; i++){
            t = t0 + i*h;
            d1 = dxdt(x);
            d2 = dxdt(x + d1*h*0.5);
            d3 = dxdt(x + d2*h*0.5);
            d4 = dxdt(x + d3*h);
            x += (d1 + 2 * d2 + 2 * d3 + d4)*(h/6.0); 
            System.out.printf("x(%f)=%f\n", t, x);
        }

        return x;
    }
    
    public static void main (String[] args) throws java.lang.Exception
    {
        Runge runge = new Runge();
        // 解を計算(初期値, 収束条件)
        double xn = runge.calc(0, 0, 1, 100);
        // 結果表示
        System.out.printf("x(1.0)=%f\n", xn); // x(1.0)=9.999546
    }
}
