score = int(input())

if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score <= 89:
    print('B')
elif score >= 70 and score <= 79:
    print('C')
elif score >= 60 and score <= 69:
    print('D')
else:
    print('F')

"""
과정 및 함수 설명
함수

과정
1. 점수를 입력받는다.
2. 점수에 맞는 성적을 찾고, 그 성적을 출력한다.
"""