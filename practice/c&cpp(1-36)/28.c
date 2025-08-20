
//print fibonacci series
#include<stdio.h>
int main(){
    int n1=0,n2=1,n3;
    int terms;
    printf("Enter the terms for fibonacci series= ");
    scanf("%d",&terms);
    printf("Fibonacci series= %d %d",n1,n2);
    for(int i=1;i<=terms-2;i++){
        n3=n1+n2;
        printf(" %d",n3);
        n1=n2;
        n2=n3;
    }
    
    return 0;

}