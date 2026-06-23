#include <stdio.h>

void myItoa(int n, char *s) {
    int i = 0, neg = 0;
    if (n < 0) { neg = 1; n = -n; }
    if (n == 0) { s[i++] = '0'; }
    while (n > 0) { s[i++] = '0' + n % 10; n /= 10; }
    if (neg) s[i++] = '-';
    s[i] = '\0';
    int l = 0, r = i - 1;
    while (l < r) { char t = s[l]; s[l] = s[r]; s[r] = t; l++; r--; }
}

int main() {
    int n;
    char s[50];
    printf("Enter an integer: ");
    scanf("%d", &n);
    myItoa(n, s);
    printf("String: %s\n", s);
    return 0;
}
