#include<iostream>
#include<string>
using namespace std;
int lenht(string name){
   int i,count=0;
   for(i=0;;i++){
    count++;
   }
   return count;
}
int main(){
    string name;
    cout<<"enter your name= ";
    getline(cin,name);
    int len=name.length();
    cout<<"Length of string = "<<len<<endl;
    int res= lenht(name);
    cout<<res;
    return 0;
}