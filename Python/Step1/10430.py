A, B, C = map(int, input().split())
print((A+B) % C)
print(((A%C)+(B%C)) % C)
print((A*B) % C)
print(((A%C)*(B%C)) % C)

"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 각각의 계산값을 출력한다.
"""