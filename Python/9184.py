"""
백준 9184번: 신나는 함수 실행
"""
import sys

arr = [[[0 for i in range(21)] for i in range(21)] for i in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if arr[a][b][c] != 0:
        return arr[a][b][c]
    
    if a < b and b < c:
        arr[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return arr[a][b][c]
    else:
        arr[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return arr[a][b][c]
    
while 1:
    a, b, c = map(int, sys.stdin.readline().strip().split())
    
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')