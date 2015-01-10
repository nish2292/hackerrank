#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int cnt[105] = {0}, n, m, i, c, a[105], b[105];
    scanf("%d %d", &n, &m);
    for(i=0; i<m; ++i)
    {
        scanf("%d %d", &a[i], &b[i]);   
        //cnt[b[i]]++;
    }
    for(i=m-1; i>=0; --i)
    {
        cnt[b[i]] += cnt[a[i]] + 1; 
    }
    c=0;
    for(i=2; i<=n; ++i)
        if(cnt[i]%2 == 1)   
            ++c;
    printf("%d\n",c);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
