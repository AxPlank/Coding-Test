import sys

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
N = sys.stdin.readline().strip()
time = 0

for i in N:
    for j in dial:
        if i in j:
            time += dial.index(j) + 3
            
print(time)

"""
과정
1. 값을 입력한다.
2. 시간을 계산하여 출력한다.
"""