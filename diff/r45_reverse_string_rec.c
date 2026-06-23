#include <stdio.h>
#include <string.h>

void reverseRec(char *s, int l, int r) {
    if (l >= r) return;
    char t = s[l]; s[l] = s[r]; s[r] = t;
    reverseRec(s, l+1, r-1);
}

int main() {
    char s[200];
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    int len = strlen(s);
    if (s[len-1] == '\n') s[--len] = '\0';

    reverseRec(s, 0, len-1);
    printf("Reversed: %s\n", s);
    return 0;
}
