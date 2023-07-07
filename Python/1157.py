import sys

txt = sys.stdin.readline().strip().upper()
txt_set = list(set(txt))
cnt_list = []

for i in txt_set:
    cnt_list.append(txt.count(i))
    
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(txt_set[cnt_list.index(max(cnt_list))])

"""
과정 및 함수 설명
함수

과정
1. 값을 입력한다.
2. 각 글자를 배수만큼 늘린다.
3. 최종 결과를 출력한다.
"""