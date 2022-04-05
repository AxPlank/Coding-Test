import sys
import time
import random

# N = int(sys.stdin.readline().strip())

num_list = []
# for i in range(N):
#     num = int(sys.stdin.readline().strip())
#     num_list.append(num)
    
for i in range(10000000):
    num_list.append(random.randint(1, 10001))

sort_list = []
start = time.time()
for i in range(1, 10001):
    if len(sort_list) == len(num_list):
        break
    if i not in num_list:
        continue
    sort_list += [i] * num_list.count(i)
    
for i in sort_list:
    print(i)
print(start - time.time())