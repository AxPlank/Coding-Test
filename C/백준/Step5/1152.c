# include <stdio.h>
# include <string.h>
# include <ctype.h>


int main() {
    // scanset 작성할 것

    char S[1000001];
    int SLen;
    int cnt = 0;

    scanf("%[^\n]", S);
    SLen = strlen(S);

    if (SLen == 1 && S == ' ') {
        printf("0\n");

        return 0;
    }

    for (int i = 0; i < SLen; i++) {
        if (isspace(S[i])) cnt ++;
    }

    if (S[0] == ' ' && S[SLen - 1] == ' ') {
        printf("%d\n", cnt - 1);
    } else if (S[0] != ' ' && S[SLen - 1] != ' ') {
        printf("%d\n", cnt + 1);
    } else {
        printf("%d\n", cnt);
    }

    return 0;
}