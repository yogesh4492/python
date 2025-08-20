#include<iostream>
using namespace std;
int main(){
    float principle,rate,time,si;
    cout<<"Enter principe ,rate and time = ";
    cin>>principle>>rate>>time;

    si=(principle*rate*time/100);
    cout<<"SImple interst is = "<<si<<endl;
    return 0;
}