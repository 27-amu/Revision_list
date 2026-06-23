#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char line[200], clean[200];
    int j = 0;
    printf("Enter a string: ");
    fgets(line, sizeof(line), stdin);

    for (int i = 0; line[i] != '\0'; i++)
        if (line[i] != ' ' && line[i] != '\n')
            clean[j++] = tolower(line[i]);
    clean[j] = '\0';

    int l = 0, r = j - 1, ok = 1;
    while (l < r) {
        if (clean[l] != clean[r]) { ok = 0; break; }
        l++; r--;
    }
    printf("%s\n", ok ? "Palindrome" : "Not a palindrome");
    return 0;
}
