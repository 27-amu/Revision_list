#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = (int *)malloc(sizeof(int));
    *p = 10;
    printf("Before free: %d\n", *p);

    free(p);
    p = NULL;  // set to NULL after free — prevents dangling pointer

    if (p == NULL)
        printf("Pointer is NULL — safe, no dangling pointer\n");

    /*
     * BAD (never do this):
     *   free(p);
     *   printf("%d", *p);  // dangling pointer — undefined behavior / crash
     */
    return 0;
}
