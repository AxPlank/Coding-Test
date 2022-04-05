import sys

C = int(sys.stdin.readline().strip())

for i in range(C):
    N = list(map(int, sys.stdin.readline().strip().split()))
    score_list = N[1:]
    score_mean = sum(score_list) / len(score_list)
    cnt = 0
    for i in score_list:
        if i > score_mean:
            cnt += 1
    ratio = cnt / N[0] * 100
    print(f'{ratio:.3f}%')
            
            

"""
과정 및 함수 설명
함수

과정
1. 테스트 케이스를 몇 개로 할지 입력받는다.
2. 학생 수와 각 학생의 성적을 입력하고, 성적의 평균을 계산한다.
3. 평균 이상의 성적을 가진 학생이 몇 명인지 센 후, 그 비율을 백분율로 출력한다.
"""