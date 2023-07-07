"""
백준 18870: 좌표 압축
"""
"""
변환 좌표 값: 해당 인덱스에 위치한 원소보다 작은 값의 갯수
"""
import sys

N = int(sys.stdin.readline())

input_list = list(map(int, sys.stdin.readline().strip().split()))
num_list = list(sorted(set(input_list)))
num_dict = {num_list[i]: i for i in range(len(num_list))}

for i in range(N):
    print(num_dict[input_list[i]], end=' ')