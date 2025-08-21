/*36. Check if a number is divisible by both 3 and 5 
using and.*/

#include<iostream>
using namespace std;

int main(){
    int number;
    cout<<"Enter number= ";
    cin>>number;
    if(number%3==0&&number%5==0){
    cout<<number<<" is divisible by both 3 and 5 "<<endl;
    }
    else{
       cout<<number<<" not divisible by both 3 and 5"<<endl;
    }
    return 0;
}