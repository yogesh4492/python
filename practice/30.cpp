//using if else and recursion check prime number
#include<iostream>
using namespace std;
int prime(int num,int divisor){
    if(num<=1){
        return 0;
    }
    else if(num==divisor){
        return 1;
    }
    else if(num%divisor==0){
        return 0;
    }
    return prime(num,divisor+1);
}
int main(){
    int num;
    cout<<"Enter number= ";
    cin>>num;
    if(prime(num,2)){
        cout<<num<<" iS prime number";
    }
    else{
        cout<<num<<" is Not a prime number";
    }
}