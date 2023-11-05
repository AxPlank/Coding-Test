#include <stdio.h>
#include <string.h>

int main () {
    int T;
    char strInput[1001];
    
    scanf("%d", &T);
    
    for (int i = 0; i < T; i++) {
        scanf("%s", strInput);
        printf("%c%c\n", strInput[0], strInput[strlen(strInput)-1]);
    }
    
    return 0;
}