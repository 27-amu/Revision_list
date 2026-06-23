#include <stdio.h>

int main() {
    char s[200];
    int count = 0, inWord = 0;

    printf("Enter a sentence: ");
    fgets(s, sizeof(s), stdin);

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] != ' ' && s[i] != '\n' && s[i] != '\t') {
            if (!inWord) { count++; inWord = 1; }
        } else {
            inWord = 0;
        }
    }
    printf("Word count: %d\n", count);
    return 0;
}
