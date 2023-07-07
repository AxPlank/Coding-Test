case = int(input())

for _ in range(case):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0

    for i in range(n):
        cx, cy, r = map(int, input().split())
        d1 = ((x1-cx) ** 2 + (y1-cy) ** 2) ** 0.5
        d2 = ((x2-cx) ** 2 + (y2-cy) ** 2) ** 0.5
        if (d1 > r and d2 < r) or (d1 < r and d2 > r):
            cnt += 1
    print(cnt)
            
"""
과정 및 함수 설명
함수
1. append(value): 리스트의 끝부분에 value 값을 추가함.

과정
1. 먼저 0과 1의 개수가 담길 리스트를 각각 만든다.
2. input을 통해 값을 입력받는다.
3. 0과 1의 개수도 피보나치 수열을 따른다. 이 원리를 이용해 각 리스트에 1과 0의 개수를 삽입하는 반복문을 설정한다.
4. 반복문이 끝났다면 0과 1의 개수를 출력한다.
"""