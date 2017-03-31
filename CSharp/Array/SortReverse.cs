using System;

public class Test
{
	public static void Main()
	{
		// 配列の宣言
        var array1 = new[] { 3, 2, 5, 4, 1 };
        var array2 = new[] { "c", "d", "a", "e", "b"};

        // 昇順ソート
        Array.Sort(array1);
        Array.Sort(array2);
        
        // 配列の反転
        Array.Reverse(array1);
        Array.Reverse(array2);
        
        // 配列の中身表示
        foreach (var a1 in array1) Console.WriteLine(a1); // 5, 4, 3, 2, 1
        foreach (var a2 in array2) Console.WriteLine(a2); // e, d, c, b, a
	}
}
