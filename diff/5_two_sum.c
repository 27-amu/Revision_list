#include <stdio.h>

int main() {
    int n, target;
    printf("Enter n: ");
    scanf("%d", &n);

    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);

    printf("Enter target: ");
    scanf("%d", &target);

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] + a[j] == target) {
                printf("Pair found: %d %d\n", a[i], a[j]);
                return 0;
            }
        }
    }

    printf("No pair found\n");
    return 0;
}
