#include <stdio.h>

int main() {
	double A, B;

	scanf_s("%lf %lf", &A, &B);

	printf("%.9lf\n", A / B); // ���⼭ �ڸ��� ǥ�� ���ϸ� �⺻������ 6�ڸ����� ǥ���ϱ� ������ ���ؿ��� �������� �νĤ�

	return 0;
}