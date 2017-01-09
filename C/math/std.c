#include <stdio.h>
 
// 合計の計算
double sum(double data[], int n)
{
    int i;                  // 変数の宣言
    double total = 0.0;
   
    for(i=0; i<n; i++){
        total += data[i];   // 合計を計算
    }
       
    return total;           // 合計を返す
}
 
// 平均の計算
double ave(double data[], int n)
{
    double total = sum(data, n);    // 合計
    return total/n;             	// 平均=合計/データ数
}

// 分散の計算
double var(double data[], int n) {
    int i;
    double a = ave(data, n);	// 平均値
    double v = 0.0;				// 分散
    // 分散を計算
    for (i=0; i<n; i++)
        v += (data[i] - a) * (data[i] - a);
    return v/n;					// 分散の平均
}

// 標準偏差の計算
double std(double data[], int n) {
    return sqrt(var(data, n));			// 標準偏差=分散の平方根
}

// Main
int main(void)
{
    double data[] = {1.2,2.1,3.1,4.1,5.1};      // 配列の宣言
    int n = sizeof(data) / sizeof(data[0]);     // 配列の要素数(データ数)
      
    printf("標準偏差は%f", std(data,n));		// 計算結果を出力
      
    return 0;
}
