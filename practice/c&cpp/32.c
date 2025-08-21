// calculte averagte of n number 
#include<stdio.h>
int main(){
    int size,sum=0;
    printf("Enter How Many Number You Want To Enter = ");
    scanf("%d",&size);
    int num;
    for(int i=0;i<size;i++){
        printf("Enter Num[%d]= ",i+1);
        scanf("%d",&num);
        sum+=num;
    }
    float avg;
    avg=sum/size;
    printf("Average of %d number = %d",size,avg);
    return 0;
}