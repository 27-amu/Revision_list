#include <stdio.h>
#include <limits.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int maxSum = INT_MIN, currSum = 0;
    for (int i = 0; i < n; i++) {
        currSum += a[i];
        if (currSum > maxSum) maxSum = currSum;
        if (currSum < 0) currSum = 0;
    }
    printf("Maximum subarray sum: %d\n", maxSum);
    return 0;
}
