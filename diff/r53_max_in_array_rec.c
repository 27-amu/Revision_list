#include <stdio.h>

int maxArr(int *a, int n) {
    if (n == 1) return a[0];
    int rest = maxArr(a, n-1);
    return a[n-1] > rest ? a[n-1] : rest;
}

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Maximum: %d\n", maxArr(a, n));
    return 0;
}
