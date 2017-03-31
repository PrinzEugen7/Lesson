using System;
using System.Collections.Generic;

public class Test
{
    public static void Main()
    {
        var i = 1;
          
        do{
            Console.WriteLine(i); // 1, 2, 3, 4, 5
            i++;    // i = i + 1;と同じ
        } while(i <= 5);

    }
}
