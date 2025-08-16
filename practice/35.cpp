// # 42. Check if a person is eligible for gym 
// # membership (age ≥ 16 or student = True).

#include<iostream>
using namespace std;
int main(){
    bool is_student=true;
    int age;
    cout<<"Enter Your Age= ";
    cin>>age;
    if(is_student){
        if(age>=16){
            cout<<"Student is eligible for gym Membership";  
        }
        else{
            cout<<"Student is not eligible because it age is less than 16.";
        }
    }
    else{
        cout<<"You Are Not Eligible Because You Are not A student .";
    }
    return 0;
}