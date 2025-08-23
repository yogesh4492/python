#include<iostream>
using namespace std;
int main(){
    int row,i,j,k;
    cout<<"Enter Row= ";
    cin>>row;
    int spc=row-1;
    for(i=1;i<=row;i++){
        for ( k = 1; k<= spc; k++)
        {
            cout<<" ";
        }
        for(j=1;j<=i;j++){
            cout<<"* ";
        }
        cout<<endl;
        spc--;
        
    }
    spc=1;
    for(i=1;i<row;i++){
        for(k=1;k<=spc;k++){
            cout<<" ";
        }
        for(j=row;j>i;j--){
            cout<<"* ";
        }
        cout<<endl;
        spc++;
    }
    return 0;
}