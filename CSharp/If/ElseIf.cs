using System;
using System.Collections.Generic;

public class Test
{
    public static void Main()
    {
        var x = 1;
          
        if(x > 3){
            Console.WriteLine("xは3より大きい\n");
        }
        else if(x > 2){
            Console.WriteLine("xは2より大きい\n");
        }
        else if(x > 1){
            Console.WriteLine("xは1より大きい\n");
        }
        else {
            Console.WriteLine("xは1以下だ\n"); // xは1以下だ
        }
    }
}
