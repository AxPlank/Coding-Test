#include <stdio.h>
#include <string.h>

int main () {
    char word[1000001], maxAlphabet;
    int wordLen, cntArr[26];
    int maxNum = -1;
    int cnt = 0;

    scanf("%s", word);

    wordLen = strlen(word);

    for (int i = 0; i < wordLen; i++) {
        if (word[i] >= 97) {
            word[i] -= 32;
        }

        cntArr[word[i]-65]++;
    }

    for (int i = 0; i < 26; i++) {
        if (cntArr[i] > maxNum) {
            maxAlphabet = i + 65;
            maxNum = cntArr[i];
            cnt = 1;
        } else if (cntArr[i] == maxNum) {
            cnt++;
        }
    }

    cnt == 1?printf("%c\n", maxAlphabet) : printf("?\n");

    return 0;
}