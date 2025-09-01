#include<stdio.h>
int main(){
    int user1,user2,i,j,ini,inj,outi,outj;
    int row=3,col=3;
    for(i=1;i<=row;i++){
        for(j=1;j<=col;j++){
            printf("%d%d | ",i,j);
        }
        printf("\n---  ---  ---\n");
    }

    printf("User1 enter index of i and j To Print x= ");
    scanf("%d %d",&ini,&inj);
    for(i=1;i<=row;i++){
        for(j=1;j<=2;j++){
           if( ini==i && j==inj){
            printf("X");
           }
        }
    }

}
