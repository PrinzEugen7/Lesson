using System;
 
public class Test
{
    public static void Main()
    {
        // 配列の宣言
        var array = new[] { 1, 2, 3, 4, 5 };
 
 
        foreach (var a in array){
            Console.WriteLine(a); // 1, 2, 3, 4, 5
        }
 
    }
}
