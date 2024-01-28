#include <stdio.h>
#include <string.h>

int main () {
    // Sol 1
    char word[101];
    int wordLen;

    scanf("%s", word);
    wordLen = strlen(word);
    int cnt = wordLen;

    for (int i = 0; i < wordLen; i++) {
        if (word[i] == '=') {
            if (word[i-1] == 'c' || word[i-1] == 's' || word[i-1] == 'z') {
                word[i-1] == 'z' && word[i-2] == 'd' ? cnt -=2 : cnt--;
            }
        }
        
        if (word[i] == '-') {
            if (word[i-1] == 'c' || word[i-1] == 'd') {
                cnt--;
            }
        }
        
        if (word[i] == 'j') {
            if (word[i-1] == 'l' || word[i-1] == 'n') {
                cnt--;
            }
        }
    }

    printf("%d\n", cnt);

    // Sol 2
    char word[101];
    int wordLen, cnt = 0;

    scanf("%s", word);
    wordLen = strlen(word);

    for (int i = 0; i < wordLen; i++) {
        cnt++;

        if (word[i] == 'c') {
            if (word[i+1] == '-' || word[i+1] == '=') {
                i++;

                continue;
            }
        }

        if (word[i] == 'd') {
            if (word[i+1] == '-') {
                i++;
                
                continue;
            }

            if (word[i+1] == 'z' && word[i+2] == '=') {
                i += 2;
                
                continue;
            }
        }

        if (word[i] == 'l' || word[i] == 'n') {
            if (word[i+1] == 'j') {
                i++;
                
                continue;
            }
        }

        if (word[i] == 's' || word[i] == 'z') {
            if (word[i+1] == '=') {
                i++;
                
                continue;
            }
        }
    }

    printf("%d\n", cnt);

    return 0;
}