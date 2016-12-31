#include <stdio.h>

int main(void)
{
  int x = 5;  // 変数xの宣言・初期化
  int y = 3;  // 変数yの宣言・初期化
  int z = 0; 
  
  z = x / y;  // 5を3で割る
  
  printf("%d\n", z);  // 計算結果を表示
  
  return 0;
}
