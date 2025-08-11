#include<iostream>
#include<string>
using namespace std;
int main(){

string name,name1;
cout<<"Enter your name= ";
getline(cin,name);
cout<<"enter your friend name =";
getline(cin,name1);
for( int i=name.length()-1;i>=0;i--){
   cout<<name[i];
}

   return 0;
}