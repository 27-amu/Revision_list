#include <stdio.h>
#include <string.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);

    int sieve[n+1];
    memset(sieve, 1, sizeof(sieve));
    sieve[0] = sieve[1] = 0;

    for (int i = 2; (long long)i*i <= n; i++)
        if (sieve[i])
            for (int j = i*i; j <= n; j += i)
                sieve[j] = 0;

    printf("Primes up to %d: ", n);
    for (int i = 2; i <= n; i++)
        if (sieve[i]) printf("%d ", i);
    printf("\n");
    return 0;
}
