#include <stdio.h>
int main()
{
    int i;
    float n;
    for(n=3; n<=30;  n=n+3)
    for ( i = 1; i<=10; i++)

    {
       printf("3 X %d = %.0f\n", i ,n);
    }
    
    return 0;
}
