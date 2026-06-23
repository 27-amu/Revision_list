#include <stdio.h>
#include <string.h>

int main() {
    char s1[200], s2[200], doubled[400];

    printf("Enter string 1: ");
    fgets(s1, sizeof(s1), stdin);
    printf("Enter string 2: ");
    fgets(s2, sizeof(s2), stdin);

    int l1 = strlen(s1), l2 = strlen(s2);
    if (s1[l1-1] == '\n') s1[--l1] = '\0';
    if (s2[l2-1] == '\n') s2[--l2] = '\0';

    if (l1 != l2) { printf("Not a rotation\n"); return 0; }

    strcpy(doubled, s1);
    strcat(doubled, s1);

    printf(strstr(doubled, s2) ? "Rotation\n" : "Not a rotation\n");
    return 0;
}
