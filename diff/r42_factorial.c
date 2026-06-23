#include <stdio.h>

long long factorial(int n) {
    return n == 0 ? 1 : n * factorial(n - 1);
}

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("%d! = %lld\n", n, factorial(n));
    return 0;
}
