#include <stdio.h>

int main(void)
{
  char x = 'a';  // 変数xの宣言・初期化
  
  printf("xに格納するデータを入力してください＞");
  scanf("%c", &x);

  printf("xは%c が入力されました\n", x);  // 計算結果を表示

  return 0;
}
