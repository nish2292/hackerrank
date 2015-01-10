#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define F 50
long int Fib[F]; 

void buildFibo()
{
    int i;
    Fib[0] = 0;
    Fib[1] = 1;
    for(i=2; i<F; ++i)
        Fib[i] = Fib[i-1] + Fib[i-2];
}

int isFibo(long int N)
{
    int l,h,m;
    l=0;
    h=F-1;
    while(l<=h)
    {
        m = (l+h)/2;    
        if(Fib[m]<N)
            l = m+1;
        else if(Fib[m]>N)
            h = m-1;
        else
            return 1;
        //printf("%d %d %ld %ld %ld\n",l,h, Fib[l], Fib[h], N);
    }
    return 0;
}

int main() {

    long int a[100001], T;
    int i;
    buildFibo();
    scanf("%ld", &T);
    for(i=0; i<T; ++i)
        scanf("%ld", &a[i]);
    //printf("%ld\n", Fib[99]);
    for(i=0; i<T; ++i)
        if(isFibo(a[i]))
            printf("IsFibo\n");
        else
            printf("IsNotFibo\n");
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
    
}
