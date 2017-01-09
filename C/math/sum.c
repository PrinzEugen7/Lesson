#include <stdio.h>
  
double sum(double data[], int n)
{
    int i;
    double total = 0.0;     // 変数の宣言
  
    for(i=0; i<n; i++){
        total += data[i];   // 合計を計算
    }
      
    return total;           // 合計を返す
}
  
  
int main(void)
{
    double data[] = {1.0,2.0,3.0,4.0,5.0};      // 配列の宣言
    int n = sizeof(data) / sizeof(data[0]); // 配列の要素数(データ数)
     
    printf("合計は%f", sum(data,n));               // 計算結果を出力
     
    return 0;
}

