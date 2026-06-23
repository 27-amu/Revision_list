#include <stdio.h>

int bSearch(int *a, int l, int r, int target) {
    if (l > r) return -1;
    int mid = (l + r) / 2;
    if (a[mid] == target) return mid;
    if (a[mid] > target) return bSearch(a, l, mid-1, target);
    return bSearch(a, mid+1, r, target);
}

int main() {
    int n, target;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d sorted integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Enter target: ");
    scanf("%d", &target);

    int idx = bSearch(a, 0, n-1, target);
    printf(idx == -1 ? "Not found\n" : "Found at index %d\n", idx);
    return 0;
}
