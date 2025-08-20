#include<stdio.h>
#include<math.h>
int main(){
    float pri,rate,time,ci,a;
    printf("Enter the principle= ");
    scanf("%f",&pri);
    printf("Enter the rate= ");
    scanf("%f",&rate);
    printf("Enter the time= ");
    scanf("%f",&time);

    a=pri*pow((1+rate/100),time);
    ci=a-pri;

    printf("total amountis= %f\n",a);
    printf("Comp[ound amount is = %f\n",ci);
    return 0;
}