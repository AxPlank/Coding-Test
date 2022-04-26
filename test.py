listt = [1, 2, 3, 4]

def listtt(arr):
    for i in range(len(arr)):
        if arr[i] == 2:
            print('y')
            return True
    print('n')
    return False

listtt(listt)