"""
백준 14888번: 연산자 끼워넣기
"""
import sys

def insert_operators(dep, plus, minus, multi, divide, ret):
    global minret
    global maxret
    if dep == max_dep:
        minret = min(minret, ret)
        maxret = max(maxret, ret)
        return
    
    if plus:
        insert_operators(dep+1, plus-1, minus, multi, divide, ret+nums[dep])
    if minus:
        insert_operators(dep+1, plus, minus-1, multi, divide, ret-nums[dep])
    if multi:
        insert_operators(dep+1, plus, minus, multi-1, divide, ret*nums[dep])
    if divide:
        if ret < 0:
            ret = ((ret*-1) // nums[dep]) * -1
            insert_operators(dep+1, plus, minus, multi-1, divide, ret)
        else:
            insert_operators(dep+1, plus, minus, multi-1, divide, ret//nums[dep])

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))
operators = list(map(int, sys.stdin.readline().strip().split()))
minret = sys.maxsize
maxret = -sys.maxsize
max_dep = len(nums)

insert_operators(1, operators[0], operators[1], operators[2], operators[3], nums[0])

print(f'{maxret}\n{minret}')