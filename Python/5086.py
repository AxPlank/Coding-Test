"""
백준 5086번: 배수와 약수
"""

import sys

while 1:
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    if n1 == 0 and n2 == 0:
        break
    
    if n2 % n1 == 0:
        print("factor")
    elif n1 % n2 == 0:
        print("multiple")
    else:
        print("neither")