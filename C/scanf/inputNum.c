#include <stdio.h>

int main(void)
{
  int x = 0;  // 変数xの宣言・初期化
  double y = 0;  // 変数yの宣言・初期化
  cahr z = 'a';  // 変数zの宣言・初期化 
  
  printf("xに格納するデータを入力してください＞");
  scanf("%d", &x);
  printf("yに格納するデータを入力してください＞");  
  scanf("%f", &y);
  printf("zに格納するデータを入力してください＞");  
  scanf("%c", &z);
  
  printf("xは%d yは&f zは%c が入力されました\n",x, y, z);  // 計算結果を表示

  return 0;
}
