using System;

public class Test
{
	public static void Main()
	{
		var str = "伊勢,日向,武蔵";

        var array = str.Split(',');
        
        foreach (var a in array) Console.WriteLine(a); // 伊勢 日向 武蔵


	}
}
