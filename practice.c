#include <stdio.h>
int main() {
    char name[50];
    char father_name[50];
    char mother_name[50];
    int age ;
    float gpa;

     printf("What's your name :");
     scanf("%s", &name);
     printf("What's your age :");
     scanf("%d", &age);
     printf("What's your GPA: );
     scanf("%f", &gpa);
     printf("What's your father name :") ;
     scanf("%s", &father_name);
     printf("What's your mother name :") ;
     scanf("%s", &mother_name);

     printf("Hello %s . I hope you are well. Your age is %d . You can do anything in your life if you practice well. Your GPA is %.2f not so bad. But you should practice more. Your father name is %s . Your mother name is %s.", name, age , gpa , father_name, mother_name);
       // I will scan print like this. hello naimul .I hope you are well .your age is 10 .You can do anything in your life if you practice well. Your GpA is 4.44 not so bad .But you should practice more. Your father name is abdul and mother name is nasima

    return 0;

}