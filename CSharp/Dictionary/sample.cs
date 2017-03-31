using System;
using System.Collections.Generic;

public class Test
{
	public static void Main()
	{
      // Dictionaryクラスのオブジェクトを生成
      Dictionary<string, int> DictData = new Dictionary<string, int>();
 
      // (キー, 値)を設定
      DictData.Add("吹雪", 1);
      DictData.Add("白雪", 2);
      DictData.Add("深雪", 3);
 
      // キーから値を取り出して表示
      System.Console.WriteLine( DictData["吹雪"] ); // 1

	}
}
