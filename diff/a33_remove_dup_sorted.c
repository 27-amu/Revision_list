#include <stdio.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d sorted integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int j = 0;
    for (int i = 1; i < n; i++)
        if (a[i] != a[j]) a[++j] = a[i];

    printf("After removing duplicates: ");
    for (int i = 0; i <= j; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
