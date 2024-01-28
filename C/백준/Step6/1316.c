#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isGW (char *start, char *mid, char *end);

int main () {
    int N;
    char word[101];
    int wordLen;
    
    scanf("%d", &N);
    int cnt = N;

    for (int i = 0; i < N; i++) {
        scanf("%s", word);
        wordLen = strlen(word) - 1;

        for (int j = 0; j < wordLen; j++) {
            if (word[j] != word[j+1]) {
                if (!isGW(&word[j], &word[j+2], &word[wordLen])) {
                    cnt--;

                    break;
                }
            }
        }
    }

    printf("%d\n", cnt);
    
    return 0;
}

bool isGW (char *start, char *mid, char *end) {
    while (mid <= end) {
        if (*start == *mid) {
            return false;
        } else {
            mid++;
        }
    }

    return true;
}