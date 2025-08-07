// check number positive ,negative or zero

#include<stdio.h>
int main(){
    int num;
    printf("\n enter the number= ");
    scanf("%d",&num);
    if(num>0)
    {
        printf("\n number is positive");
    }
    else if(num<0){
        printf("\n num is negative");
    }
    else{
        printf("\n number is zero");
    }
    return 0;
}