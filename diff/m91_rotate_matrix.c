#include <stdio.h>

int main() {
    int n;
    printf("Enter matrix size (n x n): ");
    scanf("%d", &n);
    int mat[n][n];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) scanf("%d", &mat[i][j]);

    // transpose
    for (int i = 0; i < n; i++)
        for (int j = i+1; j < n; j++) { int t = mat[i][j]; mat[i][j] = mat[j][i]; mat[j][i] = t; }

    // reverse each row
    for (int i = 0; i < n; i++) {
        int l = 0, r = n-1;
        while (l < r) { int t = mat[i][l]; mat[i][l] = mat[i][r]; mat[i][r] = t; l++; r--; }
    }

    printf("Rotated 90 degrees clockwise:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) printf("%d ", mat[i][j]);
        printf("\n");
    }
    return 0;
}
