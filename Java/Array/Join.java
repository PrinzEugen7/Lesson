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
            
            
        String str = String.join(",", name);
            
        // コンソール出力
        System.out.println(str); // 吹雪,白雪,深雪
    }
}
