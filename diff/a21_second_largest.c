#include <stdio.h>
#include <limits.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int largest = INT_MIN, second = INT_MIN;

    for (int i = 0; i < n; i++) {
        int x; scanf("%d", &x);
        if (x > largest) { second = largest; largest = x; }
        else if (x > second && x != largest) second = x;
    }

    if (second == INT_MIN) printf("No second largest\n");
    else printf("Second largest: %d\n", second);
    return 0;
}
