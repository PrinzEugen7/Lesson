import java.util.*;
import java.lang.*;
import java.io.*;

// メイン
class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// インスタンス生成
        TypeFubuki fubuki = new TypeFubuki("吹雪", "駆逐艦");
        
        // メソッド呼び出し
        fubuki.print(); // 駆逐艦:吹雪
	}
}

// クラス宣言
class TypeFubuki
{
    // インスタンス変数
    public String name ="艦名";
    public String type ="艦種";
    
    // コンストラクタ(初期化メソッド)
    public TypeFubuki(String name, String type)
    {
        this.name = name;
        this.type = type;
    }
    
    // メソッド定義
    public void print()
    {
        // 表示
        System.out.println(this.type + ":" + this.name);
    }

}
