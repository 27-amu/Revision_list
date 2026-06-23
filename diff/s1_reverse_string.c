#include <stdio.h>
#include <string.h>

int main() {
    char s[200];
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    int len = strlen(s);
    if (s[len-1] == '\n') s[--len] = '\0';

    int left = 0, right = len - 1;
    while (left < right) {
        char t = s[left]; s[left] = s[right]; s[right] = t;
        left++; right--;
    }
    printf("Reversed: %s\n", s);
    return 0;
}
