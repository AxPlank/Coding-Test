X = int(input())
T = int(input())
sum = 0

for _ in range(0, T):
    a, b = map(int, input().split())
    sum += a * b
    
if X == sum:
    print("Yes")
else:
    print("No")