#include <stdio.h>

int main () {
    int N;
    int sum = 0;
    
    scanf("%d", &N);
    N++;
    
    char Ns[N];
    scanf("%s", Ns);
    
    for (int i = 0; i < N - 1; i++) {
        sum += Ns[i] - '0';
    }
    
    printf("%d\n", sum);
    
    return 0;
}