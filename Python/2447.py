import sys

def def_star(n):
    star_print = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            star_print.append(n[i%len(n)] + ' '*len(n) + n[i%len(n)])
        else:
            star_print.append(n[i%len(n)] * 3)
    return star_print

n = int(sys.stdin.readline().strip())
cnt = 0
star_base = ['***', '* *', '***']

while n > 3:
    n /= 3
    cnt += 1

for i in range(cnt):
    star_base = def_star(star_base)
    
for i in star_base:
    print(i)

"""
과정
1. 값을 입력받는다.
2. 패턴을 출력한다.
"""