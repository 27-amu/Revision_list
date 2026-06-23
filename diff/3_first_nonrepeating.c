#include <stdio.h>
#include <string.h>

int main() {
    char s[200];
    int freq[256] = {0};

    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    int len = strlen(s);
    if (s[len - 1] == '\n') s[--len] = '\0';

    for (int i = 0; i < len; i++)
        freq[(unsigned char)s[i]]++;

    for (int i = 0; i < len; i++) {
        if (freq[(unsigned char)s[i]] == 1) {
            printf("%c\n", s[i]);
            return 0;
        }
    }

    printf("None\n");
    return 0;
}
