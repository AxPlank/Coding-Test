"""
백준 11478번: 서로 다른 문자열의 개수
"""
import sys

S = sys.stdin.readline().strip()
string_set = set()

for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        string_set.add(S[i:j])
        
print(len(string_set))