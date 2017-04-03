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
        
        // 表示
        System.out.println(fubuki.name); // 吹雪
        System.out.println(fubuki.type); // 駆逐艦
	}
}

// クラス宣言
class TypeFubuki
{
    // インスタンス変数
    public String name ="艦名";
    public String type ="艦種";
    
    // コンストラクタ(初期化メソッド)
    public TypeFubuki(String srcName, String srcType)
    {
        name = srcName;
        type = srcType;
    }

}
