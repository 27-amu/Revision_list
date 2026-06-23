#include <stdio.h>

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }

int main() {
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    printf("LCM(%d, %d) = %d\n", a, b, (a / gcd(a, b)) * b);
    return 0;
}
