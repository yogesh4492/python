//41. Check if a password is strong (length ≥ 8 and 
//contains a digit)

#include<stdio.h>
#include<string.h>
int main(){
    int flag=0;
    char  str[40];
    
    printf("Enter password= ");
    gets(str);
    int length=strlen(str);
    printf("%d",length);
    int count;
    if(length>=8){

    for(int i=0;i<length;i++){
        if(str[i]>='0' && str[i]<='9'){
            flag=1;
            count++;
        }
        
    }
}
 if(flag){
    printf("This is strong password");
    printf("%d digit in password",count);
 }
 else{
    printf("This is weak password");
 }

    return 0;

}