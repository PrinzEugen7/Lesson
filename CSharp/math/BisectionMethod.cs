using System;

public class BisectionMethod
{
    double f(double x)
    {
        return x*x*x-3*x*x+9*x-8;
    }

    double calc(double a, double b, double eps)
    {
        int i=0;
        double s = 0;
 
        while(!(Math.Abs(a-b)<eps)) {
            i++;
            s = (a+b)/2.0;
            if(f(s) * f(a)<0) b = s;
            else a = s;
            if(i==1000) break; // 1000回繰り返したら強制終了

        }
        return s; 
    }

    public static void Main()
    {
        BisectionMethod bm = new BisectionMethod();
        // 解を計算(初期値, 収束条件)
        double s = bm.calc(0.0, 4.0, 0.0001);
        // 結果表示
        System.Console.WriteLine(s); // 解：1.16595458984375
    }
}
