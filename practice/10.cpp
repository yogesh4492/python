//  Convert temperature from Celsius to Fahrenheit.

#include<iostream>
using namespace std;
int main(){

    int cel,fer;
    cout<<"Enter celcius= ";
    cin>>cel;

    fer=(cel*9/5)+32;

    cout<<cel<<" "<<fer<<"F";
    return 0;
}