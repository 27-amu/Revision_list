#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) { return *(int*)a - *(int*)b; }

int main() {
    int n, k;
    printf("Enter n and k: ");
    scanf("%d %d", &n, &k);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    qsort(a, n, sizeof(int), cmp);
    printf("%dth smallest element: %d\n", k, a[k-1]);
    return 0;
}
