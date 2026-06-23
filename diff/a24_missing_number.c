#include <stdio.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n-1];
    printf("Enter %d integers (1 to %d with one missing): ", n-1, n);
    for (int i = 0; i < n-1; i++) scanf("%d", &a[i]);

    int expected = n * (n + 1) / 2, actual = 0;
    for (int i = 0; i < n-1; i++) actual += a[i];

    printf("Missing number: %d\n", expected - actual);
    return 0;
}
