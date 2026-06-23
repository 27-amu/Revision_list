#include <stdio.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    printf("Pairs with XOR = 0 (equal pairs):\n");
    int found = 0;
    for (int i = 0; i < n; i++)
        for (int j = i+1; j < n; j++)
            if ((a[i] ^ a[j]) == 0) { printf("(%d, %d)\n", a[i], a[j]); found = 1; }

    if (!found) printf("None\n");
    return 0;
}
