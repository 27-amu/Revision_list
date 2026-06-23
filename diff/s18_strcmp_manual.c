#include <stdio.h>
#include <string.h>

int myStrcmp(char *s1, char *s2) {
    while (*s1 && *s2 && *s1 == *s2) { s1++; s2++; }
    return *s1 - *s2;
}

int main() {
    char s1[200], s2[200];
    printf("Enter string 1: ");
    fgets(s1, sizeof(s1), stdin);
    printf("Enter string 2: ");
    fgets(s2, sizeof(s2), stdin);

    int l1 = strlen(s1), l2 = strlen(s2);
    if (s1[l1-1] == '\n') s1[l1-1] = '\0';
    if (s2[l2-1] == '\n') s2[l2-1] = '\0';

    int r = myStrcmp(s1, s2);
    if (r == 0) printf("Strings are equal\n");
    else if (r < 0) printf("String 1 is smaller\n");
    else printf("String 1 is greater\n");
    return 0;
}
