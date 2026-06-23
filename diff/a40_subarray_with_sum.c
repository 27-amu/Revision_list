#include <stdio.h>

int main() {
    int n, target;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Enter target sum: ");
    scanf("%d", &target);

    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += a[j];
            if (sum == target) {
                printf("Subarray found from index %d to %d\n", i, j);
                return 0;
            }
        }
    }
    printf("No subarray found\n");
    return 0;
}
