#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) { return *(int*)a - *(int*)b; }

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    qsort(a, n, sizeof(int), cmp);

    int minDiff = INT_MAX, p1 = a[0], p2 = a[1];
    for (int i = 1; i < n; i++) {
        int diff = a[i] - a[i-1];
        if (diff < minDiff) { minDiff = diff; p1 = a[i-1]; p2 = a[i]; }
    }
    printf("Pair with minimum difference: %d and %d (diff = %d)\n", p1, p2, minDiff);
    return 0;
}
