using System;

public class Test
{
	public static void Main()
	{
		// 文字列宣言
		var str = "沖田武蔵モードレッド";
		
		// 文字抽出
		var s = str.Substring(2, 2);
		
		// 表示
		System.Console.WriteLine(s);
	}
}
