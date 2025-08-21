#include<stdio.h>
int main(){
    float principle,rate,time,si;
    printf("Enter principle =");
    scanf("%f",&principle);
    printf("Enter rate= ");
    scanf("%f",&rate);
    printf("Enter time =");
    scanf("%f",&time);

    si=(principle*rate*time/100);
    printf("simple inerest = %.2f",si);
    return 0;
}