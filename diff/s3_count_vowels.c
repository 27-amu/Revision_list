#include <stdio.h>
#include <ctype.h>

int main() {
    char s[200];
    int vowels = 0, consonants = 0;
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);

    for (int i = 0; s[i] != '\0'; i++) {
        char c = tolower(s[i]);
        if (c >= 'a' && c <= 'z') {
            if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u') vowels++;
            else consonants++;
        }
    }
    printf("Vowels: %d, Consonants: %d\n", vowels, consonants);
    return 0;
}
