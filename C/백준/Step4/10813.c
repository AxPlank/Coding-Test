# include <stdio.h>

int main() {
    int N, M;
    int ij[2];
    int tmp;

    scanf("%d %d", &N, &M);

    int Box[100]; // 실제로는 100대신 N을 대입하여 Array 구성

    for (int i = 0; i < N; i++) {
        Box[i] = i + 1;
    }

    for (int i = 0; i < M; i++) {
        scanf("%d %d", &ij[0], &ij[1]);

        if (ij[0] != ij[1]) {
            tmp = Box[ij[0] - 1];
            Box[ij[0] - 1] = Box[ij[1] - 1];
            Box[ij[1] - 1] = tmp;
        }
    }

    for (int i = 0; i < N; i++) {
        printf("%d ", Box[i]);
    }

    return 0;
}