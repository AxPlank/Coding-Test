import sys

subject_number = int(sys.stdin.readline().strip())
subject_score = list(map(int, sys.stdin.readline().strip().split()))
new_score = []

for i in subject_score:
    new_score.append(i / max(subject_score) * 100)
    
print(new_score)    
print(sum(new_score) / subject_number)

"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 나머지를 구한다.
3. 나머지가 리스트에 존재하지 않는다면, 그 값을 리스트에 추가한다.
"""