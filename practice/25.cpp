//check perfect number

#include<iostream>
using namespace std;
int main(){
    int num,sum=0,i;
    cout<<"Enter number= ";
    cin>>num;
    for(i=1;i<=num/2;i++){
        if(num%i==0){
            sum+=i;
        }
    }
    if(num==sum)
    {
        cout<<"perfect number1"<<endl;
    }
    else{
        cout<<"Not a perfect number";
    }
    return 0;

}