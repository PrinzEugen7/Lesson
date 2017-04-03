import java.util.*;
import java.lang.*;
import java.io.*;

// メイン
class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// インスタンス生成
        TypeFubuki fubuki = new TypeFubuki();
        
        // 代入
        fubuki.name = "吹雪";
        fubuki.type = "駆逐艦";

	}
}

// クラス宣言
class TypeFubuki
{
    // インスタンス変数
    public String name ="艦名";
    public String type ="艦種";
}
