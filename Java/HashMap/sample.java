import java.util.*;
import java.lang.*;
import java.io.*;

class Test
{
    public static void main (String[] args)
    {       
        // オブジェクト生成
        HashMap<String,Integer> data = new HashMap<String,Integer>();
            
        // キーと値をセット 
        data.put("吹雪", 1);
        data.put("白雪", 2);
            
        // キーから値を取り出し
        System.out.println(data.get("吹雪")); // 1
    }
}
