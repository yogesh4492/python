//#convert minute into second using namespace 

#include<stdio.h>
int main(){
    int minute,second;
    printf("Enter Minute= ");
    scanf("%d",&minute);
    second=minute*60;
    printf("TOtal second in %d minute is =%d",minute,second);
    
    return 0;
}