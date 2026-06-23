#include <stdio.h>

int countZeros(int n) {
    if (n < 10) return (n == 0) ? 1 : 0;
    return (n % 10 == 0 ? 1 : 0) + countZeros(n / 10);
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Number of zeros in %d: %d\n", n, countZeros(n));
    return 0;
}
