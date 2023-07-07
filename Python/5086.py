"""
백준 5086번: 배수와 약수
"""

import sys

while 1:
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    """
    입력값이 0인지 확인
    """
    if n1 == 0 and n2 == 0:
        break
    
    """
    두 수의 관계 확인
    """
    if n2 % n1 == 0: # n1이 n2의 약수
        print("factor")
    elif n1 % n2 == 0: # n1이 n2의 배수
        print("multiple")
    else: # 둘 다 아닐 때
        print("neither")