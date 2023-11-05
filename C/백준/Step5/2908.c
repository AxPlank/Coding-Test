# include <stdio.h>
# include <string.h>

int getNum(char num[4]) {
    int number = (num[0] - '0') + 10 * (num[1] - '0') + 100 * (num[2] - '0');

    return number;
}

int main() {
    char str1[4], str2[4];
    int num1, num2;

    scanf("%s %s", str1, str2);

    num1 = getNum(str1);
    num2 = getNum(str2);

    if (num1 >= num2) {
        printf("%d\n", num1);
    } else {
        printf("%d\n", num2);
    }

    return 0;
}