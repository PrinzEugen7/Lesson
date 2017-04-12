#include <stdio.h>
#include <math.h>

// 方程式の解を計算
void equationSolution(double a, double b, double c, 
                  double *re1, double *re2, double *im1, double*im2, double *D)
{
        *D = b*b-4.0*a*c;                      
    
        if(*D>0) {                           
                *re1 = (-b + sqrt(*D))/(2.0*a);
                *re2 = (-b - sqrt(*D))/(2.0*a);
                *im1 = 0.0;
                *im2 = 0.0;
        }
        else if(*D==0) {
                *re1 = -b/(2.0*a);
                *re2 = 0.0;
                *im1 = 0.0;
                *im2 = 0.0;
        }
        else {                            
                *re1 = *re2 =-b/(2.0*a);
                *im1 = sqrt(-*D)/(2.0*a);
                *im2 = -*im1;
        }
}

int main()
{
        double a=1,b=2,c=1;
        double re1 = 0, re2 = 0, im1 = 0,im2 = 0, D = 0;

        equationSolution(a, b, c, &re1, &re2, &im1, &im2, &D);

        if(D==0) printf("%f + %f j\n",re1,im1); // -1.000000 + 0.000000 j
        else printf("%f + %f j\n%f + %f j\n",re1,im1,re2,im2)
        
        return 0;
}
