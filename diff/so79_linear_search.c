#include <stdio.h>

int main() {
    int n, target;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Enter target: ");
    scanf("%d", &target);

    for (int i = 0; i < n; i++)
        if (a[i] == target) { printf("Found at index %d\n", i); return 0; }

    printf("Not found\n");
    return 0;
}
