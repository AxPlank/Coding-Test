import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    quiz_check = list(sys.stdin.readline().strip())
    score = 0
    score_num = 0
    for i in quiz_check:
        if i == 'O':
            score_num += 1
            score += score_num
        else:
            score_num = 0
    print(score)
            
            

"""
과정 및 함수 설명
함수

과정
1. 테스트 케이스를 몇 개로 할지 입력받는다.
2. 정답 오답 여부를 입력받는다.
3. 주어진 룰에 따라 점수를 계산하고, 계산이 끝나면 최종 점수를 출력한다.
"""