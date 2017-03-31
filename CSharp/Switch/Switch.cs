using System;
using System.Collections.Generic;

public class Test
{
    public static void Main()
    {
        var i = 1;
          
        switch (i)
        {
            case 1:
            Console.WriteLine("iは1です。\n"); // iは1です。
            break;
            
            case 2:
            Console.WriteLine("iは2です。\n");
            break;
            
            case 3:
            Console.WriteLine("iは3です。\n");
            break;
            
            default:
            Console.WriteLine("iは1～3以外です。");
            break;
        }

    }
}

