#include <stdio.h>

int main() {
    int r, c;
    printf("Enter rows and columns: ");
    scanf("%d %d", &r, &c);
    int mat[r][c];
    printf("Enter %d matrix elements:\n", r*c);
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            scanf("%d", &mat[i][j]);

    int count = 0;
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            if (mat[i][j] < 0) count++;

    printf("Count of negative numbers: %d\n", count);
    return 0;
}
