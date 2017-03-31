using System;

public class Test
{
    public static void Main()
    {
        // 配列の宣言
        string[] datas = {"沖田", "武蔵", "モードレッド"};

        // 配列内の各要素を">"で区切って連結
        string data = string.Join(">", datas);
		
		    // 変数の中身を表示
		    System.Console.WriteLine(data); // 沖田>武蔵>モードレッド
	  }
}
