using System;

// クラス定義
public class TypeFubuki
{
	// インスタンス変数
    public string name ="艦名";
    public string type ="艦種";
    
    // コンストラクタ(初期化メソッド)
    public TypeFubuki(string name, string type)
    {
        this.name = name;
        this.type = type;
    }
    
    // メソッド定義
    public void Print()
    {
        // 表示
        System.Console.WriteLine(this.type + ":" + this.name);
    }
}

public class Test
{
        public static void Main()
        {
                // インスタンス生成
                TypeFubuki fubuki = new TypeFubuki("吹雪", "駆逐艦");
                
                // メソッド呼び出し
                fubuki.Print(); // 駆逐艦:吹雪

        }
}
