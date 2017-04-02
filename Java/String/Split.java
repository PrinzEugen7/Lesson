import java.util.*;
import java.lang.*;
import java.io.*;

class Test
{
        public static void main (String[] args)
        {       
        	// 変数宣言
        	String str ="沖田,武蔵,モードレッド";
        	    
        	String[] array = str.split(",");
        	    
        	// コンソール出力
                System.out.println(array[0]); // 沖田
                System.out.println(array[1]); // 武蔵
                System.out.println(array[2]); // モードレッド
        }
}
