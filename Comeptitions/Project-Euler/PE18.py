#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

long long int max(long long int a, long long int b)
{
    if(a>b)
        return a;
    else
        return b;
}

long long int calc(long long int a[105][105], long long int n)
{
    long long int i, j;
    for(i = (n-2); i>=0; --i)
    {
        for(j=0; j<=i; ++j) 
        {
            a[i][j] = a[i][j] + max(a[i+1][j], a[i+1][j+1]);
            //printf("%lld ", a[i][j]);
        }
        //printf("\n");
    }
    return a[0][0];
}

int main() {

    long long int T,n,i,j,t,res[105];
    scanf("%lld", &T);
    for(t=0; t<T; ++t)
    {
        long long int a[105][105] = {0};
        scanf("%lld", &n);
        for(i=0; i<n; ++i)
            for(j=0; j<=i; ++j)
                scanf("%lld", &a[i][j]);
        //build(a,n);
        res[t] = calc(a,n);
        //printf("%lld\n", res[t]); 
    }
    for(t=0; t<T; ++t)
    {
        printf("%lld\n", res[t]); 
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}

