# include <stdio.h>

int main () {
    int N;
    
    scanf("%d", &N);
    int Arr[1000000]; // 실제로는 Arr의 길이에 N을 넣고 풀이하였음
    for (int i = 0; i < N; i++) {
        scanf("%d", &Arr[i]);
    }

    int max = Arr[0];
    int min = Arr[0];
    for (int i = 0; i < N; i++) {
        if (max < Arr[i]) {
            max = Arr[i];
        }
        
        if (min > Arr[i]) {
            min = Arr[i];
        }
    }
    
    printf("%d %d\n", min, max);
    
    return 0;
}