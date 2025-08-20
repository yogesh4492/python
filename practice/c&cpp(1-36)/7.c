//swape two values without using third variable

#include<stdio.h>
int main(){
    int num1,num2;
    printf("Enter Number 1= ");
    scanf("%d",&num1);
    printf("Enter Number 2= ");
    scanf("%d",&num2);

   num1=num1+num2;
   num2=num1-num2;
   num1=num1-num2;

   printf("Value of num1= %d and value of num2= %d",num1,num2);


    return 0;

}