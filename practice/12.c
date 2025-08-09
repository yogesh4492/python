//Convert kilometers to miles
#include<stdio.h>
int main(){

    double kilo,mile;
    printf("Enter teh kilomiter= ");
    scanf("%lf",&kilo);
    mile=kilo*0.621371;
    printf("miles= %lf",mile);

    return 0;
}