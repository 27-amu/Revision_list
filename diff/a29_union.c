#include <stdio.h>

int inArr(int *a, int n, int x) {
    for (int i = 0; i < n; i++) if (a[i] == x) return 1;
    return 0;
}

int main() {
    int n, m;
    printf("Enter size of array 1: "); scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    printf("Enter size of array 2: "); scanf("%d", &m);
    int b[m];
    printf("Enter %d integers: ", m);
    for (int i = 0; i < m; i++) scanf("%d", &b[i]);

    int result[n+m], r = 0;
    for (int i = 0; i < n; i++) if (!inArr(result, r, a[i])) result[r++] = a[i];
    for (int i = 0; i < m; i++) if (!inArr(result, r, b[i])) result[r++] = b[i];

    printf("Union: ");
    for (int i = 0; i < r; i++) printf("%d ", result[i]);
    printf("\n");
    return 0;
}
