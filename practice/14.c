//Convert minutes into hours and minutes.
#include<stdio.h>
int main(){
    float minute,hours;
    printf("Enter minutes = ");
    scanf("%f",&minute);
    hours=minute/60;
    printf("\n hours is %.2f when minutes= %.2f ",hours,minute);
    return 0;
}