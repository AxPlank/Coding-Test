#include <stdio.h>
#include <string.h>

int main () {
    char strInput[101];
    
    scanf("%s", strInput);
    
    printf("%d", strlen(strInput));
    
    return 0;
}