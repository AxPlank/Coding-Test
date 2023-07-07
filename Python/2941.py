import sys

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = sys.stdin.readline().strip()

for i in croatia:
    if i in word:
        word = word.replace(i, '_')
            
print(len(word))

"""
과정
1. 문장을 입력한다.
2. 몇 개의 단어가 들어가 있는지 단어의 개수를 출력한다.
"""