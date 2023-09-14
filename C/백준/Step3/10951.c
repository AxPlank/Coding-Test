#include <stdio.h>

int main () {
    int A, B;
    int isEOF;

    isEOF = scanf("%d %d", &A, &B);

    while (isEOF != -1) {
        printf("%d\n", A + B);
        isEOF = scanf("%d %d", &A, &B);
    }

    return 0;
}