"""
백준 9375번: 패션왕 신해빈
"""
import sys

T = int(sys.stdin.readline()) # 테스트 케이스 입력

for _ in range(T):
    n = int(sys.stdin.readline()) # 옷의 수 입력
    if n == 0: # 옷의 수가 0일 때
        print(0)
        continue
    
    dictt = dict() # 종류별 옷의 수를 담을 딕셔너리
    for _ in range(n):
        name, part = map(str, sys.stdin.readline().strip().split())
        if part not in dictt.keys():
            dictt[part] = 2 # 입지 않을 경우를 고려해서 2로 지정
            continue
        
        dictt[part] += 1
            
    combb = 1
    for i in dictt.keys():
        combb *= dictt[i]
        
    print(combb - 1) # 아무것도 입지 않는 경우 제외