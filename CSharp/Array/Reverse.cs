using System;
using System.Collections.Generic;

public class Test
{
	public static void Main()
	{
            // 配列の宣言
            string[] datas = {"沖田", "武蔵", "モードレッド"};
        
            // 配列の要素順序を反転
            Array.Reverse(datas);
        
	    // 配列の中身を表示
	    System.Console.WriteLine(datas[0]); // モードレッド
	    System.Console.WriteLine(datas[1]); // 武蔵
	    System.Console.WriteLine(datas[2]); // 沖田
	}
}
