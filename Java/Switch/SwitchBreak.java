import java.util.*;
import java.lang.*;
import java.io.*;
 
class Main
{
    public static void main( String[] args ) {
        // 変数宣言
        int x = 1;
          
        switch (x)
        {
            case 1:
            System.out.println("iは1です。\n"); // iは1です。
            break;
            
            case 2:
            System.out.println("iは2です。\n");
            break;
            
            case 3:
            System.out.println("iは3です。\n");
            break;
            
            default:
            System.out.println("iは1～3以外です。");
            break;
        }

    }
}
