#include<stdio.h>
int main(){

    float length,width,perimiter;
    printf("enter the length= ");
    scanf("%f",&length);
    printf("\n enter width= ");
    scanf("%f",&width);
    perimiter=(2*(length+width));
    printf("\n perimiter of rectangle is =%.2f",perimiter);
    return 0;
}