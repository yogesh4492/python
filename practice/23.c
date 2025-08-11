
// print reverse string with using inbuild and also user defined function

#include<stdio.h>
#include<string.h>
void reverse(char name1[]){
	int i,len=0;
	for(i=0;name1[i]!='\0';i++){
		len++;

	}
	for(i=len-1;i>=0;i--){
		printf("%c",name1[i]);
	}
}
int main(){
 
	char name[100],name1[100];
	printf("Enter your name = ");
	gets(name);
	printf("ENter Your friend name= ");
	gets(name1);
	strrev(name);
	printf("\n Your name in reversed = %s",name);
	printf("\nYour friend name in reversed order= ");
	reverse(name1);

	


	return 0;
}