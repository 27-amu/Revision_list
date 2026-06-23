#include <stdio.h>

int main() {
    int n;
    printf("Enter matrix size (n x n): ");
    scanf("%d", &n);
    int mat[n][n];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) scanf("%d", &mat[i][j]);

    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += mat[i][i];
        if (i != n-1-i) sum += mat[i][n-1-i];
    }
    printf("Diagonal sum: %d\n", sum);
    return 0;
}
