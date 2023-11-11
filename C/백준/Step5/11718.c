#include <stdio.h>

int main () {
    char string[101];
    
    while (scanf("%[^\n]", string) != EOF) {
        printf("%s\n", string);
        getchar();
    }
    
    return 0;
}