#include <stdio.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int pos = 0;
    for (int i = 0; i < n; i++)
        if (a[i] != 0) a[pos++] = a[i];
    while (pos < n) a[pos++] = 0;

    printf("After moving zeros: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
