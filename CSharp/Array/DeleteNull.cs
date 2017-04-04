using System;
using System.Linq;
using System.Collections.Generic;

public class Test
{
        public static void Main()
        {
        // 配列の宣言
        var array = new[] {"沖田", null, "モードレッド"};
        
        // 配列→リスト 
        List<string> list = new List<string>(array);
        
        // 空要素(null)を削除
        list.Remove(null);
        
        // リスト→配列
        var array2 = list.ToArray();
        
        // 配列の中身表示
        foreach (var a2 in array2) Console.WriteLine(a2); // 沖田, モードレッド
        }
}
