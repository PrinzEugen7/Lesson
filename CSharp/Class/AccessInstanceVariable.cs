using System;

// クラス定義
public class TypeFubuki
{
	// インスタンス変数
    public string name ="艦名";
    public string type ="艦種";
}

public class Test
{
        public static void Main()
        {
                // インスタンス生成
                TypeFubuki fubuki = new TypeFubuki();
                
                // 代入
                fubuki.name = "吹雪";
                fubuki.type = "駆逐艦";
        }
}
