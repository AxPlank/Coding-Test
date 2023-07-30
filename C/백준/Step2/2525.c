#include <stdio.h>

int main () {
    int A;
    int B, C;

    scanf("%d %d", &A, &B);
    scanf("%d", &C);

    C += B;
    A += C / 60;
    B = C % 60;
    A = A > 24 ? A - 24 : A;

    printf("%d %d", A, B);

    return 0;
}