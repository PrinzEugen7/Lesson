import java.util.*;
import java.lang.*;
import java.io.*;
 
class Main
{
    public static void main( String[] args ) {
        // 変数宣言
        int x = 1;
          
        if(x > 3){
            System.out.println("xは3より大きい\n");
        }
        else if(x > 2){
            System.out.println("xは2より大きい\n");
        }
        else if(x > 1){
            System.out.println("xは1より大きい\n");
        }
        else {
            System.out.println("xは1以下だ\n"); // xは1以下だ
        }

    }
}
