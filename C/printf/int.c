#include <stdio.h>

int main(void)
{
  int x = 10;  // 変数xの宣言・初期化
  int y = 20;  // 変数yの宣言・初期化
  
  printf("%d\n", x);  // 変数の中身のみ表示
  printf("xは%d\n", x); // 任意の文字列と変数の中身を表示
  printf("xは%d yは%d", x, y); // 任意の文字列と複数の変数の中身を表示
  
  return 0;
}
