# include <stdio.h>

int main () {
    int N, X;
    int n;
    int Arr[10000];
    
    scanf("%d %d", &N, &X);
    for (int i = 0; i < N; i++) {
        scanf("%d", &Arr[i]);
    }
    
    for (int i = 0; i < N; i++) {
        if (X > Arr[i]) {
            printf("%d ", Arr[i]);
        }
    }
    
    return 0;
}