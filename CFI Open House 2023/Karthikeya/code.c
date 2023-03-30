#include <stdio.h>
#include <stdlib.h>
int main(){
    int t;//no of iterations
    scanf("%d",&t);
    int matches=0;
    int n;//no of persons
        scanf("%d",&n);
    for(int i=0;i<t;++i){
        int a[n];//birthday dates of persons
        for(int j=0;j<n;++j){
            a[j]=rand();
            a[j]=a[j]%365;
        }
      int check=0;
        for(int j=0;j<n;++j){
            for(int k=j+1;k<n;++k){
                if(a[j]==a[k]){
                    check=1;
                    break;
                }
            }
        }
      if(check==1){
        matches++;//no of groups of n persons when we found person with same birthdays;
      }
    }
    float prob=((float)matches/(float)t);
    printf("%f\n",prob);
}
