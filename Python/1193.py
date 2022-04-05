import sys

N = int(sys.stdin.readline().strip())
line = 1

while N > line:
    N -= line
    line += 1
    
if line % 2 == 0:
    print(f'{N}/{line+1-N}')
else:
    print(f'{line+1-N}/{N}')

"""
과정
1. 문장을 입력한다.
2. 자리에 해당하는 분수를 찾아 출력한다.
"""