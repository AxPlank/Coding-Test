year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)
else:
    print(0)

"""
과정 및 함수 설명
함수

과정
1. 년도를 입력받는다.
2. 윤년 여부를 출력한다.
"""