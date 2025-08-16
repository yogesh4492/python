//calculate average of n number 

#include<iostream>
using namespace std;
int main(){
    int n,sum=0;
    cout<<"Enter How Many Number you Want To enter= ";
    cin>>n;
    int num;
    for(int i=1;i<=n;i++){
        cout<<"Enter Number "<<i<<" = ";
        cin>>num;
        sum+=num;
    }
    float avg;
    avg=float(sum)/n;
    cout<<"Average of "<<n<<" numbers is  = "<<avg<<endl;

    return 0;
}