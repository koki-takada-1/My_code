#include <stdio.h>

int main(void){
    unsigned short N;
    int check;
    while (1)
    { 
        printf("ピラミッドの高さを入力してください:");
        check=scanf("%hu",&N);
        if(N>100) check = 0;
        if(check!=0) break;
        if(check==0){
            printf("半角かつ0以上かつ100以下の整数で入力してください\n");
            scanf("%*s");
        }
    }

    for(int i=0;i<N;i++){ 

        for(int j=0;j<N-i;j++){ 
            printf(" ");
        }
        for(int k=0;k<2*i-1;k++){
            printf("*");
        }   
        printf("\n");
    }
    return 0;
}