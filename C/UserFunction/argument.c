#include <stdio.h>

// ユーザ関数を宣言・定義
int func(int x1, int x2)
{
  
  x1 = x1 * 10;
  x2 = x2 * 10;
  
  printf("x1=%d, x2=%d \n", x1, x2);
 
  return 0;  // 型があるので戻り値が必要
}

// メイン関数
int main()
{
  int x=10, y=10;
  
  func(x, y);  // ユーザ関数1を実行（呼び出し）
  
  printf("x=%d, y=%d \n", x, y);
  
  return 0;
}
