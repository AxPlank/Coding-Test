# Sol 1
import sys

remainder_list = []

for i in range(10):
    N = int(sys.stdin.readline().strip())
    N = N % 42
    if N not in remainder_list:
        remainder_list.append(N)
        
print(len(remainder_list))

# Sol 2
import sys

remainder_list = []

for i in range(10):
    N = int(sys.stdin.readline().strip())
    N = N % 42
    remainder_list.append(N)
        
remainder_set = set(remainder_list)
print(len(remainder_set))

"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 나머지를 구한다.
3. 나머지가 리스트에 존재하지 않는다면, 그 값을 리스트에 추가한다.
"""