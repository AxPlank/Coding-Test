import sys

while 1:
    l_list = list(map(int, sys.stdin.readline().strip().split()))
    if sum(l_list) == 0:
        break
    l_max = max(l_list)
    l_list.remove(l_max)
    if l_list[0] ** 2 + l_list[1] ** 2 == l_max ** 2:
        print('right')
    else:
        print('wrong')

"""
과정
1. 값을 입력한다.
2. 직각삼각형 여부를 판단한다.
3. 결과에 알맞게 출력한다.
"""