#include<stdio.h>
int main(){
    int row,i,j;
    printf("Enter Row= ");
    scanf("%d",&row);
    for(i=1;i<=row;i++){
        for(j=1;j<=i;j++){
            printf("*  ");
        }
        printf("\n");
    }
    for(i=1;i<row;i++){
        for(j=row;j>i;j--){
          printf("*  ");
        }
        printf("\n");
    }
    return 0;
}