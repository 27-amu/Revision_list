#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) { return *(int*)a - *(int*)b; }

int main() {
    int n, target;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n], sorted[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) { scanf("%d", &a[i]); sorted[i] = a[i]; }
    printf("Enter target: ");
    scanf("%d", &target);

    qsort(sorted, n, sizeof(int), cmp);

    for (int i = 0; i < n; i++)
        if (sorted[i] == target) { printf("Position of %d after sorting: index %d\n", target, i); return 0; }

    printf("Not found\n");
    return 0;
}
