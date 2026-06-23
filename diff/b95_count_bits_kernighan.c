#include <stdio.h>

int main() {
    int n, count = 0;
    printf("Enter a number: ");
    scanf("%d", &n);

    while (n) { n = n & (n - 1); count++; }
    printf("Set bits (Brian Kernighan method): %d\n", count);
    return 0;
}
