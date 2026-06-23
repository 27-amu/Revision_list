#include <stdio.h>
#include <string.h>

int main() {
    int n;
    printf("Enter number of strings: ");
    scanf("%d", &n);
    getchar();

    char words[n][100];
    for (int i = 0; i < n; i++) {
        printf("Enter string %d: ", i+1);
        fgets(words[i], sizeof(words[i]), stdin);
        int len = strlen(words[i]);
        if (words[i][len-1] == '\n') words[i][len-1] = '\0';
    }

    char prefix[100];
    strcpy(prefix, words[0]);

    for (int i = 1; i < n; i++) {
        int j = 0;
        while (prefix[j] && words[i][j] && prefix[j] == words[i][j]) j++;
        prefix[j] = '\0';
    }

    if (prefix[0] == '\0') printf("No common prefix\n");
    else printf("Longest common prefix: %s\n", prefix);
    return 0;
}
