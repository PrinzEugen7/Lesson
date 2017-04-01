using System;

// クラス定義
public class TypeFubuki
{
	// インスタンス変数
    public string name ="艦名";
    public string type ="艦種";
    // コンストラクタ(初期化メソッド)
    public TypeFubuki(string srcName, string srcType)
    {
        name = srcName;
        type = srcType;
    }
}

public class Test
{
        public static void Main()
        {
                // インスタンス生成
                TypeFubuki fubuki = new TypeFubuki("吹雪", "駆逐艦");
                // 表示
                System.Console.WriteLine(fubuki.name); // 吹雪
                System.Console.WriteLine(fubuki.type); // 駆逐艦
        }
}
