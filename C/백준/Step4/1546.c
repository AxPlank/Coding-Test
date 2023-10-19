#include <stdio.h>

int main () {
    int N;
    double max = 0;
    double sum = 0;
    
    scanf("%d", &N);
    double scoreArr[N];
    
    for (int i = 0; i < N; i++) {
        scanf("%lf", &scoreArr[i]);
        if (scoreArr[i] > max) max = scoreArr[i];
    }
    
    for (int i = 0; i < N; i++) {
        scoreArr[i] = 100 * scoreArr[i] / max;
        sum = sum + scoreArr[i];
    }
    
    printf("%lf", sum / N);
    
    return 0;
}