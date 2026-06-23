#include <stdio.h>

int *findLargest(int *a, int n) {
    int *max = a;
    for (int i = 1; i < n; i++)
        if (*(a+i) > *max) max = a+i;
    return max;
}

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Largest: %d\n", *findLargest(a, n));
    return 0;
}
