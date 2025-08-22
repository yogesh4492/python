#include<stdio.h>
int main(){
    int row,i,j,k,l;
    printf("Enter Row= ");
    scanf("%d",&row);
    int spc=row-1;
    for(i=1;i<=row;i++){
        for(k=1;k<=spc*2;k++){
            printf(" ");
        }
        for(j=1;j<=i;j++){
            printf("* ");
        }

        for(l=1;l<i;l++){
            printf("* ");
        }

        printf("\n");
        spc--;
    }
    return 0;

}