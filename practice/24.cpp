//factorial of number
#include<iostream>
using namespace std;
int main(){
    int i,num,fact=1;
    cout<<"Enter the number= ";
    cin>>num;
    for(i=1;i<=num;i++){
        fact*=i;
    }
    cout<<"Fctorial of"<<num<<" is ="<<fact<<endl;
    return 0;
}