case = int(input())

cnt_0 = [1, 0, 1]
cnt_1 = [0, 1, 1]

def fibo(N):
    lenn = len(cnt_0)
    if N >= lenn:
        for i in range(lenn, N+1):
            cnt_0.append(cnt_0[i - 2] + cnt_0[i - 1])
            cnt_1.append(cnt_1[i - 2] + cnt_1[i - 1])
    print(f'{cnt_0[N]} {cnt_1[N]}')
    
for i in range(case):
    N = int(input())
    fibo(N)
        

"""
과정 및 함수 설명
함수
1. append(value): 리스트의 끝부분에 value 값을 추가함.

과정
1. 먼저 0과 1의 개수가 담길 리스트를 각각 만든다.
2. input을 통해 값을 입력받는다.
3. 0과 1의 개수도 피보나치 수열을 따른다. 이 원리를 이용해 각 리스트에 1과 0의 개수를 삽입하는 반복문을 설정한다.
4. 반복문이 끝났다면 0과 1의 개수를 출력한다.
"""