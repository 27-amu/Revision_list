#include <stdio.h>
#include <string.h>

void myStrcpy(char *dest, const char *src) {
    while ((*dest++ = *src++));
}

int main() {
    char src[200], dest[200];
    printf("Enter a string to copy: ");
    fgets(src, sizeof(src), stdin);
    int len = strlen(src);
    if (src[len-1] == '\n') src[len-1] = '\0';

    myStrcpy(dest, src);
    printf("Copied: %s\n", dest);
    return 0;
}
