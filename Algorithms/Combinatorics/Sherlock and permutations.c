#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

long long int choose(long long int n,long long int k)
{
    long long int a[3000] = {0}, i, j, t;
    a[0] = 1;
    k = k<(n-k)? k:(n-k);
    for(i=1; i<=n; ++i)
    {
        t = i<k?i:k;
        for(j=t; j>0; --j)
            a[j] = (a[j] + a[j-1]) % 1000000007;
    }
    return a[k];
}


int main() {

    long long int i,n,m,T,t;
    scanf("%lld", &T);
    for(i=0; i<T; ++i)
    {
        scanf("%lld %lld", &n, &m);
        t = choose((n+m-1),n);
        printf("%lld\n", t);
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}

