// #Convert  miles to kilomiter
#include<stdio.h>
int main(){

    double kilo,mile;
    printf("Enter the miles= ");
    scanf("%lf",&mile);
    kilo=mile/0.621371;
    printf("mile= %.2lf",kilo);
    return 0;

}