#include<iostream>
using namespace std;
int main(){
    int num,rev=0,rem,tmp;
    cout<<"Enter the number= ";
    cin>>num;
    tmp=num;
    while(num!=0){
        rem=num%10;
        rev=(rev*10)+rem;
        num/=10;
    }
    if(rev==tmp){
        cout<<"Palindrome number";
    }
    else{
        cout<<"not a palindrome number";
        
    }
    return 0;
}