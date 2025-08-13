//check armstrong number

#include<iostream>
#include<cmath>
using namespace std;
int main(){
    int num,temp,cpy,digit=0,power,sum=0,rem,i;
    cout<<"enter number= ";
    cin>>num;
    temp=num;
    cpy=num;
    while(num!=0){
        num/=10;
        digit++;
    }
    for(i=1;i<=digit;i++){
        rem=temp%10;
        power=pow(rem,digit);
        sum+=power;
        temp/=10;


    }
    if(sum==cpy){
        cout<<"Armstrong number";
    }
    else{
        cout<<"Not a armstrong number";
    }
    return 0;
}