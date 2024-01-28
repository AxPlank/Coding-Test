#include <stdio.h>

int main () {
    int N, M;
    scanf("%d %d", &N, &M);

    int ret[N][M];

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            scanf("%d", &ret[i][j]);
        }
    }

    int tmp;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            scanf("%d", &tmp);
            ret[i][j] += tmp;

            printf("%d ", ret[i][j]);
        }

        printf("\n");
    }

    return 0;
}