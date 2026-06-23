#include <stdio.h>

int strlenPtr(char *s) {
    int len = 0;
    while (*s != '\0' && *s != '\n') { len++; s++; }
    return len;
}

int main() {
    char s[200];
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    printf("Length: %d\n", strlenPtr(s));
    return 0;
}
