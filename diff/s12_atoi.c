#include <stdio.h>

int myAtoi(char *s) {
    int result = 0, sign = 1, i = 0;
    if (s[0] == '-') { sign = -1; i = 1; }
    for (; s[i] >= '0' && s[i] <= '9'; i++)
        result = result * 10 + (s[i] - '0');
    return sign * result;
}

int main() {
    char s[50];
    printf("Enter a number string: ");
    scanf("%s", s);
    printf("Integer: %d\n", myAtoi(s));
    return 0;
}
