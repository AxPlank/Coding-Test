import sys

M, N = map(int, sys.stdin.readline().strip().split())

chess_table = []
cnt_list = []

for i in range(M):
    table_line = list(sys.stdin.readline().strip())
    chess_table.append(table_line)
    
for i in range(M-7):
    for j in range(N-7):
        cnt_W = 0 # 제일 왼쪽 제일 윗칸이 흰색으로 시작
        cnt_B = 0 # 제일 왼쪽 제일 윗칸이 검은색으로 시작
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if chess_table[k][l] != 'W':
                        cnt_W += 1
                    if chess_table[k][l] != 'B':
                        cnt_B += 1
                else:
                    if chess_table[k][l] != 'B':
                        cnt_W += 1
                    if chess_table[k][l] != 'W':
                        cnt_B += 1
        cnt_list.append(min(cnt_W, cnt_B))
        
print(min(cnt_list))

"""
과정
1. 값을 입력받는다.
2. 순위를 정한다.
3. 순위를 출력한다.
"""