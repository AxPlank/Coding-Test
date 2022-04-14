"""
백준 1181번: 단어 정렬
"""
import sys
from functools import cmp_to_key

def word_sort(a, b):
    # 단어의 길이 비교
    if len(a) > len(b):
        return 1
    elif len(a) == len(b):
        # 사전 순서대로 비교
        i = 0
        while i < len(a):
            if ord(a[i]) > ord(b[i]):
                return 1
            elif ord(a[i]) == ord(b[i]):
                i += 1
            else:
                return -1
    else:
        return -1
    
N = int(sys.stdin.readline())
word_list = [0] * N

for i in range(N):
    word_list[i] = sys.stdin.readline().strip()
    
word_list = sorted(set(word_list), key=cmp_to_key(word_sort))

for i in word_list:
    print(i)