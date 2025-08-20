// check number is even or odd
#include<stdio.h>
int main(){
    int num;
    printf("Enter the num= ");
    scanf("%d",&num);
    if(num%2==0){
        printf("number is even");
    }
    else{
        printf("Nnumber is odd");
    }
    return 0;
}