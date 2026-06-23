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

    int l = 0, r = n-1, result = -1;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (a[mid] == target) { result = mid; r = mid - 1; }
        else if (a[mid] < target) l = mid + 1;
        else r = mid - 1;
    }

    if (result == -1) printf("Not found\n");
    else printf("First occurrence at index %d\n", result);
    return 0;
}
