# Sol 1
N = int(input()) // 4

output = " ".join(["long" for _ in range(N)])
print(f'{output} int')

# Sol 2
N = int(input()) // 4

for _ in range(N):
    print("long", end=" ")
    
print("int")