def solvee(n):
    return n + sum(map(int, str(n)))

num_set = {i for i in range(1, 10000)}
no_selfnumber = set()

for i in num_set:
    no_selfnumber.add(solvee(i))
    
num_set = sorted(num_set - no_selfnumber)
for i in num_set:
    print(i)
    
"""
과정 및 함수 설명
함수

과정
1. 집합을 두 개 만든다. 하나는 1부터 9999까지 수가 담겨있고 다른 하나는 문제에서 주어지는 연산을 이용해 나오는 값을 저장하기 위한 것이다.
2. 정의한 함수를 이용해 주어진 연산을 수행하고 리턴되는 값을 no_selfnumber에 저장한다.
3. num_set에서 no_selfnumber를 뺀 후, 정렬한다.
4. 출력한다.
"""