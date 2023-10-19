# include <stdio.h>

int main () {
    int StudentNumArr[28];
    int cnt = 0;
    
    for (int i = 0; i < 28; i++) {
        scanf("%d", &StudentNumArr[i]);
    }
    
    for (int i = 1; i < 31; i++) {
        for (int j = 0; j < 28; j++) {
            if (i == StudentNumArr[j]) {
                break;
            }
            
            if (j == 27) {
                printf("%d\n", i);
                cnt++;
            }
        }
        
        if (cnt == 2) break;
    }
    
    return 0;
}