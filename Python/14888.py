"""
백준 14888번: 연산자 끼워넣기
"""
import sys

def dfs_insertOperators(cnt, max_dep, ret, plus, minus, multi, divide):
    global ret_max
    global ret_min
    
    if cnt == max_dep:
        ret_max = max(ret_max, ret)
        ret_min = min(ret_min, ret)
        return
    
    if plus != 0:
        dfs_insertOperators(cnt+1, max_dep, ret+nums[cnt+1], plus-1, minus, multi, divide)
    if minus != 0:
        dfs_insertOperators(cnt+1, max_dep, ret-nums[cnt+1], plus, minus-1, multi, divide)
    if multi != 0:
        dfs_insertOperators(cnt+1, max_dep, ret*nums[cnt+1], plus, minus, multi-1, divide)
    if divide != 0:
        if ret > 0:
            ret = ret // nums[cnt+1]
            dfs_insertOperators(cnt+1, max_dep, ret, plus, minus, multi, divide-1)
        else:
            ret = -1 * ret
            ret = ret // nums[cnt+1]
            ret = -1 * ret
            dfs_insertOperators(cnt+1, max_dep, ret, plus, minus, multi, divide-1)
        
N = int(sys.stdin.readline())
nums = tuple(map(int, sys.stdin.readline().strip().split()))
operators = list(map(int, sys.stdin.readline().strip().split()))

ret_max = -1000000000
ret_min = -ret_max

dfs_insertOperators(0, sum(operators), nums[0], operators[0], operators[1], operators[2], operators[3])
print(ret_max)
print(ret_min)