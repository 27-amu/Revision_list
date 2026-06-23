#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char line[200], clean[200];
    int j = 0;

    printf("Enter a string: ");
    fgets(line, sizeof(line), stdin);

    for (int i = 0; line[i] != '\0'; i++) {
        if (line[i] != ' ' && line[i] != '\n')
            clean[j++] = tolower(line[i]);
    }
    clean[j] = '\0';

    int left = 0, right = j - 1, is_palindrome = 1;
    while (left < right) {
        if (clean[left] != clean[right]) {
            is_palindrome = 0;
            break;
        }
        left++;
        right--;
    }

    printf("%s\n", is_palindrome ? "Palindrome" : "Not a palindrome");
    return 0;
}
