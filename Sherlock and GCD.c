#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int gcd ( int a, int b )
{
    if ( a==0 ) 
        return b;
    return gcd ( b%a, a );
}

int main() {

    long long int T,i,j,n,a[105],g;
    scanf("%lld", &T);
    for(i =0; i<T; ++i)        
    {
        scanf("%lld", &n);
        scanf("%lld", &a[0]);
        g = a[0];
        for(j = 1; j<n; ++j)        
        {
            scanf("%lld", &a[j]);
            g = gcd(a[j], g);
        }   
        if(g==1)
            printf("YES\n");
        else
            printf("NO\n");
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
