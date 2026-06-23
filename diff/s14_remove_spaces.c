#include <stdio.h>
#include <string.h>

int main() {
    char s[200], result[200];
    int j = 0;

    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    int len = strlen(s);

    for (int i = 0; i < len; i++)
        if (s[i] != ' ' && s[i] != '\n') result[j++] = s[i];
    result[j] = '\0';

    printf("Without spaces: %s\n", result);
    return 0;
}
