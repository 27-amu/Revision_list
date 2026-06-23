#include <stdio.h>
#include <string.h>

int main() {
    char s[200], word[200], longest[200] = "";
    int maxLen = 0, j = 0;

    printf("Enter a sentence: ");
    fgets(s, sizeof(s), stdin);

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] != ' ' && s[i] != '\n') {
            word[j++] = s[i];
        } else if (j > 0) {
            word[j] = '\0';
            if (j > maxLen) { maxLen = j; strcpy(longest, word); }
            j = 0;
        }
    }
    if (j > 0) { word[j] = '\0'; if (j > maxLen) strcpy(longest, word); }

    printf("Longest word: %s\n", longest);
    return 0;
}
