#include <stdio.h>

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("%d is %sa power of 2\n", n,
           (n > 0 && (n & (n-1)) == 0) ? "" : "not ");
    return 0;
}
