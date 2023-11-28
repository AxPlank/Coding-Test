# include <stdio.h>

int main() {
    int ChessUnits[] = {1, 1, 2, 2, 2, 8};
    int InputUnits[6];
    
    for (int i = 0; i < 6; i++) {
        scanf("%d ", &InputUnits[i]);
    }
    
    for (int i = 0; i < 6; i++) {
        printf("%d ", ChessUnits[i] - InputUnits[i]);
    }
    
    return 0;
}