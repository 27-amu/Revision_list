#include <stdio.h>

int main() {
    int n;
    printf("Enter n (odd count, all except one appear twice): ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int result = 0;
    for (int i = 0; i < n; i++) result ^= a[i];
    printf("Non-repeating element: %d\n", result);
    return 0;
}
