#include<iostream>
#include<cmath>
using namespace std;
int main(){
    float principle,rate,time,ci,a;
    cout<<"Enter principle ,rate and time =";
    cin>>principle>>rate>>time;

    a=principle*pow((1+rate/100),time);
    ci=a-principle;

    cout<<"Total amount is = "<<a<<endl;
    cout<<"Compound intrest is = "<<ci<<endl;
    
    return 0;
}