// Sol 1
#include <stdio.h>

int main () {
    char strInput[1001];
    int strIdx;
    
    scanf("%s", strInput);
    scanf("%d", &strIdx);
    
    printf("%c", strInput[strIdx-1]);
    
    return 0;
}

// Sol 2