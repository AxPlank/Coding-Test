case = int(input())

for i in range(case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    
    if abs(r1-r2) < distance < r1+r2:
        print(2)
    elif r1 - r2 == 0 and distance == 0:
        print(-1)
    elif abs(r1-r2) == distance or r1+r2 == distance:
        print(1)
    else:
        print(0)

"""
과정 및 함수 설명
함수

과정
1. input을 통해 값을 입력받는다.
2. split을 통해 input값을 리스트로 변환하고, 그 값을 map을 통해 정수로 변환한다.
3. 받은 좌표((x1, y1), (x2, y2))를 이용해 두 원 사이의 거리(이하 distance)를 구한다.
4. distance와 두 반지름(r1, r2)를 이용해 가능한 위치의 수를 출력한다
"""