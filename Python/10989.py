import sys

N = int(sys.stdin.readline())
num_input = [0] * 10000 # 원소들을 분류했을 때 각각 몇 개 있는지 개수를 담을 리스트

# 원소들을 확인하고 원소에 대응하는 인덱스에 원소가 몇 개 있는지 입력
for _ in range(N):
    num = int(sys.stdin.readline())
    num_input[num-1] += 1

# 오름차순으로 정렬하여 출력
for i in range(10000):
    if num_input[i] != 0:
        for _ in range(num_input[i]):
            print(i)
            
# Sol 2
def countingsort(arr_input):
    arr_output = [0] * len(arr_input)
    arr_count = [0] * (max(arr_input) + 1)
    
    for i in arr_input:
        arr_count[i] += 1
    
    for i in range(1, len(arr_count)):
        arr_count[i] += arr_count[i-1]
        
    for i in range(len(arr_input)-1, -1, -1):
        arr_output[arr_count[arr_input[i]]-1] = arr_input[i]
        arr_count[arr_input[i]] -= 1
        
    for i in arr_output:
        print(i)
        
countingsort(num_input)