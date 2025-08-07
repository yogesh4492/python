// check number positive ,negative or zero

#include<iostream>
using namespace std;
int main(){
    int num;
    cout<<"ENter the number= ";
    cin>>num;

   if(num>0){
    cout<<"num is positive";
   }
   else if(num<0){
    cout<<"number is negative";
   }
   else{
    cout<<"num is zero";
   }
    return 0;
}