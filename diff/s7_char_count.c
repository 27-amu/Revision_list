#include <stdio.h>
#include <string.h>

int main() {
    char s[200];
    int freq[256] = {0};

    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    int len = strlen(s);
    if (s[len-1] == '\n') s[--len] = '\0';

    for (int i = 0; i < len; i++)
        freq[(unsigned char)s[i]]++;

    printf("Character frequencies:\n");
    for (int i = 0; i < 256; i++)
        if (freq[i] > 0) printf("'%c' : %d\n", i, freq[i]);
    return 0;
}
