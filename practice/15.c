//Convert minutes into hours and minutes.

#include<stdio.h>
int main(){
 float hour,minites;
 printf("enter hours= ");
 scanf("%f",&hour);
 minites=hour*60;

 printf("%.2f in minute in %.1f hours" ,minites,hour);
 

    return 0;
}
