"""
백준 1427번: 소트인사이드
"""
import sys

number = sorted(map(int,list(sys.stdin.readline().strip())), reverse=True)

for i in number:
    print(i, end='')