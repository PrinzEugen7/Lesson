using System;

public class Test
{
	public static void Main()
	{
		// 配列の宣言
		int[] score = new int[] {100, 97, 78};
		
		// 変数の型をチェック
	        Type type = score.GetType();
		
		// 配列ならTrue, 違えばFalse
		System.Console.WriteLine(type.IsArray); // True
	}
}
