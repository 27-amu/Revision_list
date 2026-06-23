#include <stdio.h>
#include <math.h>

int main() {
    int n, temp, digits = 0, sum = 0;
    printf("Enter a number: ");
    scanf("%d", &n);

    temp = n;
    while (temp) { digits++; temp /= 10; }

    temp = n;
    while (temp) {
        int d = temp % 10;
        sum += (int)pow(d, digits);
        temp /= 10;
    }
    printf("%d is %san Armstrong number\n", n, sum == n ? "" : "not ");
    return 0;
}
