#include <stdio.h>

int main() {
    int n, sum = 0;
    printf("Enter a number: ");
    scanf("%d", &n);

    for (int i = 1; i < n; i++)
        if (n % i == 0) sum += i;

    printf("%d is %sa perfect number\n", n, sum == n ? "" : "not ");
    return 0;
}
