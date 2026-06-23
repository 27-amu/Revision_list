#include <stdio.h>
#include <string.h>

int isPalin(char *s, int l, int r) {
    if (l >= r) return 1;
    if (s[l] != s[r]) return 0;
    return isPalin(s, l+1, r-1);
}

int main() {
    char s[200];
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    int len = strlen(s);
    if (s[len-1] == '\n') s[--len] = '\0';

    printf("%s\n", isPalin(s, 0, len-1) ? "Palindrome" : "Not a palindrome");
    return 0;
}
