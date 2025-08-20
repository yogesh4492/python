//calculate compound interest using formula

#include<stdio.h>
#include<math.h>
int main(){
    float p,r,t;
    char c='%';
    printf("Enter Principle Amount= ");
    scanf("%f",&p);
    printf("Enter rate in %c = ",c);
    scanf("%f",&r);
    printf("Enter Time period in year= ");
    scanf("%f",&t);
    
    float amount;
    amount=p*pow((1+r/100),t);
    float ci=amount-p;
    printf("\nprinciple Amount=%.2f",p);
    printf("\nRate=%.2f '%c'/year",r,c);
    printf("\nTime Period=%.2f year",t);
    printf("\nCompound Interest Amount=%.2f",ci);
    printf("\nTotal Amount=%.2f",amount);

    return 0;
}