#include <stdio.h>

int main() {
    int a[] = {10, 20, 30, 40, 50};
    int n = 5;
    int *p = a;

    printf("Accessing array using pointer arithmetic:\n");
    for (int i = 0; i < n; i++)
        printf("a[%d] = %d  |  *(p+%d) = %d\n", i, a[i], i, *(p+i));

    printf("\nPointer moves by %lu bytes per step (sizeof int)\n", sizeof(int));
    return 0;
}
