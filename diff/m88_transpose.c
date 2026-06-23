#include <stdio.h>

int main() {
    int n;
    printf("Enter matrix size (n x n): ");
    scanf("%d", &n);
    int mat[n][n];
    printf("Enter %d elements:\n", n*n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &mat[i][j]);

    printf("Transpose:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) printf("%d ", mat[j][i]);
        printf("\n");
    }
    return 0;
}
