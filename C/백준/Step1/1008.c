#include <stdio.h>

int main() {
	double A, B;

	scanf_s("%lf %lf", &A, &B);

	printf("%.9lf\n", A / B); // 여기서 자리수 표시 안하면 기본적으로 6자리까지 표시하기 때문에 백준에선 오답으로 인식ㄹ

	return 0;
}