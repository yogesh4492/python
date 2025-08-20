//check the length of string 
#include<stdio.h>
#include<string.h>
int len(char str[]){
	int i;
	for(i=0;str[i]!='\0';i++){
		
	}
	return i;
}
int main(){
	char str[100];
	printf("Enter any string= ");
	gets(str);
	int res=strlen(str);
	int length=len(str);
	printf("length=%d",res);
	printf("length of string =%d",length);
	return 0;
}
