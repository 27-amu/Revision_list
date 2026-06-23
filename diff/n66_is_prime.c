#include <stdio.h>
#include <math.h>

int isPrime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i <= (int)sqrt(n); i++)
        if (n % i == 0) return 0;
    return 1;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("%d is %sprime\n", n, isPrime(n) ? "" : "not ");
    return 0;
}
