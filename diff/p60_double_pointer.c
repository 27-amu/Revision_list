#include <stdio.h>
#include <stdlib.h>

void allocate(int **p, int val) {
    *p = (int *)malloc(sizeof(int));
    **p = val;
}

int main() {
    int *p = NULL;
    allocate(&p, 42);
    printf("Value set via double pointer: %d\n", *p);
    free(p);
    p = NULL;
    return 0;
}
