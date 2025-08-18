/*I will write a code which will give me the sum of total number and the GPA of all the subjects */


#include <stdio.h>
int main(){
    int bangla, english, math, sum,bgs,islam, physics, chemistry, biology, higher_math;
    float gpa;
    printf("enter your bangla number: ");
    scanf("%d", &bangla);
    printf("enter your english number: ");
    scanf("%d", &english);
    printf("enter your math number: ");
    scanf("%d" ,&math);
      printf("enter your bgs number: ");
    scanf("%d" ,&bgs);
      printf("enter your islam number: ");
    scanf("%d" ,&islam);
      printf("enter your physics number: ");
    scanf("%d" ,&physics);
      printf("enter your chemistry number: ");
    scanf("%d" ,&chemistry);
      printf("enter your biology number: ");
    scanf("%d" ,&biology);
      printf("enter your higher-math number: ");
    scanf("%d" ,&higher_math);
     
    
    sum = (bangla + english + math +bgs +islam + physics + chemistry +biology + higher_math);
    printf("Your number is %d\n", sum);
    
    if (sum>800){
        printf("You pass the exam");
    }
    else{
        printf("You are not pass the exam");
    }
  
    
   
    
    return 0;
}