#include <stdio.h>

void reversePtr(int *a, int n) {
    int *l = a, *r = a + n - 1;
    while (l < r) { int t = *l; *l = *r; *r = t; l++; r--; }
}

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    reversePtr(a, n);
    printf("Reversed: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
