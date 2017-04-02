import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.List;
import java.util.ArrayList;

class Test
{
    public static void main (String[] args)
    {       
        // 配列の宣言・初期化
        String[] name = {"吹雪", "白雪", "深雪"};
        
        // 逆順に並び替え
        List list = Arrays.asList(name);
        Collections.reverse(list);
        String[] name2 = (String[])list.toArray(new String[3]);
            
        // コンソール出力
        for(String n : name2) System.out.println(n); // 深雪, 白雪, 吹雪 
    }
}
