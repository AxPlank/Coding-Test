import sys

N = int(sys.stdin.readline().strip())
cnt = N

for i in range(N):
    word = sys.stdin.readline().strip()
    for i in range(len(word)-1):
        print(word[i] in word[i+1:], word[i+1:])
        if (word[i] != word[i+1]) and (word[i] in word[i+1:]):
            cnt -= 1
            break;
        
print(cnt)

"""
과정
1. 문장을 입력한다.
2. 그룹 단어의 개수를 출력한다.
"""