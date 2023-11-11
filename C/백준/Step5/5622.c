#include <stdio.h>
#include <string.h>

int getTime(char alphabet);

int main() {
    char word[16];
    int wordLen;
    int time = 0;
    
    scanf("%s", word);
    wordLen = strlen(word);
    
    for (int i = 0; i < wordLen; i++) {
        time += getTime(word[i]);
    }
    
    printf("%d\n", time);
    
    return 0;
}

int getTime(char alphabet) {
    if (alphabet >= 65 && alphabet <= 67) {
        return 3;
    } else if (alphabet >= 68 && alphabet <= 70) {
        return 4;
    } else if (alphabet >= 71 && alphabet <= 73) {
        return 5;
    } else if (alphabet >= 74 && alphabet <= 76) {
        return 6;
    } else if (alphabet >= 77 && alphabet <= 79) {
        return 7;
    } else if (alphabet >= 80 && alphabet <= 83) {
        return 8;
    } else if (alphabet >= 84 && alphabet <= 86) {
        return 9;
    } else if (alphabet >= 87 && alphabet <= 90) {
        return 10;
    }
}