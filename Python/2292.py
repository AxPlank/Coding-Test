import sys

N = int(sys.stdin.readline().strip())
cnt = 1
sequencee = 1

while N > sequencee:
    sequencee += 6 * cnt
    cnt += 1
    
print(cnt)

"""
과정
1. 문장을 입력한다.
2. 몇 칸 지나가야 하는지 출력한다.
"""