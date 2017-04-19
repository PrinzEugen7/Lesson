using System;

public class Euler
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
        double x, t, h;
        x = x0;
        t = t0;
        h = (tn - t0) /n;
    
        // 漸化式を計算
        for ( i=1; i <= n ; i++){
            x += dxdt(x) * h;
            t = t0 + i*h;
            System.Console.WriteLine(x);
        }
        return x;
    }
    
    public static void Main()
    {
        Euler euler = new Euler();
        // 解を計算(初期値, 収束条件)
        double xn = euler.calc(0, 0, 1, 100);
        // 結果表示
        System.Console.WriteLine(xn); // x(1)=9.99973438601112
    }
}

