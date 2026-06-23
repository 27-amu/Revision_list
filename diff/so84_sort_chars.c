#include <stdio.h>
#include <string.h>

int main() {
    char s[200];
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    int len = strlen(s);
    if (s[len-1] == '\n') s[--len] = '\0';

    for (int i = 0; i < len-1; i++)
        for (int j = 0; j < len-i-1; j++)
            if (s[j] > s[j+1]) { char t = s[j]; s[j] = s[j+1]; s[j+1] = t; }

    printf("Sorted: %s\n", s);
    return 0;
}
