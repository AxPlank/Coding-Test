# Sol 1: sorted() 이용
import sys

N = int(sys.stdin.readline().strip())

"""
숫자를 입력받기 위한 반복문. 반복문 진행순서
1. 숫자를 입력받는다.
2. 입력받은 숫자를 숫자를 모아두기 위해 만든 리스트에 추가한다.
"""
num_list = []
for i in range(N):
    number = int(sys.stdin.readline().strip())
    num_list.append(number)
    
"""
리스트를 정렬하고 출력하기 위한 반복문
"""
num_list = sorted(num_list)
for i in num_list:
    print(i)

# Sol 2: sort() 이용
import sys

N = int(sys.stdin.readline().strip())

"""
숫자를 입력받기 위한 반복문. 반복문 진행순서
1. 숫자를 입력받는다.
2. 입력받은 숫자를 숫자를 모아두기 위해 만든 리스트에 추가한다.
"""
num_list = []
for i in range(N):
    number = int(sys.stdin.readline().strip())
    num_list.append(number)
    
"""
리스트를 정렬하고 출력하기 위한 반복문
"""
num_list = sorted(num_list)
for i in num_list:
    print(i)

# Sol 3: 반복문 이용
import sys

N = int(sys.stdin.readline().strip())

"""
숫자를 입력받기 위한 반복문. 반복문 진행순서
1. 숫자를 입력받는다.
2. 입력받은 숫자를 숫자를 모아두기 위해 만든 리스트에 추가한다.
"""
num_list = []
for i in range(N):
    number = int(sys.stdin.readline().strip())
    num_list.append(number)
    
"""
리스트를 정렬하고 출력하기 위한 반복문
"""
for i in range(N-1):
    for j in range(i+1, N):
        if num_list[i] > num_list[j]:
            temp = num_list[i]
            num_list[i] = num_list[j]
            num_list[j] = temp
for i in num_list:
    print(i)