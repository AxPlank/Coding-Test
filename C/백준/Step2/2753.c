#include <stdio.h>

int main () {
    int year;
    int m1, m2, m3;

    scanf("%d", &year);

    m1 = year % 4;
    m1 = year % 100;
    m1 = year % 400;

    if ((m1 == 0 && m2 != 0) || m3 == 0) {
        printf("1");
    } else {
        printf("0");
    }

    return 0;
}