import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    str_input = sys.stdin.readline().rstrip()
    
    print(f'{str_input[0]}{str_input[-1]}')