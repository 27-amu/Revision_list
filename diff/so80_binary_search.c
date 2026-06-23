#include <stdio.h>

int main() {
    int n, target;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d sorted integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Enter target: ");
    scanf("%d", &target);

    int l = 0, r = n-1;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (a[mid] == target) { printf("Found at index %d\n", mid); return 0; }
        if (a[mid] < target) l = mid + 1;
        else r = mid - 1;
    }
    printf("Not found\n");
    return 0;
}
