/*I will write a code which will give me the sum of total number and the GPA of all the subjects */


#include <stdio.h>
int main(){
    int bangla, english, math, sum;
    float gpa;
    printf("enter your bangla number: ");
    scanf("%d", &bangla);
    printf("enter your english number: ");
    scanf("%d", &english);
    printf("enter your math number: ");
    scanf("%d" ,&math);
    
    sum = (bangla + english + math);
    printf("Your number is %d\n", sum);
    
    if (sum>250){
        printf("You pass the exam");
    }
    else{
        printf("You are not pass the exam");
    }
  
    
   
    
    return 0;
}