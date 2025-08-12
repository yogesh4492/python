//check perfect number

#include<stdio.h>
int main(){
    int num,i,sum=0;
    printf("Enter Number= ");
    scanf("%d",&num);
    for(i=1;i<=num/2;i++){
        if(num%i==0){
            sum+=i;
        }
    }
    if(num==sum){
        printf("Perfect number");
    }
    else{
        printf("Not a perfect number");
    }
    return 0;
}