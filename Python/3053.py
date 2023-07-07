import sys
import math

R = int(sys.stdin.readline().strip())

euclid_area = math.pi * (R ** 2)
manhattan_area = 2 * (R ** 2)

print(f'{euclid_area: .6f}')
print(f'{manhattan_area: .6f}')

"""
과정
1. 반지름을 입력한다.
2. 각 기하학에 맞는 값을 출력한다.
"""