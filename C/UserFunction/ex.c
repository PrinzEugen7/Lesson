#include <stdio.h>

// ユーザ関数の宣言
int func1();  // ユーザ関数1を宣言(int型)
void func2();  // ユーザ関数2を宣言(型なし)

// メイン関数
int main()
{

  func1();  // ユーザ関数1を実行（呼び出し）
  func2();  // ユーザ関数2を実行 （呼び出し）
  
  return 0;
}
// ユーザ関数1を定義
int func1()
{
  printf("ユーザ関数1を実行");
 
  return 0;  // 型があるので戻り値が必要
}

// ユーザ関数2を定義
void func2()
{
  printf("ユーザ関数2を実行");
 // 型がない(void型)なので戻り値は不要 
}
