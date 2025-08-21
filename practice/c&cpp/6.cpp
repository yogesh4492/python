#include<iostream>
using namespace std;
int main(){
    int a,b,c;
    cout<<"Enter value of a and b= ";
    cin>>a>>b;
    c=a;
    a=b;
    b=c;

    cout<<"value of a= "<<a<<" and  value of b= "<<b;
    return 0;
}
