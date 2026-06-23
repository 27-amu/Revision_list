#include <stdio.h>

int add(int a, int b)      { return a + b; }
int subtract(int a, int b) { return a - b; }
int multiply(int a, int b) { return a * b; }

int main() {
    int (*op)(int, int);
    int a, b, choice;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    printf("1. Add  2. Subtract  3. Multiply\nChoice: ");
    scanf("%d", &choice);

    if (choice == 1) op = add;
    else if (choice == 2) op = subtract;
    else op = multiply;

    printf("Result: %d\n", op(a, b));
    return 0;
}
