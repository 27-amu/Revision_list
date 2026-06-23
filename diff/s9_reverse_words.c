#include <stdio.h>
#include <string.h>

void rev(char *s, int l, int r) {
    while (l < r) { char t = s[l]; s[l] = s[r]; s[r] = t; l++; r--; }
}

int main() {
    char s[200];
    printf("Enter a sentence: ");
    fgets(s, sizeof(s), stdin);
    int len = strlen(s);
    if (s[len-1] == '\n') s[--len] = '\0';

    rev(s, 0, len - 1);

    int start = 0;
    for (int i = 0; i <= len; i++) {
        if (s[i] == ' ' || s[i] == '\0') {
            rev(s, start, i - 1);
            start = i + 1;
        }
    }
    printf("Reversed words: %s\n", s);
    return 0;
}
