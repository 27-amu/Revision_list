#include <stdio.h>

int main() {
    int n, m;
    printf("Enter size of array 1: "); scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    printf("Enter size of array 2: "); scanf("%d", &m);
    int b[m];
    printf("Enter %d integers: ", m);
    for (int i = 0; i < m; i++) scanf("%d", &b[i]);

    printf("Intersection: ");
    int found = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (a[i] == b[j]) { printf("%d ", a[i]); found = 1; b[j] = -99999; break; }

    if (!found) printf("None");
    printf("\n");
    return 0;
}
