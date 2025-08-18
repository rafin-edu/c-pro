#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int num1, sum1;
    int num2 ,differnce1;
    float num3 ,sum2;
    float num4, differnce2;
    
    
    scanf("%d %d \n%f %f", &num1, &num2, &num3, &num4);
    
    sum1 = num1+num2;
    differnce1= num1-num2;
    sum2= num3 + num4;
    differnce2= num3-num4;
    
    printf("%d %d \n%.1f %.1f", sum1, differnce1, sum2 ,differnce2);
    
    return 0;
}
