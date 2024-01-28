#include <stdio.h>
#include <string.h>

float getScore (char score[3]);

int main () {
    char subject[51];
    float credit;
    char score[3];
    float demo = 0.0, nume = 0.0;

    for (int i = 0; i < 1; i++) {
        scanf("%s %f %s", subject, &credit, score);

        if (score[0] != 'P') {
            demo += credit;
            nume += credit * getScore(score);
        }
    }

    printf("%f\n", nume / demo);
    
    return 0;
}

float getScore (char score[3]) {
    printf("%s\t%d\n", score, strcmp(score, "A+"));
    if (strcmp(score, "A+") == 0) {
        printf("4.5\n");
        return 4.5;
    } else if (strcmp(score, "A0") == 0) {
        return 4.0;
    } else if (strcmp(score, "B+") == 0) {
        return 3.5;
    } else if (strcmp(score, "B0") == 0) {
        return 3.0;
    } else if (strcmp(score, "C+") == 0) {
        return 2.5;
    } else if (strcmp(score, "C0") == 0) {
        return 2.0;
    } else if (strcmp(score, "D+") == 0) {
        return 1.5;
    } else if (strcmp(score, "D0") == 0) {
        return 1.0;
    } else {
        return 0.0;
    }
}