// 37. Check if a number is divisible by 3 or 5 using 
// or
#include<stdio.h>
int main(){
    int num;
    printf("Enter Number= ");
    scanf("%d",&num);
    if(num%3==0 || num%5==0)
    {
        printf("%d is divisible by 3 or 5\n ",num);    
    }
    else{
        printf("\n %d is not divisible by 3 or 5",num);
    }
    return 0;
}