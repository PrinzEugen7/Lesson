    #include <stdio.h>
     
    int main(void)
    {
      int x;
      x = 1;
      if(x > 3){
        printf("xは3より大きい\n");
      }
      else if(x > 2){
        printf("xは2より大きい\n");
      }
      else if(x > 1){
        printf("xは1より大きい\n");
      }
      else {
        printf("xは1以下だ\n");
      }
      return 0;
    } 
