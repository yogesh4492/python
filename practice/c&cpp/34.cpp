// # 38. Check if a number is not divisible by 2 using 
// # not.

#include<iostream>
using namespace std;
int main(){
    int num;
    printf("Enter number= ");
    scanf("%d",&num);
    if(!(num%2==0)){

        printf("%d is not divisible by 2",num);
    }
    else{
        printf("%d is divisible by 2",num);
        
    }
    return 0;

}