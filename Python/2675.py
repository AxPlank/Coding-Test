import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    R, S = sys.stdin.readline().strip().split()
    txt = ''
    for i in S:
        txt += i * int(R)
    print(txt)

"""
과정 및 함수 설명
함수

과정
1. 값을 입력한다.
2. 각 글자를 배수만큼 늘린다.
3. 최종 결과를 출력한다.
"""