# include <stdio.h>

int main () {
    int Arr[9];
    int maxValue = 0;
    int maxIdx = 0;
    
    for (int i = 1; i < 10; i++) {
        scanf("%d", &Arr[i-1]);
        if (Arr[i-1] > maxValue) {
            maxValue = Arr[i-1];
            maxIdx = i;
        }
    }
    
    printf("%d\n%d\n", maxValue, maxIdx);
}