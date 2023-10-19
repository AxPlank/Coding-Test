# include <stdio.h>

int main () {
    int remainderArr[42] = {0};
    int NumArr[10];
    int NumCnt = 0;
    
    for (int i = 0; i < 10; i++) {
        scanf("%d", &NumArr[i]);
        remainderArr[NumArr[i] % 42]++;
        
        if (remainderArr[NumArr[i] % 42] == 1) NumCnt++;
    }
    
    printf("%d", NumCnt);
    
    return 0;
}