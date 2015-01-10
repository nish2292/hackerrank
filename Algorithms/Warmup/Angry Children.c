#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX 100000
#define MAX_VAL 1000000001

int candies[MAX];

/** The code to read from STDIN and output to STDOUT has been provided by us, for convenience. You may or may not use this. **/

int cmpfunc (const void * a, const void * b)
{
    return ( *(int*)a - *(int*)b );
}
 
int main() {
    
    int N,K;
    int i, temp;
    
    scanf("%d %d",&N,&K);
    for(i = 0;i < N;i++)
        scanf("%d",candies + i);
  
    qsort(candies, N, sizeof(int), cmpfunc);
    //int unfairness = // Compute the min unfairness over here, using N,K,candies
    
    int min;
    
    min = candies[K-1] - candies[0];
    
    for(i = K; i < N; i++)
    {
        temp = candies[i] - candies[i-K+1];
        if(temp < min)
            min = temp;
    }
        //printf("%d\n",candies[i]);
    int unfairness = min;    
    printf("%d",unfairness);
    return 0;
}
