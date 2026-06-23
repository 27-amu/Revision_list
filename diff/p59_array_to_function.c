#include <stdio.h>

int sumArray(int *a, int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) sum += *(a + i);
    return sum;
}

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Sum (via pointer): %d\n", sumArray(a, n));
    return 0;
}
