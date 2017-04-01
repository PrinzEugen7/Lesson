using System;

// クラス定義
public class TypeFubuki
{
	// インスタンス変数
    public string name ="吹雪";
}

public class Test
{
        public static void Main()
        {
                // インスタンス生成
                TypeFubuki fubuki = new TypeFubuki();
                
                // 表示
                System.Console.WriteLine(fubuki.name); // 吹雪

        }
}

