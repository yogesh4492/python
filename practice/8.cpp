#include<iostream>
using namespace std;
int main(){
    int num1,num2;
    cout<<"Enter the num1 and num2= ";
    cin>>num1>>num2;

    num1=num1*num2;
    num2=num1/num2;
    num1=num1/num2;

    cout<<"value of num1 = "<<num1<<" And value of num2= "<<num2;

    return 0;
}
