#include <stdio.h>
#include <string.h>

int main () {
    char word[101];

    scanf("%s", word);

    int wordLen = strlen(word);
    int wordMid = wordLen / 2;

    for (int i = 0; i < wordMid; i++) {
        if (word[i] != word[wordLen - 1 - i]) {
            printf("0");

            return 0;
        }
    }

    printf("1");

    return 0;
}