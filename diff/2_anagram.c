#include <stdio.h>
#include <ctype.h>

int main() {
    char s1[200], s2[200];
    int count[256] = {0};

    printf("Enter first string:  ");
    fgets(s1, sizeof(s1), stdin);
    printf("Enter second string: ");
    fgets(s2, sizeof(s2), stdin);

    for (int i = 0; s1[i] != '\0'; i++)
        if (s1[i] != '\n') count[(unsigned char)tolower(s1[i])]++;

    for (int i = 0; s2[i] != '\0'; i++)
        if (s2[i] != '\n') count[(unsigned char)tolower(s2[i])]--;

    for (int i = 0; i < 256; i++) {
        if (count[i] != 0) {
            printf("Not anagram\n");
            return 0;
        }
    }

    printf("Anagram\n");
    return 0;
}
