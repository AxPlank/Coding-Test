# Sol 1
import sys

N1, N2 = sys.stdin.readline().strip().split()

N1 = int(N1[::-1])
N2 = int(N2[::-1])
    
print(max(N1, N2))

# Sol 2
import sys

N = sys.stdin.readline().strip().split()

for i in range(len(N)):
    N[i] = int(''.join(reversed(N[i])))
    
print(max(N))

"""
과정
1. 값을 입력한다.
2. 입력받은 수를 뒤집는다.
3. 큰 값을 출력한다.
"""