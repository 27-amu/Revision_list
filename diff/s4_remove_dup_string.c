#include <stdio.h>
#include <string.h>

int main() {
    char s[200], result[200];
    int seen[256] = {0}, j = 0;

    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    int len = strlen(s);
    if (s[len-1] == '\n') s[--len] = '\0';

    for (int i = 0; i < len; i++) {
        if (!seen[(unsigned char)s[i]]) {
            seen[(unsigned char)s[i]] = 1;
            result[j++] = s[i];
        }
    }
    result[j] = '\0';
    printf("After removing duplicates: %s\n", result);
    return 0;
}
