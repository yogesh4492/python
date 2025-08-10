//Find the total marks and percentage of 5 subjects.


#include<stdio.h>
int main(){
    int sub[5],marks=0;
    int percentage;
    int i;
    for(i=0;i<5;i++){
        printf("Enter Subject %d marks =",i+1);
        scanf("%d",&sub[i]);
        marks+=sub[i];
    }

    percentage=marks/5;

    printf("Total marks = %d",marks);
    printf("\n Percentage =%d ",percentage);

    return 0;
}