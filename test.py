def factorizationn(n):
    print(n)
    factor_list = [0] * (n + 1)
    i = 2
    while n > 2 and i <= n:
        if n % i == 0:
            factor_list[i] += 1
            n = n / i
            print(n)
        else:
            i += 1
    
    return factor_list

factorizationn(24)