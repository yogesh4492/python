#include<stdio.h>
int main(){
    int row,i,k,j;
    printf("\n Enterw Row= ");
    scanf("%d",&row);
    int spc=row-1;
    for(i=1;i<=row;i++){
        for(k=1;k<=spc;k++){
            printf(" ");
        }
        for(j=1;j<=i;j++){
            printf("* ");
        }
        printf("\n");
        spc--;
    }
    spc=0;
    for(i=1;i<=row;i++){
        for(k=spc;k>=1;k--){
            printf(" ");
        }
        for(j=row;j>=i;j--){
            printf("* ");
        }
        printf("\n");
        spc++;
    }

    return 0;

}