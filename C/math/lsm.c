#include <stdio.h>
 
#define N 5             //データの個数
 
void lsm(double x[],double y[])
{
        int i;
        double a0,a1,p,q;
        double A00,A01,A02,A11,A12;


 
        A00=A01=A02=A11=A12=0.0;
 
        for (i=0;i<N;i++) {
                A00+=1.0;
                A01+=x[i];
                A02+=y[i];
                A11+=x[i]*x[i];
                A12+=x[i]*y[i];
        }
 
        a0 = (A02*A11-A01*A12) / (A00*A11-A01*A01);
        a1 = (A00*A12-A01*A02) / (A00*A11-A01*A01);
        printf("a0=%f\na1=%f", &a0, a1);

 
}
 
int main()
{
        double x[N]={1.1,2.3,2.8,4.2,5.1};
        double y[N]={0.7,1.9,3.1,4.2,5.6};
 
        lsm(x,y);
 
        return 0;
}
