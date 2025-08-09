// Find the area of a rectangle (length × width).

#include<stdio.h>
int main(){
    
    float length,width;
    printf("Enter length= ");
    scanf("%f",&length);
    printf("Enter Width= ");
    scanf("%f",&width);
    float area;
    area=length*width;
    printf("Area of rectangle = %.2f",area);

    return 0;
}
