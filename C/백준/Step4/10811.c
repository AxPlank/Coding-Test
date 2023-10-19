#include <stdio.h>

int main() {
    int N, M;
    
    scanf("%d %d", &N, &M);
    
    int Boxes[N];
    int MArr[2];
    
    for (int i = 0; i < N; i++) {
        Boxes[i] = i + 1;
    }
    
    for (int i = 0; i < M; i++) {
        scanf("%d %d", &MArr[0], &MArr[1]);
        int reverseArr[MArr[1] - MArr[0] + 1];
        
        for (int j = 0; j < MArr[1] - MArr[0] + 1; j++) {
            reverseArr[j] = Boxes[MArr[1] - j - 1];
        }
        
        for (int j = 0; j < MArr[1] - MArr[0] + 1; j++) {
            Boxes[j + MArr[0] - 1] = reverseArr[j];
        }
    }
    
    for (int i = 0; i < N; i++) {
        printf("%d ", Boxes[i]);
    }
    
    return 0;
}