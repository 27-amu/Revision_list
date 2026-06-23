#include <stdio.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    printf("Duplicates: ");
    int found = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (a[i] == a[j]) { printf("%d ", a[i]); found = 1; break; }

    if (!found) printf("None");
    printf("\n");
    return 0;
}
