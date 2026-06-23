#include <stdio.h>

double mySqrt(double n) {
    double low = 0, high = (n < 1) ? 1 : n, mid;
    while (high - low > 1e-6) {
        mid = (low + high) / 2;
        if (mid * mid < n) low = mid;
        else high = mid;
    }
    return (low + high) / 2;
}

int main() {
    double n;
    printf("Enter a number: ");
    scanf("%lf", &n);
    printf("Square root of %.2f = %.6f\n", n, mySqrt(n));
    return 0;
}
