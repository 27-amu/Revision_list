#include <stdio.h>

void rev(int *a, int l, int r) {
    while (l < r) { int t = a[l]; a[l] = a[r]; a[r] = t; l++; r--; }
}

int main() {
    int n, k;
    printf("Enter n and k (rotate by k): ");
    scanf("%d %d", &n, &k);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    k = k % n;
    rev(a, 0, n-1); rev(a, 0, k-1); rev(a, k, n-1);

    printf("After rotating by %d: ", k);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
