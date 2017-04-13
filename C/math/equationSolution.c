#include <stdio.h>
#include <math.h>

void equation2d(double a,double b,double c, 
            double *re1, double *im1, double *im2, double *re2, double *D)
{

        *D = b*b-4.0*a*c;                      
    
        if(D>0) {                           
                *re1 = (-b + sqrt(*D))/(2.0*a);
                *re2 = (-b - sqrt(*D))/(2.0*a);
                *im1 = 0.0;
                *im2 = 0.0;
        }
        else if(D==0) {
                *re1 = -b/(2.0*a);
                *re2 = 0.0;
                *im1 = 0.0;
                *im2 = 0.0;
        }
        else {                            
                *re1 = -b/(2.0*a);
                *re2 = *re1;
                *im1 = sqrt(-*D)/(2.0*a);
                *im2 = -*im1;
        }


}

int main()
{
        double re1,im1,re2,im2,D;

        // x^2 + 2x + 1 = 0 
        equation2d(1,2,1,&re1,&im1,&re2,&im2,&D);
        if(D==0) {
                printf("%f + %f j\n",re1,im1); // -1.000000 + 0.000000 j
        }
        else {
                printf("%f + %f j\n",re1,im1);
                printf("%f + %f j\n",re2,im2);
        }

        return 0;
}
