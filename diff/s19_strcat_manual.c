#include <stdio.h>
#include <string.h>

void myStrcat(char *dest, char *src) {
    while (*dest) dest++;
    while (*src) *dest++ = *src++;
    *dest = '\0';
}

int main() {
    char s1[400], s2[200];
    printf("Enter string 1: ");
    fgets(s1, sizeof(s1), stdin);
    printf("Enter string 2: ");
    fgets(s2, sizeof(s2), stdin);

    int l1 = strlen(s1), l2 = strlen(s2);
    if (s1[l1-1] == '\n') s1[l1-1] = '\0';
    if (s2[l2-1] == '\n') s2[l2-1] = '\0';

    myStrcat(s1, s2);
    printf("Concatenated: %s\n", s1);
    return 0;
}
