#include <stdio.h>

// 合計の計算
double sum(double data[], int n)
{
    int i;					// 変数の宣言
    double total = 0.0;
  
    for(i=0; i<n; i++){
        total += data[i];   // 合計を計算
    }
      
    return total;           // 合計を返す
}

// 平均の計算 
double ave(double data[], int n)
{
    double total = sum(data, n);	// 合計
    return total/n;				// 平均=合計/データ数
}
    
int main(void)
{
	double data[] = {1.2,2.1,3.1,4.1,5.1};   	// 配列の宣言
    int n = sizeof(data) / sizeof(data[0]);		// 配列の要素数(データ数)
     
    printf("平均値は%f", ave(data,n));			// 計算結果を出力
     
    return 0;
}
