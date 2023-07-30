#include <stdio.h>

int main () {
    int x, y;

    scanf("%d", &x);
    scanf("%d", &y);

    if (x > 0) {
        y > 0 ? printf("1") : printf("4");
    } else {
        y > 0 ? printf("2") : printf("3");
    }

    return 0;
}