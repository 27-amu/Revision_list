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

    int maxFreq = 0; char maxChar = s[0];
    for (int i = 0; i < 256; i++)
        if (freq[i] > maxFreq) { maxFreq = freq[i]; maxChar = (char)i; }

    printf("Most frequent: '%c' (%d times)\n", maxChar, maxFreq);
    return 0;
}
