#include<stdio.h>
int main(){
  int a,b,c;
  printf("Enter value of a= ");
  scanf("%d",&a);
  printf("Enter value of b= ");
  scanf("%d",&b);
  c=a;
  a=b;
  b=c;
  
  printf("value of a=%d\n ",a);
  printf("Value of b=%d\n ",b);
  
  return 0;

}