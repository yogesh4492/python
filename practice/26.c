//check armstrong or not
#include<stdio.h>
#include<math.h>
int main(){
    int num,temp,cpy,i,rem,sum=0,power,dig=0;
    printf("enter number= ");
    scanf("%d",&num);
    temp=num;
    cpy=num;
    while(num!=0){
        num=num/10;
        dig++;
    }
	for(i=1;i<=dig;i++){
       rem=temp%10;
       power=pow(rem,dig);
       sum=sum+power;
       temp/=10;
    }
    if(cpy==sum){
      printf("armstrong number");
    }
    else{
        printf("not a armstrong number");
    }
    return 0;
}
