#include <stdio.h>

int countDigits(int n) {
    if (n < 10) return 1;
    return 1 + countDigits(n / 10);
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Number of digits: %d\n", countDigits(n < 0 ? -n : n));
    return 0;
}
