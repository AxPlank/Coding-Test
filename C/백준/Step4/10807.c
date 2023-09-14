# include <stdio.h>

int main () {
    int N;
    int Arr[100];
    int v;
    int cnt = 0;
    
    scanf("%d", &N);
    
    for (int i = 0; i < N; i++) {
        scanf("%d", &Arr[i]);
    }
    
    scanf("%d", &v);
    
    for (int i = 0; i < N; i++) {
        if (v == Arr[i]) {
            cnt++;
        }
    }
    
    printf("%d\n", cnt);
    
    return 0;
}