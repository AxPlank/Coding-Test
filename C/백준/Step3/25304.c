#include <stdio.h>

int main () {
    int T, X;
    int a, b;
    int sum = 0;
    
    scanf("%d\n", &X);
    scanf("%d\n", &T);
    
    for (int i = 0; i < T; i++) {
        scanf("%d %d\n", &a, &b);
        sum += a * b;
    }
    
    if (X == sum) printf("Yes\n");
    else printf("No\n");
    
    return 0;
}