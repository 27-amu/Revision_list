#include <stdio.h>
#include <string.h>

void permute(char *s, int l, int r) {
    if (l == r) { printf("%s\n", s); return; }
    for (int i = l; i <= r; i++) {
        char t = s[l]; s[l] = s[i]; s[i] = t;
        permute(s, l + 1, r);
        t = s[l]; s[l] = s[i]; s[i] = t;
    }
}

int main() {
    char s[20];
    printf("Enter a string (max 8 chars): ");
    scanf("%s", s);
    printf("All permutations:\n");
    permute(s, 0, strlen(s) - 1);
    return 0;
}
