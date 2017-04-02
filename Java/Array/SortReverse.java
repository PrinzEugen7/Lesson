import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Arrays;

class Test
{
        public static void main (String[] args)
        {       
        	// 配列の宣言・初期化
        	Integer score[] = {100, 51, 72};
            
            
            Arrays.sort(score, Comparator.reverseOrder());
            
            // コンソール出力
            for(int a : score) System.out.println(a); // 100, 72, 51
        }
}
