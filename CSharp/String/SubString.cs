using System;

public class Test
{
	public static void Main()
	{
		// 文字列宣言
		var str = "沖田武蔵モードレッド";
		
		// 文字抽出
		var s1 = str.Substring(2, 2);
		var s2 = str.Substring(2);		
		// 表示
		System.Console.WriteLine(s1); // 武蔵
		System.Console.WriteLine(s2); // 武蔵モードレッド
	}
}
