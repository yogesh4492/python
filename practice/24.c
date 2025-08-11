#include<stdio.h>
int main(){
    int i,fact=1,num;
    printf("Enter number= ");
    scanf("%d",&num);
    for(i=1;i<=num;i++){
        fact*=i;
    }
    printf("Factorial of numbers is =%d",fact);
    return 0;
}