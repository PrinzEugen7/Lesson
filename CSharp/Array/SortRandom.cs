using System;
using System.Linq;

public class Test
{
	public static void Main()
	{
		// 配列の宣言
        var array = new[] { 3, 2, 5, 4, 1 };

        // ランダムソート
        var array2 = array.OrderBy(i => Guid.NewGuid()).ToArray();
        
        // 配列の中身表示
        foreach (var a2 in array2) Console.WriteLine(a2); // 5, 4, 1, 2, 3
	}
}
