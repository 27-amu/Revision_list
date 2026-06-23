#include <stdio.h>

int multiply(int a, int b) {
    if (b == 0) return 0;
    if (b < 0) return -multiply(a, -b);
    return a + multiply(a, b - 1);
}

int main() {
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    printf("%d x %d = %d\n", a, b, multiply(a, b));
    return 0;
}
