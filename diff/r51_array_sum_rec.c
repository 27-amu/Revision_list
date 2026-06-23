#include <stdio.h>

int arraySum(int *a, int n) {
    if (n == 0) return 0;
    return a[n-1] + arraySum(a, n-1);
}

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Sum: %d\n", arraySum(a, n));
    return 0;
}
