# include <stdio.h>

int main() {
    int N, M;
    int ijkArr[3];

    scanf("%d %d", &N, &M);

    int Box[100]; // 실제로는 N을 대입하여 Array 정의

    for (int i = 0; i < N; i++) {
        Box[i] = 0;
    }

    for (int i = 0; i < M; i++) {
        scanf("%d %d %d", &ijkArr[0], &ijkArr[1], &ijkArr[2]);

        if (ijkArr[0] == ijkArr[1]) {
            Box[ijkArr[0] - 1] = ijkArr[2];
        }
        else {
            for (int j = ijkArr[0] - 1; j < ijkArr[1]; j++) {
                Box[j] = ijkArr[2];
            }
        }
    }

    for (int i = 0; i < N; i++) {
        printf("%d ", Box[i]);
    }

    return 0;
}