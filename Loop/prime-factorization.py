def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_fact(n):
    lst = []
    for i in range(2, n):
        if prime:
            lst.append(i)
    
    factor = lst[0]
    ind = 1
    while True:
        for i in lst[ind:]:
            if i * factor == n:
                return i
                
        factor = lst[ind]
        ind += 1
        if ind >= len(lst):
            return False

if __name__ == "__main__":
    n = int(input())

    print(prime_fact(n))
    