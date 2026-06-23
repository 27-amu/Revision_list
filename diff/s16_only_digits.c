#include <stdio.h>
#include <string.h>

int main() {
    char s[200];
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    int len = strlen(s);
    if (s[len-1] == '\n') s[--len] = '\0';

    int ok = 1;
    for (int i = 0; i < len; i++)
        if (s[i] < '0' || s[i] > '9') { ok = 0; break; }

    printf("%s\n", ok ? "Contains only digits" : "Contains non-digit characters");
    return 0;
}
