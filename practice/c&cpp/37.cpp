#include<iostream>
using namespace std;
int main(){
    int row ,i,j,k;
    cout<<"Enter row= ";
    cin>>row;
    int spc=row-1;
    for(i=1;i<=row;i++){
        for(k=1;k<=spc*2;k++){
            cout<<" ";
        }
        for(j=1;j<=i;j++){
            cout<<"* ";
        }
        cout<<endl;
        spc--;
    }
    return 0;
}