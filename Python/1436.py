import sys

N = int(sys.stdin.readline().strip())
num = 666
cnt = 1

while True:
    """
    두 개의 출력 조건을 만족하는지 확인할 if문. 
    두 조건 모두 만족한다면 num을 출력하고 함수를 종료한다. 아래의 조건이 출력 조건이다.
    1. str(num)에 666이 포함되어 있어야 할 것
    2. cnt의 값이 N과 동일할 것
    """
    if '666' in str(num) and cnt == N:
        print(num)
        break
    """
    두 출력 조건을 만족하지 않는 수 중, 조건 1만 만족하는 수를 확인하기 위한 if문
    조건 1만 만족한다면 cnt도 1 증가시킬 것이며, 조건 1도 만족하지 않는 num이라면 num만 1 증가시킨다.
    """
    if '666' in str(num):
        cnt += 1
    num += 1