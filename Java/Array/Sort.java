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
        	int[] score = {100, 51, 72};
            
            
            Arrays.sort(score);
            
            // コンソール出力
            for(int a : score) System.out.println(a); // 51, 72, 100
        }
}
