#include <stdio.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int candidate = a[0], count = 1;
    for (int i = 1; i < n; i++) {
        if (a[i] == candidate) count++;
        else if (--count == 0) { candidate = a[i]; count = 1; }
    }

    count = 0;
    for (int i = 0; i < n; i++) if (a[i] == candidate) count++;

    if (count > n / 2) printf("Majority element: %d\n", candidate);
    else printf("No majority element\n");
    return 0;
}
