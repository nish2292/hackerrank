#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
long long int SumDivisbleBy(long long int n, long long int p){
return n*(p/n)*((p/n)+1)/2;
}
int main() {
long long int T,i,N,c;
scanf("%lld", &T);
while(T--)
{
scanf("%lld", &N);
c= SumDivisbleBy(3,N-1)+SumDivisbleBy(5,N-1)-SumDivisbleBy(15,N-1);
printf("%lld\n",c);
}
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
return 0;
}
