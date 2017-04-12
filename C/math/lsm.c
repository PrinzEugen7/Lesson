#include <stdio.h>

// 最小二乗法の計算 
void lsm(double x[],double y[], int N, double *a0, double *a1)
{
        int i;
        double A00=0 ,A01=0, A02=0, A11=0, A12=0;
 
        for (i=0;i<N;i++) {
                A00+=1.0;
                A01+=x[i];
                A02+=y[i];
                A11+=x[i]*x[i];
                A12+=x[i]*y[i];
        }
 
        *a0 = (A02*A11-A01*A12) / (A00*A11-A01*A01);
        *a1 = (A00*A12-A01*A02) / (A00*A11-A01*A01);
}
 
int main()
{
        double x[]={1.1,2.3,2.8,4.2,5.1};
        double y[]={0.7,1.9,3.1,4.2,5.6};
        double a0 = 0,a1 = 0;
        
        // データの個数
        int N = sizeof(x) / sizeof(x[0]); 
        
        // 最小二乗法の計算
        lsm(x, y, N, &a0, &a1);
        
        printf("a0=%f\na1=%f", a0, a1);
        
        return 0;
}
