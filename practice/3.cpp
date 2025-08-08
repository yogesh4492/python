#include<iostream>
using namespace std;
int main(){
	int num,flag,i,j;
	
	cout<<"Enter number= ";
	cin>>num;
	
	for(i=2;i<=num;i++){
		flag=1;
		for(j=2;j<=i/2;j++)
		if(i%j==0){
			flag=0;
			
		}
		if(flag){
			cout<<i<<endl;
		}
		
	}
	return 0;
}
