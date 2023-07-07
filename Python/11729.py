import sys

def hanoi(n, outt, inn):
    if n == 1:
        print(outt, inn)
        return 0
        
    hanoi(n-1, outt, 6-inn-outt)
    print(outt, inn)
    hanoi(n-1, 6-outt-inn, outt)

N = int(sys.stdin.readline().strip())
print(2 ** N - 1)
hanoi(N, 1, 3)

"""
과정
1. 값을 입력받는다.
2. 움직임 수와 모든 이동 경로를 출력한다.
"""