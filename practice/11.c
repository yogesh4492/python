#include<stdio.h>
int main(){
    float fer,cel;
    printf("Enter the fehrenhits= ");
    scanf("%f",&fer);
    cel=(fer-32)*5/9;

    printf("fer is= %.2f and cel =%.2f ",fer,cel);
    
    return 0;
}