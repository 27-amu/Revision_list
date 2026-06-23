#include <stdio.h>

int main() {
    int r, c, target;
    printf("Enter rows and columns: ");
    scanf("%d %d", &r, &c);
    int mat[r][c];
    printf("Enter matrix (sorted row-wise and column-wise):\n");
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) scanf("%d", &mat[i][j]);
    printf("Enter target: ");
    scanf("%d", &target);

    int row = 0, col = c-1;
    while (row < r && col >= 0) {
        if (mat[row][col] == target) { printf("Found at row %d, col %d\n", row, col); return 0; }
        if (mat[row][col] > target) col--;
        else row++;
    }
    printf("Not found\n");
    return 0;
}
