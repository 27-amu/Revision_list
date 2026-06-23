#include <stdio.h>

int main() {
    int n, m;
    printf("Enter size of array 1: "); scanf("%d", &n);
    int a[n];
    printf("Enter %d sorted integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    printf("Enter size of array 2: "); scanf("%d", &m);
    int b[m];
    printf("Enter %d sorted integers: ", m);
    for (int i = 0; i < m; i++) scanf("%d", &b[i]);

    int merged[n+m], i = 0, j = 0, k = 0;
    while (i < n && j < m)
        merged[k++] = (a[i] <= b[j]) ? a[i++] : b[j++];
    while (i < n) merged[k++] = a[i++];
    while (j < m) merged[k++] = b[j++];

    printf("Merged: ");
    for (int x = 0; x < n+m; x++) printf("%d ", merged[x]);
    printf("\n");
    return 0;
}
