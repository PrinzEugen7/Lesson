using System;
using System.Collections.Generic;

public class Test
{
    public static void Main()
    {
        // Dictionaryクラスのオブジェクトを生成
        Dictionary<string, int> dict = new Dictionary<string, int>();
 
        // (キー, 値)を設定
        dict.Add("c", 3);
        dict.Add("b", 2);
        dict.Add("a", 1);
        
        // 連想配列をキーで昇順ソート
        SortedDictionary<string, int> dict2 = new SortedDictionary<string, int>(dict);
        
        // キーを表示
        foreach (KeyValuePair<string, int> d in dict2) Console.WriteLine(d.Key); // a, b, c
    }

}
