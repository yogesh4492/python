#include<stdio.h>
int main(){
	
	int num,flag=1,i;
	printf("\n Ener Number= ");
	scanf("%d",&num);
	for(i=2;i<num;i++){
		if(num%i==0){
			flag=0;
			break;
		}
	}
	if(flag==1){
		printf("\n Prime number");
	}
	else{
		printf("\n nota prime number");
	}
	return 0;
	
}
