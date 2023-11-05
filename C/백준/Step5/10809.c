# include <stdio.h>
# include <string.h>

int main () {
    char S[101];
    int alphabetArr[26];
    
    for (int i = 0; i < 26; i++) {
        alphabetArr[i] = -1;
    }
    
    scanf("%s", S);
    int Slen = strlen(S);
    
    for (int i = 0; i < Slen; i++) {
        if (alphabetArr[(int)S[i] - (int)'a'] == -1) alphabetArr[(int)S[i] - (int)'a'] = i;
    }
    
    for (int i = 0; i < 26; i++) {
        printf("%d ", alphabetArr[i]);
    }
    
    printf("\n");
    
    return 0;
}