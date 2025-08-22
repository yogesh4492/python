#include<iostream>
using namespace std;
int main(){
    int num,i,j;
    cout<<"Enter Number= ";
    cin>>num;
    for(i=1;i<=num;i++){
        cout<<"Multiplication table of "<<i<<endl;
        for(j=1;j<=10;j++){
            cout<<i<<" * "<<j<<" = "<<i*j<<endl;
        }
        cout<<endl;
    }
    return 0;
}