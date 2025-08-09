#include<stdio.h>
int main(){
    float cel,fer;
    printf("Enter celcius is= ");
    scanf("%f",&cel);
    
    fer=(cel*9/5)+32;
    
    printf(" cel is %.2f is= %.2f fehrenhit",cel,fer);
    return 0;
}