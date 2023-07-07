# Sol 1
D = list(map(int, input().split()))

if D[0] == D[1] == D[2]:
    print(10000 + D[0] * 1000)
elif D[0] == D[1]:
    print(1000 + D[0] * 100)
elif D[0] == D[2]:
    print(1000 + D[0] * 100)
elif D[1] == D[2]:
    print(1000 + D[1] * 100)
else:
    print(max(D) * 100)
    
# Sol 2
D1, D2, D3 = map(int, input().split())

if D1 == D2 == D3:
    print(10000 + D1 * 1000)
elif D1 == D2:
    print(1000 + D1 * 100)
elif D1 == D3:
    print(1000 + D1 * 100)
elif D2 == D3:
    print(1000 + D3 * 100)
else:
    print(max(D1, D2, D3) * 100)
    
"""
과정 및 함수 설명
함수

과정
1. 주사위 값을 입력한다.
2. 상황에 맞는 상금을 출력한다.
"""