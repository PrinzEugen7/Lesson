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
        
        // コンソール出力
        System.out.println(fubuki.name); // 吹雪
	}
}

// クラス宣言
class TypeFubuki
{
    // インスタンス変数
    public String name = "吹雪";
 
}
