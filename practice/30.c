//using if else and recursion check prime number
#include<stdio.h>
int prime(int num,int divisor){
    if(num<=1){
        return 0;
    }
    else if(num==divisor){
        return 1;
    }
    else if(num%divisor==0){
        return 0;
    }
    return prime(num,divisor+1);
}
int main()
{
    int num;
    printf("Enter the number= ");
    scanf("%d",&num);
    if(prime(num,2)){
        printf("%d is prime number",num);
    }
    else{
        printf("%d is not a prime number",num);
    }
    return 0;
}