//Find the total marks and percentage of 5 subjects.

#include<iostream>
using namespace std;
int main(){
    int sub[5],i,marks=0,percentage;
    for(i=0;i<5;i++){
        cout<<"Enter Subject "<<i+1<<" Marks  = ";
        cin>>sub[i];
        marks+=sub[i];
    }

    percentage=marks/5;

    cout<<"Total Marks = "<<marks<<endl;
    cout<<"percentage = "<<percentage<<"% "<<endl;
    return 0;
}
