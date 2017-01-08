#include <stdio.h>

// ユーザ関数を宣言・定義
int func(int x1, int x2)
{
  
  int x3 = 0;
  
  x3 = x1 * x2;
 
  return x3;  // 変数xを戻り値に設定(呼び出し側へ送る)
}

// メイン関数
int main()
{
  int x = 10, y = 10, z = 0;
  
  z = func(x, y);  // ユーザ関数を実行(戻り値x3の値を変数zへ代入)
  
  printf("z=%d\n", z);
  
  return 0;
}
