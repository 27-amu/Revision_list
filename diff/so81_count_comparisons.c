#include <stdio.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int comparisons = 0, swaps = 0;
    for (int i = 0; i < n-1; i++)
        for (int j = 0; j < n-i-1; j++) {
            comparisons++;
            if (a[j] > a[j+1]) { int t = a[j]; a[j] = a[j+1]; a[j+1] = t; swaps++; }
        }

    printf("Sorted: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\nComparisons: %d, Swaps: %d\n", comparisons, swaps);
    return 0;
}
