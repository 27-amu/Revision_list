#include <stdio.h>

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);

    for (int i = 1; i * i <= n; i++) {
        if (i * i == n) {
            printf("%d is a perfect square (sqrt = %d)\n", n, i);
            return 0;
        }
    }
    printf("%d is not a perfect square\n", n);
    return 0;
}
