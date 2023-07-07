# Sol 1
import sys

x1, y1 = map(int, sys.stdin.readline().strip().split())
x2, y2 = map(int, sys.stdin.readline().strip().split())
x3, y3 = map(int, sys.stdin.readline().strip().split())

x_list = [x1, x2, x3]
y_list = [y1, y2, y3]

if x_list.count(max(x_list)) == 2:
    if y_list.count(max(y_list)) == 2:
        print(min(x_list), min(y_list))
    else:
        print(min(x_list), max(y_list))
else:
    if y_list.count(max(y_list)) == 2:
        print(max(x_list), min(y_list))
    else:
        print(max(x_list), max(y_list))

# Sol 2
import sys

x_list = []
y_list = []

for i in range(3):
    x, y = map(int, sys.stdin.readline().strip().split())
    x_list.append(x)
    y_list.append(y)

x = 0
y = 0
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y = y_list[i]
        
print(x, y)

"""
과정
1. 값을 입력한다.
2. 네 번째 좌표를 찾아 출력한다.
"""