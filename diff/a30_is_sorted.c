#include <stdio.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int sorted = 1;
    for (int i = 0; i < n-1; i++)
        if (a[i] > a[i+1]) { sorted = 0; break; }

    printf("%s\n", sorted ? "Array is sorted" : "Array is not sorted");
    return 0;
}
