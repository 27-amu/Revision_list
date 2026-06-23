#include <stdio.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int total = 0;
    for (int i = 0; i < n; i++) total += a[i];

    int leftSum = 0;
    for (int i = 0; i < n; i++) {
        total -= a[i];
        if (leftSum == total) { printf("Equilibrium index: %d\n", i); return 0; }
        leftSum += a[i];
    }
    printf("No equilibrium index\n");
    return 0;
}
