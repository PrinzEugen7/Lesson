using System;

public class Test
{
        public static void Main()
        {
                // 文字列宣言
                string str = "沖田";
                
                // ローカル関数
                int myFunc(string x) {
                   System.Console.WriteLine(str);
                   System.Console.WriteLine(x);
                   return 0;
                };
                
                // ローカル関数の呼び出し
                myFunc("武蔵");

        }
}
